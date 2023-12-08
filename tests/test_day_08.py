from aoc_23.day_08 import _parse_data, part_1, _terminal_dict
from aoc_23.load_data import get_test_data



test_data = get_test_data(8)
test_data_2 = get_test_data('8-2')
data_dict = _parse_data(test_data)
instructions = data_dict['instructions']
network = data_dict['network']
expected_result_part_1a = 2
expected_result_part_1b = 6
expected_result_part_2 = None


def test_part_1():
    assert type(test_data) == str
    assert type(data_dict) == dict
    assert len(data_dict) == 2
    assert type(data_dict['network']['AAA'])== tuple


    assert type(_terminal_dict(instructions, network, 'AAA')) == dict
    assert _terminal_dict(instructions, network, 'AAA')['terminal'] == 'ZZZ'
    assert _terminal_dict(instructions, network, 'DDD')['terminal'] == 'DDD'
    assert _terminal_dict(instructions, network, 'BBB')['terminal'] == 'EEE'
    assert _terminal_dict(instructions, network, 'AAA', end_search=True)['terminal'] == 'ZZZ'
    assert _terminal_dict(instructions, network, 'DDD', end_search=True)['terminal'] == 'DDD'
    assert _terminal_dict(instructions, network, 'BBB', end_search=True)['terminal'] == 'EEE'
    assert _terminal_dict(instructions, network, 'AAA', end_search=True)['ZZZ'] == 2
    assert _terminal_dict(instructions, network, 'DDD', end_search=True)['ZZZ'] == None
    assert _terminal_dict(instructions, network, 'BBB', end_search=True)['ZZZ'] == None

    assert part_1(test_data)== expected_result_part_1a
    assert part_1(test_data_2) == expected_result_part_1b
    pass


def test_part_2():
   pass
