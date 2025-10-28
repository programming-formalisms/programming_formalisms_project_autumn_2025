"""The script is to learn how to apply CI."""

def is_odd(number: int) -> bool:
    """Check if number is odd."""
    assert isinstance(number, int)
    return number % 2 == 0
