#! /usr/bin/env python

import click
from openapi_markdown.generator import to_markdown
import os

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path(), required=False)
@click.option('--templates-dir', '-t',
              type=click.Path(exists=False, file_okay=False, dir_okay=True),
              default='templates',
              help='Custom templates directory path')
@click.option('--filter-paths', '-f',
              type=click.STRING,
              multiple=True,
              help='Only generate apis that start with the given path, multiple paths are allowed')
def main(input_file, output_file, templates_dir, filter_paths):
    """Convert OpenAPI spec to Markdown documentation.

    INPUT_FILE: Path to OpenAPI specification file (JSON or YAML)
    OUTPUT_FILE: Path where markdown file will be generated (optional, defaults to INPUT_FILE with .md extension)
    """
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.md'
        
    try:
        # Use default templates if templates_dir is not provided
        to_markdown(input_file, output_file, templates_dir, options = {
            'filter_paths': filter_paths
        })
        click.echo(f"Successfully generated markdown documentation at {output_file}")
    except Exception as e:
        raise e

if __name__ == '__main__':
    main()