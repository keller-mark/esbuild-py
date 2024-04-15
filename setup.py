from distutils.errors import CompileError
from subprocess import call
import os

from setuptools import Extension, setup, find_packages
from setuptools.command.build_ext import build_ext


class build_go_ext(build_ext):
    """Custom command to build extension from Go source files"""
    def build_extension(self, ext):
        ext_path = self.get_ext_fullpath(ext.name)
        print(ext_path)
        cmd = ['go', 'build', '-buildmode=c-shared', '-o', ext_path]
        cmd += ext.sources
        out = call(cmd)
        if out != 0:
            raise CompileError('Go build failed')
        
        wasm_ext_path = ext_path.replace('.so', '.wasm')
        print(wasm_ext_path)
        wasm_sources = [s.replace('.go', '_wasm.go') for s in ext.sources]
        my_env = os.environ.copy()
        my_env['GOOS'] = 'js'
        my_env['GOARCH'] = 'wasm'
        cmd = ['go', 'build', '-o', wasm_ext_path]
        cmd += wasm_sources
        out = call(cmd, env=my_env)
        if out != 0:
            raise CompileError('Go build failed for WASM')


setup_args = dict(
    packages = find_packages(where="src"),
    package_dir = {"": "src"},
    ext_modules = [
        Extension(
            name = '_esbuild',
            sources = ['esbuild_bindings.go'],
        )
    ],
    cmdclass = {'build_ext': build_go_ext},
)

setup(**setup_args)