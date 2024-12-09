import unittest

from openapi_markdown.generator import ref_to_schema


class TestGeneratorHelpers(unittest.TestCase):
    spec_data = {
        "components": {
            "schemas": {
                "Pet": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"}
                    }
                }
            }
        }
    }

    def test_ref_to_schema(self):
        schema = {
            "schema": {
                "$ref": "#/components/schemas/Pet"
            }
        }

        result = ref_to_schema(schema, self.spec_data)
        self.assertEqual(result, {
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "integer"}
                },
                "$ref": "#/components/schemas/Pet"
            }
        })

    def test_ref_to_schema_array(self):
        # Sample OpenAPI spec data with schemas
        schema = {
            "schema": {
                "type": "array",
                "items": {
                    "$ref": "#/components/schemas/Pet"
                }
            }
        }

        result = ref_to_schema(schema, self.spec_data)
        self.assertEqual(result, {
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"}
                    },
                    "$ref": "#/components/schemas/Pet"
                }
            }
        })
