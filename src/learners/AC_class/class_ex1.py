# Exercise 1 : Class

class PositiveNumber:
    def __init__(self, number):
        assert number > 0
        self._number = number
    
    def get_value(self):
        return self._number


x = PositiveNumber(3)
assert x.get_value() == 3
PositiveNumber(-1) # Must raise an exception