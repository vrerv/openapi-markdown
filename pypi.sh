#!/bin/bash

rm -rf ./dist
python -m build
python -m twine upload --repository pypi --username __token__ --password $PYPI_API_TOKEN dist/*

