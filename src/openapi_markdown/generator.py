import json
import os

import yaml
from jinja2 import Environment, FileSystemLoader, PackageLoader
from openapi_core import Spec
from warnings import warn


def to_json(value):
    return json.dumps(value, indent=2)


def ref_to_link(ref):
    if not ref:
        return ""
    if ref.get('$ref'):
        parts = ref['$ref'].split("/")
        schema_name = parts[-1]
        return f"[{schema_name}](#{schema_name.lower()})"
    elif ref.get('type'):
        return f"{ref['type']}"
    return ""


def ref_to_param(ref, spec_data):
    warn('ref_to_param is deprecated. Use ref_to_schema directly.', DeprecationWarning,
         stacklevel=2)
    return ref_to_schema(ref, spec_data)


def ref_to_schema(schema, spec_data):
    """Convert a schema reference to actual schema object, recursively resolving all
    nested references while preserving $ref."""
    if isinstance(schema, dict):
        if '$ref' in schema:
            # Get the referenced schema
            ref_path = schema['$ref'].split('/')
            current = spec_data
            for part in ref_path[1:]:  # Skip the first '#' element
                current = current[part]
            # Merge the referenced schema with the original, keeping $ref
            resolved = ref_to_schema(current, spec_data)
            return {**resolved, **schema}
        else:
            # Process all dictionary values recursively
            return {k: ref_to_schema(v, spec_data) for k, v in schema.items()}
    elif isinstance(schema, list):
        # Process all list items recursively
        return [ref_to_schema(item, spec_data) for item in schema]
    return schema


def to_markdown(api_file, output_file, templates_dir='templates', options={}):
    # Load the OpenAPI 3.0 specification file in either JSON or YAML format
    with open(api_file) as f:
        spec_data = json.load(f) if api_file.endswith(".json") else yaml.safe_load(f)
    # Resolve all references in the spec data
    # spec_data = ref_to_schema(spec_data, spec_data)
    # filter spec_data.paths if filter_paths option is provided
    if 'filter_paths' in options:
        spec_data['paths'] = {
            k: v for k, v in spec_data['paths'].items()
            if any(k.startswith(prefix) for prefix in options['filter_paths'])
        }
    spec = Spec.from_dict(spec_data)
    # Load the Jinja2 template file
    if os.path.exists(templates_dir):
        env = Environment(loader=FileSystemLoader(templates_dir))
    else:
        env = Environment(loader=PackageLoader('openapi_markdown', templates_dir))
    env.filters['ref_to_link'] = ref_to_link
    env.filters['to_json'] = to_json
    env.filters['ref_to_param'] = ref_to_param
    env.filters['ref_to_schema'] = ref_to_schema
    template = env.get_template('api_doc_template.md.j2')
    rendered_template = (
        template.render(spec=spec,
                        ref_to_param=lambda ref: ref_to_param(ref, spec_data),
                        ref_to_schema=lambda ref: ref_to_schema(ref, spec_data))
    )
    with open(output_file, "w") as f:
        f.write(rendered_template)
