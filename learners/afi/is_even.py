def is_even(input):
    """
    function to determine if soemthing is even:
    even numbers to be True
    uneven numbers to be False
    assert error if not a number (Integer)
    """
    if not isinstance(input, int): 
        raise TypeError('not an int')
    
    return (input%2)==0

assert is_even.__doc__
assert is_even(2)
assert not is_even(1)

has_thrown = False
try:
    is_even(0.0)
except TypeError:
    has_thrown = True
assert has_thrown

