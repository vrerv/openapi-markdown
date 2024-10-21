# OpenAPI Documentation Generator

This is a Python script that generates API documentation from an OpenAPI specification file.

## Requirements

- Python 3.x
- json
- PyYAML
- openapi-core
- Jinja2

## Development

`pip install -r requirement.txt`

install a project in editble mode
`pip install -e ./`

run tests

`python -m unittest`

## Usage

```python
from openapi_markdown.generator import to_markdown

apiFile = "./tests/openapi.json"
outputFile = "api_doc.md"

to_markdown(apiFile, outputFile)
```

- If you want to use your own template, creates 'templates' directory and put [`api_doc_template.md.j2`](src/openapi_markdown/templates/api_doc_template.md.j2) file in it.
- You can change templates directory by passing it as the 3rd argument of `to_markdown`.


## Deploy

```
python3 -m pip install --upgrade twine
```

```
./pypi.sh
```
