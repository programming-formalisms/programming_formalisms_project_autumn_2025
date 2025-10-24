def is_even(input):
    """
    function to determine if soemthing is even:
    even numbers to be True
    uneven numbers to be False
    assert error if not a number (Integer)
    """
    if (input%2)==0:
        return True
    else:  
        return False

assert is_even.__doc__
assert is_even(2)
assert not is_even(1)

