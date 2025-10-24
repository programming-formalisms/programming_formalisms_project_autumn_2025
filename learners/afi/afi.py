def is_even(input):
	"""
	is the number even (True) or odd (False)
	raise error if not a number
	"""
	if not isinstance(input, int):
		raise TypeError("'input' must be of type int")
	
	if (input%2)==0:
		return True
	else:
		return False



assert is_even.__doc__
assert is_even(2)
assert not is_even(1)

has_thrown = False
try:
    is_even(0.0)
except TypeError:
    has_thrown = True
assert has_thrown





def is_odd(input):
	"""
	is the number even (True) or odd (False)
	raise error if not a number
	"""
	if not isinstance(input, int):
		raise TypeError("'input' must be of type int")
	
	if (input%2)==0:
		return False
	else:
		return True



assert is_odd.__doc__
assert not is_odd(2)
assert is_odd(1)

has_thrown = False
try:
    is_odd(0.0)
except TypeError:
    has_thrown = True
assert has_thrown


