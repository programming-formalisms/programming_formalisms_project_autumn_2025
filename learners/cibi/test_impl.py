def get_test_prime():
    return 15485863

def get_t_is_prime_1_impl():
    is_prime_1(get_test_prime())

def get_t_is_prime_2_impl():
    is_prime_2(get_test_prime())

def get_t_is_prime_1():
    import timeit
    return timeit.timeit(get_t_is_prime_1_impl, number = 1)

def get_t_is_prime_2():
    import timeit
    return timeit.timeit(get_t_is_prime_2_impl, number = 1)


import cProfile
cProfile.run('')