# Starting new exercise to see if I have understood the method properly

def is_even(number):
    """Defines if input number is even"""
    # Here I have defined is_even
    if not isinstance(number, int):
        raise TypeError("'number' must be of type int")
    
    if number % 2 == 0:
        return True
    else:
        return False

assert is_even.__doc__
assert is_even(2) == True
assert is_even(3) == False


has_thrown = False
try:
    is_even(0.13)
except TypeError:
    has_thrown = True
assert has_thrown


