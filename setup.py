# Magic from https://stackoverflow.com/a/34830639

from setuptools import find_packages
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext as build_ext_orig


class build_ext(build_ext_orig):

    def build_extension(self, ext):
        self._ctypes = isinstance(ext, CTypes)
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)

    def get_ext_filename(self, ext_name):
        if self._ctypes:
            return ext_name + '.so'
        return super().get_ext_filename(ext_name)


class CTypes(Extension):
    pass


files = [
    'cpp/main.cpp', 'cpp/vector.cpp',
]

setup(
    name='mc',
    version='1.0',
    py_modules=['mc.wrapper', 'mc.vector'],
    ext_modules=[
        CTypes(
            'ct',
            sources=files,
            include_dirs=['cpp']
        ),
        Extension(
            'ext',
            sources=files,
            include_dirs=['cpp']
        )
    ],
    cmdclass={'build_ext': build_ext},
    packages=find_packages()
)
