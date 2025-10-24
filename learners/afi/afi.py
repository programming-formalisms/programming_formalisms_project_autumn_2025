def is_even(input):
	"""
	is the number even (True) or odd (False)
	raise error if not a number
	"""
	if (input%2)==0:
		return True
	else:
		return False



assert is_even.__doc__
assert is_even(2)
assert not is_even(1)


