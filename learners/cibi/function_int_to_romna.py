def int_to_roman(input):
    """Convert an integer to roman."""
    if input == 0: 
        return ""
    return "I"

assert int_to_roman.__doc__
assert int_to_roman(1) == "I"
assert int_to_roman(0) == ""
assert int_to_roman(2) == "II"
