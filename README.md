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

run tests - not unit tests

`python tests/test.py`

## Usage

```python
from openapi_markdown.generator import to_markdown

apiFile = "./tests/openapi.json"
outputFile = "api_doc.md"

to_markdown(apiFile, outputFile)
```

## Deploy

```
python3 -m pip install --upgrade twine
```

```
./pypi.sh
```
