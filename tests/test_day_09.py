from aoc_23.day_09 import part_1
from aoc_23.load_data import get_test_data
import numpy as np


test_data = get_test_data(9)
result = part_1(test_data)
expected_result_part_1 = 114
expected_result_part_2 = None



def test_part_1():
    assert type(result) == int
    assert part_1(test_data) == expected_result_part_1
    pass


def test_part_2():
   pass
