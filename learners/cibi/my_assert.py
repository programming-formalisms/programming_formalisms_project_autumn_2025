# Exercise 1
def divide_by(numerator, denominator):
    assert (denominator != 0.0)
    assert isinstance(numerator, float)
    assert isinstance(denominator, float)

    return (numerator / denominator)

# 'a = divide_by(3, 4)
# print(a)

# Exercise 2

def read_file(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content


# Exercise 3
def read_non_empty_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

read_non_empty_file('random.txt')