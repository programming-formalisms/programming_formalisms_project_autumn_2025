
# exercise 1
def is_zero(number:float) -> bool:
    if not isinstance(number, (int, float)):
        raise TypeError(f"{number} is not a number")
    return number == 0


# excercise 2
def is_even(number:int) -> bool:
    assert isinstance(number, int), f"""{number} is not an integer number"""
    return number % 2 == 0


# exercise 3

def is_odd(number:int) -> bool:
    assert isinstance(number, int), f"""{number} is not an integer number"""
    return number % 2 != 0



# exercise 4
def is_probability(value:float) -> bool:
    assert isinstance(value, (int, float)), f"""{value} is not a number"""
    return 0.0 <= value <= 1.0


# exercise 5

def is_prime(number:int) -> bool:
    assert isinstance(number, int), f"""{number} is not an integer number"""
    out_bool = True
    if number <= 1:
        out_bool = False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                out_bool = False
                break
    return out_bool


