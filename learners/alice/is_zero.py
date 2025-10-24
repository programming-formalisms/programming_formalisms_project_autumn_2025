def is_zero(var):
    if not isinstance(var, int):
        raise TypeError("'x' must be of type int")
    if var == 0:
        return True
    else:
        return False