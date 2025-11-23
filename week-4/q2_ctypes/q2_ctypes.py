import ctypes
import os

here = os.path.dirname(__file__)
libpath = os.path.join(here, 'libstringlib.so')
lib = ctypes.CDLL(libpath)

lib.reverse_string.restype = ctypes.c_void_p
lib.reverse_string.argtypes = [ctypes.c_char_p]
lib.free_string.restype = None
lib.free_string.argtypes = [ctypes.c_void_p]

def reverse_and_print(s: str):
    b = s.encode('utf-8')
    ptr = lib.reverse_string(b)
    if not ptr:
        print('reverse_string returned NULL')
        return
    py_bytes = ctypes.string_at(ptr)
    print('Original:', s)
    print('Reversed:', py_bytes.decode('utf-8'))
    lib.free_string(ptr)

if __name__ == '__main__':
    reverse_and_print('Hello from C')
    reverse_and_print('abcde')
