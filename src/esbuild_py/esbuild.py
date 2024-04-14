import ctypes
from distutils.sysconfig import get_config_var
from pathlib import Path
import os
import site

# Get path to shared library (.so file)
# References:
# - https://github.com/ardanlabs/python-go/blob/db361abf/pyext/checksig.py#L7
# - https://github.com/jopohl/urh/blob/8886970/src/urh/util/util.py#L93
# - https://github.com/dmlc/xgboost/blob/882f413/python-package/xgboost/libpath.py#L14
# - https://stackoverflow.com/a/77824551
def get_lib_path():
    ext_suffix = get_config_var('EXT_SUFFIX')
    so_filename = ('_esbuild' + ext_suffix)

    dirs_to_try = [
        # For running in editable mode
        str(Path(__file__).absolute().parent.parent),
    ] + site.getsitepackages()
    for d in dirs_to_try:
        so_path = os.path.join(d, so_filename)
        if os.path.exists(so_path):
            return so_path

# Load functions from shared library and set their signatures
# References:
# - https://github.com/ardanlabs/python-go/blob/db361ab/pyext/checksig.py#L12
so_filepath = get_lib_path()
so = ctypes.cdll.LoadLibrary(so_filepath)
transform_binding = so.transform
transform_binding.argtypes = [ctypes.c_char_p]
transform_binding.restype = ctypes.c_void_p
free = so.free
free.argtypes = [ctypes.c_void_p]

# Wrap the bound go function.
def transform(jsx):
    res = transform_binding(jsx.encode('utf-8'))
    if res is not None:
        msg = ctypes.string_at(res).decode('utf-8')
        free(res)
        return msg

