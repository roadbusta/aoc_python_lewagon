from aoc_23.day_08 import _parse_data
from aoc_23.load_data import get_test_data
import numpy as np


test_data = get_test_data(8)
expected_result_part_1 = None
expected_result_part_2 = None


def test_part_1():
    assert type(test_data) == str
    assert type(_parse_data(test_data)) == dict
    assert len(_parse_data(test_data)) == 2
    assert type(_parse_data(test_data)['network']['AAA'])== tuple

    pass


def test_part_2():
   pass
