import os
import unittest

from openapi_markdown.generator import to_markdown

TESTOUT_EXTENSION = '.testout.md'
TESTDIR = './' if os.getcwd().endswith('tests') else 'tests/'
KEEP_OUT_FILES = os.getenv('KEEP_OUT_FILES', 'false').lower() == 'true'


class TestToMarkdown(unittest.TestCase):

    def tearDown(self):
        if not KEEP_OUT_FILES:
            for file in os.listdir(TESTDIR):
                if file.endswith(TESTOUT_EXTENSION):
                    os.remove(TESTDIR + file)

    def test_to_markdown(self):
        test_cases = [
            ("test-api.json", "expected_test-api.md"),
            ("test-api2.yaml", "expected_test-api2.md")
        ]

        for api_file, expected_output_file in test_cases:
            with self.subTest(api_file=api_file,
                              expected_output_file=expected_output_file):
                self._test_to_markdown(api_file, expected_output_file)

    def _test_to_markdown(self, api_file, expected_output_file):
        output_file = api_file + TESTOUT_EXTENSION
        to_markdown(TESTDIR + api_file, TESTDIR + output_file, templates_dir='templates')

        # read output file and compare it to the expected output file
        with open(TESTDIR + output_file, 'r') as f:
            output = f.read()
        with open(TESTDIR + expected_output_file, 'r') as f:
            expected_output = f.read()
        self.assertEqual(output, expected_output)
