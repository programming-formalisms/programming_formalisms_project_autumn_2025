


def is_zero(input):
    """ Determins if the input is zero """
    return input == 0

assert is_zero.__doc__
assert is_zero(0) == True
assert is_zero(1) == False

has_thrown = False
try:
    my_function("nonsense")
except:
    has_thrown = True
assert has_thrown