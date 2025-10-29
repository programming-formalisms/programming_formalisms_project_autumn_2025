class Range:
    def __init__(self, lowest, highest):
        assert lowest < highest
        self.__lowest = lowest
        self.__highest = highest

    def get_lowest(self):
        return self.__lowest
    
    def get_highest(self):
        return self.__highest
    
    def set_lowest(self, new_lowest):
        assert new_lowest < self.__highest, "The new lower bound must be lower than the current upper bound"
        self.__lowest = new_lowest

    def set_highest(self, new_highest):
        assert self.__lowest > new_highest, "The new upper bound must be higher than the current lower bound"
        self.__highest = new_highest


rangeObj = Range(3, 10)
assert rangeObj.get_lowest() == 3
assert rangeObj.get_highest() == 10
rangeObj.set_lowest(4)
rangeObj.set_highest(-1)
rangeObj.__lowest = 1
#rangeObj.__getattribute__(lowest)
#rangeObj.__setattr__
