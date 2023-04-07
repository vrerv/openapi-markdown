from openapi_markdown.generator import to_markdown

apiFile = "./tests/openapi.json"
outputFile = "api_doc.md"

to_markdown(apiFile, outputFile)
