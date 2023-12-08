from load_data import get_data,get_test_data
from itertools import cycle
import copy
day = 8
"""Part 1 Pseudo Code
1. Create function that outputs dictionary for instructions, and mapping dictionary
2. Iterate through dictionary to find next step in the loop

Note: This method is brute force and takes too long.

Will try a different approach. - *Update* Error in code was causing the delayed run

1. Find the terminal point achieved if the instructions are followed exactly once
2. If ZZZ is reached, flag how many steps are taken for it to be reached

Part 2 -
1. Find all the starting nodes that end in A
2. Take the next step
3. Check to see if all the next step is ends in Z. If so stop and record count.
If not, continue
"""
def _parse_data(data:str )-> dict:
    """Takes in the data as a string and returns a dictionary with the following structure:
    {
        'instructions' : [L,R...],
        'network' :
        {
            'AAA' : ('BBB', 'CCC'),...
        }
    }
    """
    raw_list = data.strip().split('\n\n')

    # Create a data dictionary
    data_dict = {}
    data_dict['instructions'] = raw_list[0]
    data_dict['network'] = {}
    node_str_list = raw_list[1].strip().split('\n')

    for node_str in node_str_list:

        node = node_str[0:3]
        node_left = node_str[7:10]
        node_right = node_str[12:15]
        data_dict['network'][node] = (node_left, node_right)

    return data_dict

def _brute_force(data:str) -> dict:
    """Takes in an original data string and finds the number of steps required
    to get to the end of the map
    """
    #Read in the data
    data_dict = _parse_data(data)
    instructions = data_dict['instructions']
    network = data_dict['network']

    current_location = 'AAA'
    count = 0

    for step in cycle(instructions):
        if step == 'L':
            new_location = network[current_location][0]
        else:
            new_location = network[current_location][1]
        count +=1
        current_location = new_location
        if count%10000000 ==0:
            print(count)
            print(current_location)
        if current_location == 'ZZZ':
            break

    return count

def _find_next_location(instruction: str, network:dict, current_location:str) -> str:
    """Takes in instruction, netowrk, current location and returns the next location"""
    if instruction == 'L':
        new_location = network[current_location][0]
    else:
        new_location = network[current_location][1]
    return new_location

def _terminal_dict(instructions: str, network:dict, start:str, end_search = False, end: str = 'ZZZ')-> dict:
    """Takes in the instructions, network and starting point and returns a
    dictionary containing the ending node. If end search is True,  """
    if end_search:
        record_count = None
        count = 0
        current_location = start
        for step in instructions:
            if step == 'L':
                new_location = network[current_location][0]
            else:
                new_location = network[current_location][1]
            count += 1
            current_location = new_location
            if current_location == 'ZZZ':
                record_count = count
                break
        terminal_dict = {'terminal' : current_location, 'ZZZ' : record_count}

    else:
        current_location = start
        for step in instructions:
            if step == 'L':
                new_location = network[current_location][0]
            else:
                new_location = network[current_location][1]
            current_location = new_location

        terminal_dict = {'terminal' : current_location, 'ZZZ' : None}

    return terminal_dict

def _start_node_list(network: dict) -> list:
    """Generate pt2_start nodes as a list"""
    return [key for key, values in network.items() if key[2] == 'A']


def _next_node_list(step:str, network: dict, current_nodes: list) -> list:
    """Takes in current_nodes as a list and the network nodes as a dict
    and returns a list of next nodes"""
    return[ _find_next_location(step, network, node) for node in current_nodes]


def _check_node_list(current_nodes: list, check_value='Z') -> int:
    """Takes in the current nodes as a list and looks to see if the check value
    is the last letter. If so, it counts, and returns a count
    """
    pass

def part_1(data:str) -> dict:
    return _brute_force(data)

def part_2():
    pass


if __name__ == "__main__":

    # data = get_test_data(day)
    # _parse_data(data)
    test_data = get_test_data(8)
    # data_dict = _parse_data(test_data)
    # instructions = data_dict['instructions']
    # network = data_dict['network']
    # _terminal_dict(instructions, network, 'DDD', end_search=True)
    # print(part_1(test_data))
    # Uncomment the lines below when your function passes the test!
    real_data = get_data(day)
    print(f'part 1 solution = {part_1(real_data)}')
    # # # print(f'part 2 solution = {part_2(real_data)}')

    # data_dict = _parse_data(real_data)
    # instructions = data_dict['instructions']
    # network = data_dict['network']





#     print(f'Original size {len(network)}')

#    # Create replacement dictionary
#     replacement_dict = {}
#     for key, value in network.items():
#         if value[0] == value[1]:
#             replacement_dict[key] = value

#     new_network = copy.deepcopy(network)
#     # Delete old keys
#     for key, value in network.items():
#         if key in replacement_dict.keys():
#             del new_network[key]

#     # Cycle through and replace values in dictionary
#     for key, value in new_network.items():
#         if value[0] in replacement_dict.keys():
#             new_l = replacement_dict[value[0]]
#         else:
#             new_l = value[0]

#         if value[1] in replacement_dict.keys():
#             new_r = replacement_dict[value[1]]
#         else:
#             new_r = value[1]

#         new_network[key] = (new_l, new_r)

#     print(f"Cycle 1 complete. Size:{len(new_network)}")

#     network = copy.deepcopy(new_network)
#    # Create replacement dictionary
#     replacement_dict = {}
#     for key, value in network.items():
#         if value[0] == value[1]:
#             replacement_dict[key] = value

#     new_network = copy.deepcopy(network)
#     # Delete old keys
#     for key, value in network.items():
#         if key in replacement_dict.keys():
#             del new_network[key]

#     # Cycle through and replace values in dictionary
#     for key, value in new_network.items():
#         if value[0] in replacement_dict.keys():
#             new_l = replacement_dict[value[0]]
#         else:
#             new_l = value[0]

#         if value[1] in replacement_dict.keys():
#             new_r = replacement_dict[value[1]]
#         else:
#             new_r = value[1]

#         new_network[key] = (new_l, new_r)

#     print(f"Cycle 2 complete. Size:{len(new_network)}")
