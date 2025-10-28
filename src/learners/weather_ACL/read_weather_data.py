import os

def read_data(file_path):
    """Read the weather data from .dat file."""
    # Check if the file exists
    if not os.path.exists(file_path):
        return False

    # open the file in read mode
    with open(file_path, 'r') as file_obj:
        # read first character
        first_char = file_obj.read(1)

        if not first_char:
            return False
        else:
            return True


assert read_data.__doc__
assert read_data("data/uppsala_tm_1722-2022.dat")

