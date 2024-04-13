# esbuild-py

:warning: Work in progress

## Setup

Create conda environment

```sh
conda create -n esbuild-py python=3.11
```

## Build

```sh
conda activate esbuild-py
cd esbuild_py
go get github.com/keller-mark/esbuild-py
# go build -buildmode=c-shared -o _esbuild.so
```

## Develop

```sh
pip install -e ./esbuild_py
python
```

```python
from esbuild_py.esbuild import transform
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

## Build python package

```sh
cd esbuild_py
python setup.py bdist_wheel
python setup.py sdist
ls dist
```

## Resources

- Install go v1.20.12 from https://go.dev/dl/


- https://github.com/ardanlabs/python-go/tree/master/pyext
- https://pkg.go.dev/github.com/evanw/esbuild@v0.20.2/pkg/api#hdr-Transform_API
- https://github.com/evanw/esbuild/blob/main/.github/workflows/ci.yml