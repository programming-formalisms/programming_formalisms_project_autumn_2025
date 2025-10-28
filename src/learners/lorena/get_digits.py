def get_digits(input):
    """ Gets the integer and splits into digits
    """
    # input_str = str(input).split()
    input_int = []
    for i in str(input):
        i = int(i)
        input_int.append(i)
    return input_int

assert get_digits.__doc__
#print(get_digits(12))
assert get_digits(1) == [1]
assert get_digits(12) == [1, 2]
