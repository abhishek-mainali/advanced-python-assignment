from cffi import FFI
import numpy as np

ffi = FFI()

# Define the C function signature
ffi.cdef("""
    double dot_product_c(double* a, double* b, int n);
""")

# C code for dot product
c_code = """
double dot_product_c(double* a, double* b, int n) {
    double result = 0.0;
    for (int i = 0; i < n; i++) {
        result += a[i] * b[i];
    }
    return result;
}
"""

# Build the C extension
ffi.set_source("_cffi_dot", c_code)

def dot_product_cffi(a, b):
    """
    Compute dot product of two 1D arrays using CFFI.
    Args:
        a: First 1D array (list or numpy array)
        b: Second 1D array (list or numpy array)
    Returns:
        Dot product as a float
    """
    # Convert to numpy arrays if needed
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    
    if len(a) != len(b):
        raise ValueError("Arrays must have the same length")
    
    n = len(a)
    
    # Get pointers to the data
    a_ptr = ffi.cast("double*", a.ctypes.data)
    b_ptr = ffi.cast("double*", b.ctypes.data)
    
    # Call C function
    result = ffi.lib.dot_product_c(a_ptr, b_ptr, n)
    
    return result

if __name__ == "__main__":
    # Build the extension if run directly
    ffi.compile(tmpdir='.')