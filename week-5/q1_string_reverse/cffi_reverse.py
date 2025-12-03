from cffi import FFI
import os

ffi = FFI()

# Define the C function signature
ffi.cdef("""
    char* reverse_string_c(const char* input);
    void free_string(char* ptr);
""")

# C code for string reversal
c_code = """
#include <stdlib.h>
#include <string.h>

char* reverse_string_c(const char* input) {
    if (!input) return NULL;
    
    int len = strlen(input);
    char* result = (char*)malloc(len + 1);
    if (!result) return NULL;
    
    for (int i = 0; i < len; i++) {
        result[i] = input[len - 1 - i];
    }
    result[len] = '\\0';
    
    return result;
}

void free_string(char* ptr) {
    free(ptr);
}
"""

# Build the C extension
ffi.set_source("_cffi_reverse", c_code)

def reverse_string_cffi(s):
    """
    Reverse a string using CFFI.
    Example: "hello" -> "olleh"
    """
    # Convert Python string to C string
    c_input = s.encode('utf-8')
    
    # Call C function
    c_result = ffi.lib.reverse_string_c(c_input)
    
    if c_result == ffi.NULL:
        return ""
    
    # Convert back to Python string
    result = ffi.string(c_result).decode('utf-8')
    
    # Free the C memory
    ffi.lib.free_string(c_result)
    
    return result

if __name__ == "__main__":
    # Build the extension if run directly
    ffi.compile(tmpdir='.')