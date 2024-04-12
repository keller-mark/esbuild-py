# esbuild-py

```sh
conda create -n esbuild-py python=3.11
conda activate esbuild-py
```

```sh
cd pyext
go get github.com/keller-mark/esbuild-py/pyext
go build -buildmode=c-shared -o _checksig.so
python
```


```py
import ctypes
so = ctypes.cdll.LoadLibrary('./_checksig.so')
verify = so.verify
verify.argtypes = [ctypes.c_char_p]
verify.restype = ctypes.c_void_p
free = so.free
free.argtypes = [ctypes.c_void_p]

verify_arg = """
import * as React from 'react'
import * as ReactDOM from 'react-dom'

ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('root')
);
"""

ptr = verify(verify_arg.encode('utf-8'))
out = ctypes.string_at(ptr)
free(ptr)
print(out.decode('utf-8'))
```

## Resources

- Install go v1.20.12 from https://go.dev/dl/


- https://github.com/ardanlabs/python-go/tree/master/pyext
- https://pkg.go.dev/github.com/evanw/esbuild@v0.20.2/pkg/api#hdr-Transform_API
- https://github.com/evanw/esbuild/blob/main/.github/workflows/ci.yml