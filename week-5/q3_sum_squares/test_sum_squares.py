#!/usr/bin/env python3
"""
Test script for sum of squares implementations
"""

def test_cython():
    print("Testing Cython implementation:")
    try:
        import cython_sum_squares
        
        result1 = cython_sum_squares.sum_of_squares(5)
        print(f"  sum_of_squares(5) = {result1}")
        print(f"  Expected: {sum(i*i for i in range(1, 6))} (1^2 + 2^2 + 3^2 + 4^2 + 5^2)")
        
        result2 = cython_sum_squares.sum_of_squares(10)
        print(f"  sum_of_squares(10) = {result2}")
        print(f"  Expected: {sum(i*i for i in range(1, 11))}")
        
        result3 = cython_sum_squares.sum_of_squares(100)
        print(f"  sum_of_squares(100) = {result3}")
        print(f"  Expected: {sum(i*i for i in range(1, 101))}")
        
    except ImportError:
        print("  Cython module not built. Run: python setup.py build_ext --inplace")

def test_cffi():
    print("\nTesting CFFI implementation:")
    try:
        from cffi_sum_squares import sum_of_squares_cffi
        
        result1 = sum_of_squares_cffi(5)
        print(f"  sum_of_squares_cffi(5) = {result1}")
        print(f"  Expected: {sum(i*i for i in range(1, 6))} (1^2 + 2^2 + 3^2 + 4^2 + 5^2)")
        
        result2 = sum_of_squares_cffi(10)
        print(f"  sum_of_squares_cffi(10) = {result2}")
        print(f"  Expected: {sum(i*i for i in range(1, 11))}")
        
        result3 = sum_of_squares_cffi(100)
        print(f"  sum_of_squares_cffi(100) = {result3}")
        print(f"  Expected: {sum(i*i for i in range(1, 101))}")
        
    except ImportError:
        print("  CFFI module not built. Run the cffi_sum_squares.py file first to compile.")

if __name__ == "__main__":
    test_cython()
    test_cffi()