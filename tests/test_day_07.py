from aoc_23.day_07 import _hand, _hand_scorer, _hand_parser, _game_dict, part_1
from aoc_23.load_data import get_test_data
import numpy as np


test_data = get_test_data(7)

expected_result_part_1 = 6440
expected_result_part_2 = None


def test_part_1():
    assert type(test_data) == str
    assert type(_game_dict(test_data)) == dict
    assert len(_game_dict(test_data)) == 5

    assert _hand('23456') == 0
    assert _hand('22345') == 1
    assert _hand('22334') == 2
    assert _hand('22234') == 3
    assert _hand('22233') == 4
    assert _hand('22223') == 5
    assert _hand('22222') == 6

    assert _hand_parser('TJQKA') == [10,11,12,13,14]
    assert _hand_parser('12345') == [1,2,3,4,5]

    assert _hand_scorer([10,11,12,13,14],0) == 60
    assert _hand_scorer([2,2,3,4,5,],1) == 252
    assert _hand_scorer([2,2,3,3,4],2) == 1804
    assert _hand_scorer([2,2,2,3,4],3) == 10807
    assert _hand_scorer([2,2,2,3,3],4) == 84000
    assert _hand_scorer([2,2,2,2,3],5) == 480003
    assert _hand_scorer([2,2,2,2,2],6) == 4000000

    assert part_1(test_data) == expected_result_part_1
    pass


def test_part_2():
   pass
