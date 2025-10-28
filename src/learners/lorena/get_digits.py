def get_digits(input_str):
    """Get the integer and split into digits."""
    # input_str = str(input_str).split()
    input_int = []
    for i in str(input_str):
        i = int(i)
        input_int.append(i)
    return input_int

assert get_digits.__doc__
#print(get_digits(12))
assert get_digits(1) == [1]
assert get_digits(12) == [1, 2]
