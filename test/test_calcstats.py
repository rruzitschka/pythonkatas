from src.calcstats import *

# tests for the kata
# Your task is to process a sequence of integer numbers to determine the following statistics:
#
# minimum value
# maximum value
# number of elements in the sequence
# average value

val_set = (5, 2, 3, 6, 10)

def test_min_value():
    assert(minimum_val(val_set) == 2)

def test_max_value():
    assert(maximum_val(val_set) == 10)


def test_num_set():
    assert(num_elements(val_set)) == 5

def test_average():
    assert(average_val(val_set) == 5.2)



