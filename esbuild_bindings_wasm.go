package main

import (
	"github.com/evanw/esbuild/pkg/api"
)

func transform(jsxStr string) string {
	result := api.Transform(jsxStr, api.TransformOptions{
        Loader: api.LoaderJSX,
    })
	resultStr := string(result.Code[:])
	return resultStr
}

func main() {}
