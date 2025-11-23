from setuptools import setup, Extension

ext_modules = [
    Extension('intarray', ['intarray.c']),
]

setup(
    name='intarray',
    version='0.1',
    ext_modules=ext_modules,
)
