import unittest

from esbuild_py import transform


class TestTransform(unittest.TestCase):

    def test_jsx(self):
        jsx = """
import * as React from 'react'
import * as ReactDOM from 'react-dom'

ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('root')
);
        """
        expected = """
import * as React from "react";
import * as ReactDOM from "react-dom";
ReactDOM.render(
  /* @__PURE__ */ React.createElement("h1", null, "Hello, world!"),
  document.getElementById("root")
);
        """
        assert transform(jsx).strip() == expected.strip()