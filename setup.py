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