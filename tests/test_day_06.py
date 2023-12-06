from aoc_23.day_06 import _generate_lists, _positive_int
from aoc_23.load_data import get_test_data
import numpy as np


test_data = get_test_data(6)
race_data = _generate_lists(test_data)
expected_result_part_1 = 288
expected_result_part_2 = None


def test_part_1():
    assert type(test_data) == str

    assert type(race_data) == dict
    assert type(race_data['time']) == list
    assert _positive_int(race_data['time']) == True
    assert type(race_data['distance']) == list
    assert _positive_int(race_data['distance'])== True

    pass


def test_part_2():
   pass
