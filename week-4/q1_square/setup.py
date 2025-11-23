from setuptools import setup, Extension

ext_modules = [
    Extension('csquare', ['squaremodule.c']),
]

setup(
    name='csquare',
    version='0.1',
    ext_modules=ext_modules,
)
