from cffi import FFI

ffi = FFI()

# Define the C function signature
ffi.cdef("""
    long long sum_of_squares_c(int n);
""")

# C code for sum of squares
c_code = """
long long sum_of_squares_c(int n) {
    long long result = 0;
    for (int i = 1; i <= n; i++) {
        result += (long long)i * i;
    }
    return result;
}
"""

# Build the C extension
ffi.set_source("_cffi_sum_squares", c_code)

def sum_of_squares_cffi(n):
    """
    Compute sum of squares from 1 to n (1^2 + 2^2 + ... + n^2) using CFFI.
    Args:
        n: Upper limit (inclusive)
    Returns:
        Sum of squares as integer
    """
    if n < 0:
        return 0
    
    result = ffi.lib.sum_of_squares_c(n)
    return result

if __name__ == "__main__":
    # Build the extension if run directly
    ffi.compile(tmpdir='.')