from aoc_23.day_04 import _card_dict, _positive_int, _points_dict, part_1, _win_count_dict, part_2
from aoc_23.load_data import get_test_data
import numpy as np


test_data = get_test_data(4)
card_dict = _card_dict(test_data)
points_dict = _points_dict(card_dict)
win_count_dict = _win_count_dict(card_dict)
expected_result_part_1 = 13
expected_result_part_2 = 30


def check_test_data():
    assert type(test_data) == str
    pass


def check_positive_int():
    assert _positive_int([0,1,2]) == True
    assert _positive_int([-1,1,2]) == False
    assert _positive_int(['a', 1,2 ]) == False
    pass

def check_card_dict():
    assert type(card_dict) == dict # Dictionary output
    assert len(card_dict['1'][0]) != 0 # Non-empty list
    assert len(card_dict['1'][1]) != 0 # Non-empty list
    assert _positive_int(card_dict['1'][0]) == True # Positive integers including zero
    assert _positive_int(card_dict['1'][1]) == True # Positive integers including zero
    assert type(_points_dict(card_dict) == dict) # Check data type
    pass

def check_points_dict():
    assert points_dict['1'] >=0 # Check positive integer
    assert type(points_dict['1']) == int # Check for integer
    pass

def test_part_1():
    assert type(part_1(test_data)) == int # Check data type
    assert part_1(test_data) >= 0
    assert part_1(test_data) == expected_result_part_1
    pass


def test_part_2():

    assert type(win_count_dict) == dict
    assert len(win_count_dict['1']) == 2
    assert type(win_count_dict['1']['points']) == int
    assert win_count_dict['1']['points'] >= 0
    assert type(win_count_dict['1']['copies']) == int
    assert win_count_dict['1']['copies'] >= 0
    assert part_2(test_data) == expected_result_part_2
    pass
