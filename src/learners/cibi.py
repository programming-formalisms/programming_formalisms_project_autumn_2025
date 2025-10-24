
def is_zero(input):
    """This is a function that checks if the input is equal to zero
    1. Returns True if input is zero
    2. Returns False if input is non-zero
    3. Gives error if input is not a number
    """
    assert isinstance(input, (int,float))
    if input == 0:
        return True
    else:
        return False

assert is_zero.__doc__