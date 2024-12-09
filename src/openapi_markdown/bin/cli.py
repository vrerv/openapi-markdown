#! /usr/bin/env python

import click
from openapi_markdown.generator import to_markdown
import os

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path(), required=False)
@click.option('--templates-dir', '-t',
              type=click.Path(exists=True, file_okay=False, dir_okay=True),
              help='Custom templates directory path')
def main(input_file, output_file, templates_dir):
    """Convert OpenAPI spec to Markdown documentation.

    INPUT_FILE: Path to OpenAPI specification file (JSON or YAML)
    OUTPUT_FILE: Path where markdown file will be generated (optional, defaults to INPUT_FILE with .md extension)
    """
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.md'
        
    try:
        # Use default templates if templates_dir is not provided
        if templates_dir is None:
            to_markdown(input_file, output_file)
        else:
            to_markdown(input_file, output_file, templates_dir)
        click.echo(f"Successfully generated markdown documentation at {output_file}")
    except Exception as e:
        raise e

if __name__ == '__main__':
    main()