#!/bin/bash

rm -rf ./dist
python -m build
python3 -m twine upload --repository pypi --username __token__ --password $PYPI_API_TOKEN dist/*

