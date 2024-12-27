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

//export build
func build(input, output *C.char) int {
	input_str := C.GoString(input)
	output_str := C.GoString(output)

	result := api.Build(api.BuildOptions{
		EntryPoints: []string{input_str},
		Outfile:     output_str,
		Bundle:      true,
		Write:       true,
		LogLevel:    api.LogLevelError,
	})

	if len(result.Errors) > 0 {
		return 1
	}
	return 0
}

func main() {}
