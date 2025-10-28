import os
def read_data(file_path):
    """Read the weather data from .dat file."""
    # Check if the file exists
    return os.path.exists(file_path)

assert read_data.__doc__
assert read_data('data/uppsala_tm_1722-2022.dat')