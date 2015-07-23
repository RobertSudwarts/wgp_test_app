

from project import midpoint, median_sort
from nose.tools import *

MIN_AGE = 25
MAX_AGE = 30


def test_midpoint():
    assert midpoint(MIN_AGE, MAX_AGE) == 27


def test_median_sort():
    # we know 27 to be midpoint between
    # 25 and 30, therefore we expect the first
    # four records to be 'age' == 27
    data = [
        {'id': 'x', 'age': 30},
        {'id': 'x', 'age': 29},
        {'id': 'x', 'age': 28},
        {'id': 'x', 'age': 27},
        {'id': 'x', 'age': 27},
        {'id': 'x', 'age': 27},
        {'id': 'x', 'age': 27},
        {'id': 'x', 'age': 26},
        {'id': 'x', 'age': 25},
        {'id': 'x', 'age': 24},
     ]

    expected = [
        {'id': 'x', 'age': 27},
        {'id': 'x', 'age': 27},
        {'id': 'x', 'age': 27},
        {'id': 'x', 'age': 27},
     ]

    result = median_sort(data, MIN_AGE, MAX_AGE)

    assert_list_equal(result[:4], expected)

    # we also know that the 5th item in the list will be 26
    eq_(result[5]['age'], 26)
