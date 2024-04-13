from distutils.errors import CompileError
from subprocess import call

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

ext = Extension(
    name                = '_esbuild',          # 'mypackage.mymodule'
    sources             = ['esbuild_bindings.go'],            # list of source files (to compile)
)

setup_args = dict(
    packages        = find_packages(where="src"),       # list 
    package_dir     = {"": "src"},                      # mapping
    ext_modules     = [ext],     
    cmdclass={'build_ext': build_go_ext},                       # list
)

setup(**setup_args)