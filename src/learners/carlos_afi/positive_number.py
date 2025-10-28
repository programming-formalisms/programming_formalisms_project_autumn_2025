"""A class for positive number."""

class PositiveNumber:

    """A class for positive number."""

    def __init__(self,number:int):
        """Initialize."""
        assert self.is_positive(number)
        self._number = number

    def get_number(self):
        """Get the number."""
        return self._number

    def is_positive(self, number:int)->bool:
        """Check if number is positive."""
        return number > 0
