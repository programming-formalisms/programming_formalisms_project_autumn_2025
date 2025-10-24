
# def is_zero(input):
#     """This is a function that checks if the input is equal to zero
#     1. Returns True if input is zero
#     2. Returns False if input is non-zero
#     3. Gives error if input is not a number
#     """
#     assert isinstance(input, (int,float))
#     if input == 0:
#         return True
#     else:
#         return False

# assert is_zero.__doc__


# # Testing
# # Test 1
# assert is_zero(1)
# assert is_zero(-1)
# assert is_zero(0)
# assert is_zero(1.3)

# # Test 2
# assert is_zero('a')

# Exercise 2 : is_even()

def is_even(input):
    """This function verifies if the given input is even
    1. Return True if input is even
    2. Return False if input is not even
    3. Gives an error when the inputis not a number
    """

    if not isinstance(input, int):
        raise TypeError("The input must be an integer!")

    if (input % 2 == 0):
        return True
    return False


# Testing using Assert
assert is_even(2)
assert not is_even(3)
assert not is_even(-1)

has_thrown = False
try:
    is_even(1.0)
except TypeError:
    has_thrown = True
assert has_thrown
