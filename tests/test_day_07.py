from aoc_23.day_07 import _hand, _hand_scorer
from aoc_23.load_data import get_test_data
import numpy as np


test_data = get_test_data(7)

expected_result_part_1 = None
expected_result_part_2 = None


def test_part_1():
    assert type(test_data) == str
    assert _hand('23456') == 0
    assert _hand('22345') == 1
    assert _hand('22334') == 2
    assert _hand('22234') == 3
    assert _hand('22233') == 4
    assert _hand('22223') == 5
    assert _hand('22222') == 6

    # assert _hand_scorer([10,11,12,13,14]) == 60
    # assert _hand_scorer([2,2,3,4,5]) == 252
    # assert _hand_scorer([2,2,3,3,4]) == 1804
    # assert _hand_scorer([2,2,2,3,4]) == 10807
    # assert _hand_scorer([2,2,2,3,3]) == 84000
    # assert _hand_scorer([2,2,2,2,3]) == 480003

    pass


def test_part_2():
   pass
