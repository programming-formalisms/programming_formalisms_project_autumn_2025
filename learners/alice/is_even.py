# Starting new exercise to see if I have understood the method properly

def is_even(number):
    """Defines if input number is even"""
    # Here I have defined is_even
    if number % 2 == 0:
        return True
    else:
        return False

assert is_even.__doc__
assert is_even(2) == True