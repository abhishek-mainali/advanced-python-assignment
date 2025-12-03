#!/usr/bin/env python3
"""
Test script for string reversal implementations
"""

def test_cython():
    print("Testing Cython implementation:")
    try:
        import cython_reverse
        result = cython_reverse.reverse_string("hello")
        print(f"  reverse_string('hello') = '{result}'")
        
        result2 = cython_reverse.reverse_string("Python")
        print(f"  reverse_string('Python') = '{result2}'")
    except ImportError:
        print("  Cython module not built. Run: python setup.py build_ext --inplace")

def test_cffi():
    print("\nTesting CFFI implementation:")
    try:
        from cffi_reverse import reverse_string_cffi, ffi
        result = reverse_string_cffi("hello")
        print(f"  reverse_string_cffi('hello') = '{result}'")
        
        result2 = reverse_string_cffi("Python")
        print(f"  reverse_string_cffi('Python') = '{result2}'")
    except ImportError:
        print("  CFFI module not built. Run the cffi_reverse.py file first to compile.")

if __name__ == "__main__":
    test_cython()
    test_cffi()