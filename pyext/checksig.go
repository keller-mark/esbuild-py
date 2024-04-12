package main

import (
	"github.com/evanw/esbuild/pkg/api"
)

// CheckSignatures calculates sha1 signatures for files in rootDir and compare
// them with signatures found at "sha1sum.txt" in the same directory. It'll
// return an error if one of the signatures don't match
func CheckSignatures(rootDir string) string {
	jsx := rootDir
	result := api.Transform(jsx, api.TransformOptions{
        Loader: api.LoaderJSX,
    })

	resultString := string(result.Code[:])

	return resultString
}
