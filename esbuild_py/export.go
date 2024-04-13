package main

import "C"

//export transform
func transform(jsx *C.char) *C.char {
	jsxStr := C.GoString(jsx)
	result := RunTransform(jsxStr)
	return C.CString(result)
}

func main() {}
