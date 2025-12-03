#!/usr/bin/env python3
"""
Test script for dot product implementations
"""
import numpy as np

def test_cython():
    print("Testing Cython implementation:")
    try:
        import cython_dot
        
        a = np.array([1.0, 2.0, 3.0])
        b = np.array([4.0, 5.0, 6.0])
        result = cython_dot.dot_product(a, b)
        print(f"  dot_product([1, 2, 3], [4, 5, 6]) = {result}")
        print(f"  Expected: {np.dot(a, b)}")
        
        a2 = np.array([1.0, 0.0, -1.0])
        b2 = np.array([2.0, 3.0, 4.0])
        result2 = cython_dot.dot_product(a2, b2)
        print(f"  dot_product([1, 0, -1], [2, 3, 4]) = {result2}")
        print(f"  Expected: {np.dot(a2, b2)}")
        
    except ImportError:
        print("  Cython module not built. Run: python setup.py build_ext --inplace")

def test_cffi():
    print("\nTesting CFFI implementation:")
    try:
        from cffi_dot import dot_product_cffi
        
        a = [1.0, 2.0, 3.0]
        b = [4.0, 5.0, 6.0]
        result = dot_product_cffi(a, b)
        print(f"  dot_product_cffi([1, 2, 3], [4, 5, 6]) = {result}")
        print(f"  Expected: {np.dot(a, b)}")
        
        a2 = [1.0, 0.0, -1.0]
        b2 = [2.0, 3.0, 4.0]
        result2 = dot_product_cffi(a2, b2)
        print(f"  dot_product_cffi([1, 0, -1], [2, 3, 4]) = {result2}")
        print(f"  Expected: {np.dot(a2, b2)}")
        
    except ImportError:
        print("  CFFI module not built. Run the cffi_dot.py file first to compile.")

if __name__ == "__main__":
    test_cython()
    test_cffi()