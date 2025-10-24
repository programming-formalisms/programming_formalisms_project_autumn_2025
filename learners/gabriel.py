def is_zero(n):
    """Function that return True if n is 0 and False otherwise"""
    if not isinstance(n, int):
        raise TypeError("n must be of type int")
    
    return  n == 0

assert is_zero.__doc__
assert is_zero(0) == True
assert is_zero(1) == False

has_thrown = False
try:
    is_zero({0, 1})
except TypeError:
    has_thrown = True

assert has_thrown



assert is_prime.__doc__