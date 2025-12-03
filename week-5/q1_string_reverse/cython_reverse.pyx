def reverse_string(str s):
    """
    Reverse a string using Cython.
    Example: "hello" -> "olleh"
    """
    cdef int length = len(s)
    cdef str result = ""
    cdef int i
    
    for i in range(length - 1, -1, -1):
        result += s[i]
    
    return result