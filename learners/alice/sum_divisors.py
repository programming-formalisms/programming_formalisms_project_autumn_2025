def sum_divisors(x):
    """Returns the Sum of input divisors"""
    summation = 0
    if x==1:
            return 1
    for divisor in range(1, x):
        if x%divisor == 0:
            summation += divisor

    return summation


assert sum_divisors.__doc__ 
assert sum_divisors(1) == 1
assert sum_divisors(4) == 3
assert sum_divisors(0) == 0