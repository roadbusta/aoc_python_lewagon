from aoc_23.day_03 import str_to_array, num_position
from aoc_23.load_data import get_test_data
import numpy as np


test_data = get_test_data(3)
machine_array = str_to_array(test_data)
num_dict_list = num_position(machine_array)
expected_result_part_1 = 4361
# expected_result_part_2 =


def test_part_1():
    assert type(test_data) == str
    assert type(machine_array) == np.ndarray
    assert len(machine_array.shape) ==2
    assert type(num_dict_list) == list
    assert type(num_dict_list[0]) == dict
    assert len(num_dict_list[0]['4']) == 2
    # assert type(day_03.game_dictionary(test_data))== di
    # assert type(day_03.part_1(test_data)) == int
    # assert day_03.part_1(test_data) == expected_result_part_1

# def test_part_2():
#     assert type(test_data) == str
#     assert type(day_02.game_dictionary(test_data))== dict
#     assert day_02.part_2(test_data) == expected_result_part_2
