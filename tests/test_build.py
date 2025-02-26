import unittest

import os
from esbuild_py import build, EsbuildError

class TestTransform(unittest.TestCase):
    first_file = {
        "name": './first-file.ts',
        "content": "export const B: string = 'hello typescript';"
    }
    second_file = {
        "name": './second_file.ts',
        "content": "import {B} from './first-file'; console.log(B);"
    }
    output_file_name = './output.js'
    expected = '''  
(() => {
  // first-file.ts
  var B = "hello typescript";

  // second_file.ts
  console.log(B);
})();
'''.strip()
    def write_file(self, file, content = None):
        file_name= file["name"]
        try:
            os.remove(file_name)
        except OSError:
            pass
        with open(file_name, "a") as f:
            f.write(file["content"] if content is None else content) 

    def atest_error(self):
        self.write_file(self.first_file)
        bad_content = "'".join([self.second_file["content"], ""]);
        self.write_file(self.second_file, bad_content)
        with self.assertRaises(EsbuildError):
            build(self.second_file["name"], self.output_file_name)

    def test_build(self):
        self.write_file(self.first_file)
        self.write_file(self.second_file)
        try:
            build(self.second_file["name"], self.output_file_name)
            with open(self.output_file_name, "r") as f:
                result = f.read()
            os.remove(self.output_file_name)
        finally:
            os.remove(self.first_file["name"])
            os.remove(self.second_file["name"])
        self.assertEqual(result.strip(), self.expected)
