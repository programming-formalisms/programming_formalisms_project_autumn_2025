#assert 1 == 2

def divide_by(numerator, denominator):
    assert(denominator != 0.0)
    assert isinstance(numerator, (float, int))
    assert isinstance(denominator, (float, int))
    return (numerator / denominator)

divide_by(4, 2)


def read_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)

    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

def read_non_empty_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)
    file = open(filename, "r")
    content = file.read()
    if len(content) == 0:
        raise ValueError("File has no content")
    file.close()
    return content