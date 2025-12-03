import numpy as np
cimport numpy as cnp

def dot_product(cnp.ndarray[double, ndim=1] a, cnp.ndarray[double, ndim=1] b):
    """
    Compute dot product of two 1D arrays using Cython.
    Args:
        a: First 1D array
        b: Second 1D array
    Returns:
        Dot product as a float
    """
    if len(a) != len(b):
        raise ValueError("Arrays must have the same length")
    
    cdef int n = len(a)
    cdef double result = 0.0
    cdef int i
    
    for i in range(n):
        result += a[i] * b[i]
    
    return result