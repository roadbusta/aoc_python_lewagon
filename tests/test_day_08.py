from aoc_23.day_08 import _parse_data, part_1
from aoc_23.load_data import get_test_data



test_data = get_test_data(8)
test_data_2 = get_test_data('8-2')
expected_result_part_1a = 2
expected_result_part_1b = 6
expected_result_part_2 = None


def test_part_1():
    assert type(test_data) == str
    assert type(_parse_data(test_data)) == dict
    assert len(_parse_data(test_data)) == 2
    assert type(_parse_data(test_data)['network']['AAA'])== tuple

    assert part_1(test_data)== expected_result_part_1a
    assert part_1(test_data_2) == expected_result_part_1b

    pass


def test_part_2():
   pass
