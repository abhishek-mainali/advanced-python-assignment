# Difference: `ctypes` vs Extension Modules

Summary:

ctypes allows loading of already existing shared libraries at runtime, and invoking C functions through a pure-python interface. It is excellent with rapid interoperability as well as prototyping and when you already possess an existing compiled.so/.dll/.dylib.
The extension modules are Python modules that are code written on top of the Python/C API (or on top of C++ macros, such as pybind11). These are bundled into modules which are imported by Python. They are faster, have a closer integration with Python types, and are more flexible (custom types, exceptions, lifecycle control).

Key differences:

Build vs runtime loading: The extension modules are written in the form of Python modules and loaded as such; ctypes simply loads any shared libraries it desires, without having them be Python modules.
Type safety Extension modules may work with Python objects directly, may represent Python types, can marshal Python types to C types and can marry should request you to specify the argtypes/restype in Python.
Performance: Extension modules typically have lower overhead of being called a large number of times or other small business operations on Python objects since they invoke Python C API functions. ctypes implies overhead on marshalling the call.
Safety and error management Extension modules are able to raise Python errors directly; using ctypes you must use your own Python level exception translator to translate C errors into Python errors.
Laws of convenience: ctypes has flexibility: you will be able to develop much more quickly when you simply need to invoke a few C functions in an existing library. To write an extension module (or with pybind11) generally needs further set up however the Python API becomes more idiomatic and maintenance friendly.

When to choose:
mcall Ctypes Use ctypes when making quick experiments or when calling an existing shared library which is stable.
Extend with Python extension modules (C or C++/pybind11) with high performance or custom Python types and heavy integration with the Python internals.