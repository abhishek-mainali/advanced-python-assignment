def sum_of_squares(int n):
    """
    Compute sum of squares from 1 to n (1^2 + 2^2 + ... + n^2) using Cython.
    Args:
        n: Upper limit (inclusive)
    Returns:
        Sum of squares as integer
    """
    cdef long long result = 0
    cdef int i
    
    for i in range(1, n + 1):
        result += i * i
    
    return result