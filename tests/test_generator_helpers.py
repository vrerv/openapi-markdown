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

    def test_ref_to_schema_oneOf(self):
        schema = {
            "data": {
                "oneOf": [
                    {
                        "$ref": "#/components/schemas/Pet"
                    },
                    {
                        "$ref": "#/components/schemas/Pet"
                    },
                ]
            },
        }

        result = ref_to_schema(schema, self.spec_data)
        self.assertEqual(result, {
            "data": {
                "oneOf": [
                    {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "age": {"type": "integer"}
                        },
                        "$ref": "#/components/schemas/Pet"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "age": {"type": "integer"}
                        },
                        "$ref": "#/components/schemas/Pet"
                    }
                ]
            }
        })

    def test_ref_to_schema_additionalProperties(self):
        schema = {
            "data": {
                "additionalProperties": {
                    "$ref": "#/components/schemas/Pet"
                }
            },
        }

        result = ref_to_schema(schema, self.spec_data)
        self.assertEqual(result, {
            "data": {
                "additionalProperties": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"}
                    },
                    "$ref": "#/components/schemas/Pet"
                }
            }
        })
