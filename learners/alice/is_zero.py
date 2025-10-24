def is_zero(var):
    "This is the documentation I had not added before"
    if not isinstance(var, int):
        raise TypeError("'x' must be of type int")
    if var == 0:
        return True
    else:
        return False
    

assert is_zero.__doc__