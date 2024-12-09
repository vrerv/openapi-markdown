# OpenAPI Documentation Generator

This is a Python script that generates API documentation from an OpenAPI specification file.

## Usage

`pip install openapi-markdown`

### CLI

You can use `openapi2markdown` command as follows:

```
% openapi2markdown --help                
Usage: openapi2markdown [OPTIONS] INPUT_FILE [OUTPUT_FILE]

  Convert OpenAPI spec to Markdown documentation.

  INPUT_FILE: Path to OpenAPI specification file (JSON or YAML) OUTPUT_FILE:
  Path where markdown file will be generated (optional, defaults to INPUT_FILE
  with .md extension)

Options:
  -t, --templates-dir DIRECTORY  Custom templates directory path
  -f, --filter-paths TEXT        Only generate apis that start with the given
                                 path, multiple paths are allowed
```

### Library

```python
from openapi_markdown.generator import to_markdown

apiFile = "./tests/openapi.json"
outputFile = "api_doc.md"
templatesDir = "templates"
options = {
    'filter_paths': ['/client']
}

to_markdown(apiFile, outputFile, templates_dir, options)
```

- If you want to use your own template, creates 'templates' directory and put [`api_doc_template.md.j2`](src/openapi_markdown/templates/api_doc_template.md.j2) file in it.
- You can change templates directory by passing it as the 3rd argument of `to_markdown`.

### Default templates

There are internal templates you can use. If not set default is used.

* templates - default
* templates/embed - prints objects hierarchially as list in every request/response

## Development

### Requirements

- Python 3.x
- json
- PyYAML
- openapi-core
- Jinja2

`pip install -r requirement.txt`

install a project in editble mode
`pip install -e ./`

run tests

`python -m unittest`

### Deploy

```
python3 -m pip install --upgrade twine
```

```
./pypi.sh
```
