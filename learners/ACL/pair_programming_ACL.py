def get_digits(input):
    """Gets the integer and splits into digits
    """
    input_str = str(input).split()
    
    return input_str

assert get_digits.__doc__
print(get_digits(1))
#assert get_digits(1) == [1]
#assert get_digits(12) == [1,2]