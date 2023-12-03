from aoc_23.day_03 import str_to_array
from aoc_23.load_data import get_test_data
import numpy as np


test_data = get_test_data(3)
expected_result_part_1 = 4361
# expected_result_part_2 =


def test_part_1():
    assert type(test_data) == str
    assert type(str_to_array(test_data)) == np.ndarray
    # assert type(day_03.game_dictionary(test_data))== di
    # assert type(day_03.part_1(test_data)) == int
    # assert day_03.part_1(test_data) == expected_result_part_1

# def test_part_2():
#     assert type(test_data) == str
#     assert type(day_02.game_dictionary(test_data))== dict
#     assert day_02.part_2(test_data) == expected_result_part_2
