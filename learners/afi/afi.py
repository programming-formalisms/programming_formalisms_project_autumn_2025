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


def is_probability(input):
	"""
	is the number in [0.0, 1.0]
	"""
	if not isinstance(input, float):
		msg = "'number' must be a floating point number. "
		raise TypeError(
            msg, "Actual type of 'number': ", type(input),)
	
	if 0.0 <= input and input <= 1.0:
		return True
	else:
		return False

assert is_probability.__doc__
assert is_probability(0.0)
assert is_probability(0.5)
assert not is_probability(1.1)
has_thrown = False
try:
    is_odd(0.0)
except TypeError:
    has_thrown = True
assert has_thrown


def is_prime(input):
	"""
	is the number a prime number (only devidable by 1 and itself and bigger than 1)
	True if it is prime number
	False if it is note
	error if not a number
	"""
	if not isinstance(input, int):
		raise TypeError("'input' must be of type int")
	if input > 1:
		is_prime = True 
		for i in range(2, input-1):
			if input % i == 0:
				is_prime = False
		return is_prime
	else:
		return False


assert is_prime.__doc__
assert is_prime(2)
assert not is_prime(1)
assert not is_prime(4)

has_thrown = False
try:
    is_odd(0.0)
except TypeError:
    has_thrown = True
assert has_thrown
