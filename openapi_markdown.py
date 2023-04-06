import json

import yaml
from jinja2 import Environment, FileSystemLoader
from openapi_core import Spec


def to_json(value):
    return json.dumps(value, indent=2)


def ref_to_link(ref):
    if not ref:
        return ""
    parts = ref['$ref'].split("/")
    schema_name = parts[-1]
    return f"[{schema_name}](#{schema_name.lower()})"


apiFile = "./test/openapi.json"
outputFile = "api_doc.md"

# Load the OpenAPI 3.0 specification file in either JSON or YAML format
with open(apiFile) as f:
    spec_data = json.load(f) if apiFile.endswith(".json") else yaml.safe_load(f)

spec = Spec.from_dict(spec_data)

# Load the Jinja2 template file
# env = Environment(loader=PackageLoader('my_package', 'templates'))
env = Environment(loader=FileSystemLoader('./templates'))
env.filters['ref_to_link'] = ref_to_link
env.filters['to_json'] = to_json

template = env.get_template('api_doc_template.md.j2')

rendered_template = template.render(spec=spec)

with open(outputFile, "w") as f:
    f.write(rendered_template)
