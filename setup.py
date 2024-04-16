from distutils.errors import CompileError
from subprocess import call

from setuptools import Extension, setup, find_packages
from setuptools.command.build_ext import build_ext
import os


class build_go_ext(build_ext):
    """Custom command to build extension from Go source files"""
    def build_extension(self, ext):
        ext_path = self.get_ext_fullpath(ext.name)
        print(ext_path)
        
        if ext_path.endswith('emscripten.so'):
            cmd = ['go', 'build', '-o', ext_path]
            cmd += ['esbuild_bindings_wasm.go']

            my_env = os.environ.copy()
            my_env['GOOS'] = 'wasip1'
            my_env['GOARCH'] = 'wasm'
            out = call(cmd, env=my_env)
        else:  
            cmd = ['go', 'build', '-buildmode=c-shared', '-o', ext_path]
            cmd += ['esbuild_bindings.go']
            out = call(cmd)
        if out != 0:
            raise CompileError('Go build failed')

setup_args = dict(
    packages = find_packages(where="src"),
    package_dir = {"": "src"},
    ext_modules = [
        Extension(
            name = '_esbuild',
            sources = ['esbuild_bindings.go', 'esbuild_bindings_wasm.go'],
        )
    ],
    cmdclass = {'build_ext': build_go_ext},
)

setup(**setup_args)