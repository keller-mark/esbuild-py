package main

import "github.com/evanw/esbuild/pkg/api"

func RunTransform(jsx string) string {
	result := api.Transform(jsx, api.TransformOptions{
        Loader: api.LoaderJSX,
    })
	resultString := string(result.Code[:])
	return resultString
}
