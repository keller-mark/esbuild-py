from distutils.errors import CompileError
from subprocess import call

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class build_go_ext(build_ext):
    """Custom command to build extension from Go source files"""
    def build_extension(self, ext):
        ext_path = self.get_ext_fullpath(ext.name)
        cmd = ['go', 'build', '-buildmode=c-shared', '-o', ext_path]
        cmd += ext.sources
        out = call(cmd)
        if out != 0:
            raise CompileError('Go build failed')

setup(
    name='esbuild_py',
    version='0.1.0',
    py_modules=['esbuild'],
    ext_modules=[
        Extension('_esbuild', ['esbuild_bindings.go'])
    ],
    cmdclass={'build_ext': build_go_ext},
    zip_safe=False,
)