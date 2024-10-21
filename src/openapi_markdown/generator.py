import json
import os

import yaml
from jinja2 import Environment, FileSystemLoader, PackageLoader
from openapi_core import Spec


def to_json(value):
    return json.dumps(value, indent=2)


def ref_to_link(ref):
    if not ref:
        return ""
    for key in ref.keys():
        if key == '$ref':
            parts = ref['$ref'].split("/")
            schema_name = parts[-1]
            return f"[{schema_name}](#{schema_name.lower()})"
        elif key == 'type':
            return f"{ref[key]}"
        else:
            return 'Not implemented type}'


def ref_to_param(ref, spec_data):
    if not ref:
        return None
    for key in ref.keys():
        if key == '$ref':
            parts = ref['$ref'].split("/")
            schema_type = parts[-2]
            schema_name = parts[-1]
            if schema_type == "parameters":
                # Find parameter in components and return the parameter object
                param = spec_data.get("components", {}).get("parameters", {}).get(
                    schema_name)
                return param
    return ref


def to_markdown(api_file, output_file, templates_dir='templates'):
    # Load the OpenAPI 3.0 specification file in either JSON or YAML format
    with open(api_file) as f:
        spec_data = json.load(f) if api_file.endswith(".json") else yaml.safe_load(f)
    spec = Spec.from_dict(spec_data)
    # Load the Jinja2 template file
    if os.path.exists(templates_dir):
        env = Environment(loader=FileSystemLoader(templates_dir))
    else:
        env = Environment(loader=PackageLoader('openapi_markdown', 'templates'))
    env.filters['ref_to_link'] = ref_to_link
    env.filters['to_json'] = to_json
    template = env.get_template('api_doc_template.md.j2')
    rendered_template = template.render(spec=spec,
                                        ref_to_param=lambda ref: ref_to_param(ref,
                                                                              spec_data))
    with open(output_file, "w") as f:
        f.write(rendered_template)
