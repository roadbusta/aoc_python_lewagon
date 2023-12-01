from aoc_23 import day_01
from aoc_23.load_data import get_test_data


test_data = get_test_data(1)
expected_result_part_1 = 142


def test_part_1():
    assert type(test_data) == str
    assert type(day_01.part_1(test_data)) == int
    assert day_01.part_1(test_data) == expected_result_part_1
