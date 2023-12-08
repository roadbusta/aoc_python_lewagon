from aoc_23.day_08 import _parse_data, part_1, _terminal_dict, _start_node_list, _next_node_list, _check_node_list
from aoc_23.load_data import get_test_data

test_data = get_test_data(8)
test_data_2 = get_test_data('8-2')
data_dict = _parse_data(test_data)
instructions = data_dict['instructions']
network = data_dict['network']
expected_result_part_1a = 2
expected_result_part_1b = 6

test_data_3 =get_test_data('8-3')
data_dict_3 = _parse_data(test_data_3)
instructions_3 = data_dict_3['instructions']
network_3 = data_dict_3['network']
expected_result_part_2 = 6


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
    assert type(_start_node_list(network_3)) == list
    assert len(_start_node_list(network_3)) == 2
    assert _start_node_list(network_3)[0] == '11A'
    assert _start_node_list(network_3)[1] == '22A'

    assert type(_next_node_list('L', network_3, ['11A', '22A'])) == list
    assert _next_node_list('L', network_3, ['11A', '22A']) == ['11B', '22B']
    pass
