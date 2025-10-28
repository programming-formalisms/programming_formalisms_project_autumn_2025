"A class for positive number."

class PositiveNumber:
    def __init__(self,number:int):
        assert self.is_positive(number)
        self._number = number

    def get_number(self):
        return self._number
    
    def is_positive(self, number:int)->bool:
        """Check if number is positive."""
        return number > 0
    


