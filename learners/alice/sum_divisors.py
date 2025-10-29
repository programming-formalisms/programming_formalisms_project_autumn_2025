def sum_divisors(x):
    """Returns the Sum of input divisors"""
    summation = 0
    if x==1 or isinstance(x, float):
            return 0
    for divisor in range(1, x):
        if x%divisor == 0:
            summation += divisor

    return summation


assert sum_divisors.__doc__ 
assert sum_divisors(1) == 0
assert sum_divisors(4) == 3
assert sum_divisors(0) == 0
assert sum_divisors(-1) == 0
assert sum_divisors(1.5) == 0
has_thrown = False
try:
    sum_divisors("test")
except:
    has_thrown = True

assert has_thrown == False