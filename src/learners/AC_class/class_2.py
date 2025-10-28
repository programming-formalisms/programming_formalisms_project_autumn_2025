class Range:
    def __init__(self, value_low, value_high):
        assert value_high > value_low
        self._value_low = value_low
        self._value_high = value_high
    
    def get_lowest(self):
        return self._value_low
    
    def get_highest(self):
        return self._value_high


x = Range(3, 10)

assert x.get_lowest() == 3
assert x.get_highest() == 10
Range(100, 10) # Must raise an exception