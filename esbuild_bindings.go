package main

/*
#include <stdlib.h>
*/
import "C"
import "unsafe"
import "github.com/evanw/esbuild/pkg/api"

//export transform
func transform(jsx *C.char) *C.char {
	jsxStr := C.GoString(jsx)
	result := api.Transform(jsxStr, api.TransformOptions{
        Loader: api.LoaderJSX,
    })
	resultStr := string(result.Code[:])
	return C.CString(resultStr)
}

//export free
func free(ptr *C.char) {
	C.free(unsafe.Pointer(ptr))
}

func main() {}
