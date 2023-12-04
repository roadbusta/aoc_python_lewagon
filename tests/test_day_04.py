from aoc_23.day_04 import _card_dict, _positive_int, _points_dict, part_1
from aoc_23.load_data import get_test_data
import numpy as np


test_data = get_test_data(4)
expected_result_part_1 = 13
# expected_result_part_2 =


def test_part_1():
    assert type(test_data) == str
    assert _positive_int([0,1,2]) == True
    assert _positive_int([-1,1,2]) == False
    assert _positive_int(['a', 1,2 ]) == False

    card_dict = _card_dict(test_data)

    assert type(card_dict) == dict # Dictionary output
    assert len(card_dict['1'][0]) != 0 # Non-empty list
    assert len(card_dict['1'][1]) != 0 # Non-empty list
    assert _positive_int(card_dict['1'][0]) == True # Positive integers including zero
    assert _positive_int(card_dict['1'][1]) == True # Positive integers including zero
    assert type(_points_dict(card_dict) == dict) # Check data type
    assert _points_dict(card_dict)['1'] >=0 # Check positive integer
    assert type(_points_dict(card_dict)['1']) == int # Check for integer
    assert type(part_1(test_data)) == int # Check data type
    assert part_1(test_data) >= 0
    assert part_1(test_data) == expected_result_part_1



    # assert type(day_03.game_dictionary(test_data))== di
    # assert type(day_03.part_1(test_data)) == int
    # assert day_03.part_1(test_data) == expected_result_part_1

# def test_part_2():
#     assert type(test_data) == str
#     assert type(day_02.game_dictionary(test_data))== dict
#     assert day_02.part_2(test_data) == expected_result_part_2
