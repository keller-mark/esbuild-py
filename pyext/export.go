package main

import "C"

//export verify
func verify(root *C.char) *C.char {
	rootDir := C.GoString(root)
	result := CheckSignatures(rootDir)
	return C.CString(result)
}

func main() {}
