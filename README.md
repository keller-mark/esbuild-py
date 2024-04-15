# esbuild-py

[![PyPI](https://img.shields.io/pypi/v/esbuild_py)](https://pypi.org/project/esbuild_py)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keller-mark/esbuild-py/blob/main/scripts/esbuild_py_demo.ipynb)

Python bindings to the [esbuild](https://github.com/evanw/esbuild) [Transform API](https://pkg.go.dev/github.com/evanw/esbuild@v0.20.2/pkg/api#hdr-Transform_API).
## Installation

```py
pip install esbuild_py
```

## Usage

```python
from esbuild_py import transform

jsx = """
import * as React from 'react'
import * as ReactDOM from 'react-dom'

ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('root')
);
"""

print(transform(jsx))
```

## API

### `transform`

Parameters:
- `jsx` (`str`) - The JSX string to be transformed.

Returns: `str` - The transformed JS as a string.


## Development

### Setup

Create conda environment

```sh
conda create -n esbuild-py python=3.11
```

- Install go v1.20.12 from https://go.dev/dl/

### Build

```sh
conda activate esbuild-py
go get github.com/keller-mark/esbuild-py
# go build -buildmode=c-shared -o _esbuild.so
```

### Develop

Build python package and install in editable mode

```sh
python setup.py bdist_wheel
python setup.py sdist
pip install -e .
```

### Publish

Increment the version in `pyproject.toml`.
The [cibuildwheel](https://github.com/pypa/cibuildwheel) GH action will build wheels for a matrix of Python versions, OS, and architectures.
Then, GH actions will publish to PyPI.

## Resources


- https://github.com/ardanlabs/python-go/tree/master/pyext
- https://pkg.go.dev/github.com/evanw/esbuild@v0.20.2/pkg/api#hdr-Transform_API
- https://github.com/evanw/esbuild/blob/main/.github/workflows/ci.yml
