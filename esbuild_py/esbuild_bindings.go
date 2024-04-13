package main

import (
	"C"

	"github.com/evanw/esbuild/pkg/api"
)

//export transform
func transform(jsx *C.char) *C.char {
	jsxStr := C.GoString(jsx)
	result := api.Transform(jsxStr, api.TransformOptions{
        Loader: api.LoaderJSX,
    })
	resultStr := string(result.Code[:])
	return C.CString(resultStr)
}

func main() {}
