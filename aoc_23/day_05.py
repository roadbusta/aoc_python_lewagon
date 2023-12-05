from load_data import get_data,get_test_data
import re
import numpy as np
from itertools import chain
day = 5

""" Part 1 Pseudo code
1. Separate the text file into different dictionaries for the ranges. First
would be a list, everything else would be dictionaries
    - Tests:
        - Test that it is a list/ dictionary
        - Test that there are positive integers
        - Test that each of the sub dictionarys have a length of three

2. For each seed, use the different dictionaries to find the outputs.
Use the tables to find the maps for the inputs
"""

"""Part 2 Pseudo code:
Similar to part 1, but the initial seed list is longer.
Update _parse_source_data to include an argument to expand seed list
"""

def _positive_int(input_list: list) -> bool:
    """ A simple function that can be used to check if items in the list are positive intiger
    """
    output = True
    try:
        for i in input_list:
            if type(i) != int or i < 0:
                output = False
    except:
        output =  False

    return output

def _parse_source_data(data: str, expand_seeds = False) -> dict:
    """ Takes in the raw data and convert this into dictionaries within
    dictionaries with the following structure:
    {
    'seeds' : [...],
    'seed-to-soil' : [
        {'dest' : ##, 'source' : ##, 'range_len' : ##},...
        ]
    }
    """
    parsed_dict = {}
     # split data into vector/list of numbers
    raw_list = data.strip().split('\n\n')

    # Get the seed info
    if expand_seeds:
        pass
    else:
        parsed_dict['seeds'] = [int(i) for i in raw_list[0].split(':')[1].strip().split()]

    for item in raw_list[1:]:
        split_item =item.strip().split(' map:')
        name = split_item[0]
        parsed_list = []
        data_list = split_item[1].strip().split('\n')

        for data in data_list:
            sub_list = [int(i) for i in data.split()]
            dest = sub_list[0]
            source = sub_list[1]
            range_len = sub_list[2]
            parsed_list.append({ 'dest' : dest, 'source': source, 'range_len': range_len})

        parsed_dict[name] = parsed_list

    return parsed_dict

def _destination(source_num: int, list_dict:list) -> int:
    """Takes in a source value and mapping list of dictionaries as an integer and returns the destination value as
    an integer
    """
    dest_num = source_num
    for sub_dict in list_dict:
        source = sub_dict['source']
        dest = sub_dict['dest']
        if source_num in range(source, source + sub_dict['range_len']):
            delta = source_num - source
            dest_num = dest + delta
        else:
            continue

    return dest_num

def _final_destination(seed_num: int, parsed_data:dict) -> int:
    """ Takes in source number and parsed_data_dict and returns the final
    destination_number for the source number
    """
    dest_1 = _destination(seed_num, parsed_data['seed-to-soil'])
    dest_2 = _destination(dest_1, parsed_data['soil-to-fertilizer'])
    dest_3 = _destination(dest_2, parsed_data['fertilizer-to-water'])
    dest_4 = _destination(dest_3, parsed_data['water-to-light'])
    dest_5 = _destination(dest_4, parsed_data['light-to-temperature'])
    dest_6 = _destination(dest_5, parsed_data['temperature-to-humidity'])

    return _destination(dest_6, parsed_data['humidity-to-location'])

def part_1(data:str) -> int:
    """ Takes in the test data then returns the lowest location
    """

    # Parse the data
    parsed_data = _parse_source_data(data)

    # Generate seed list
    seeds = parsed_data['seeds']

    # Generate destition list
    dest_list = [_final_destination(seed_num, parsed_data) for seed_num in seeds]

    return min(dest_list) # Return the minimum value


def part_2():
    pass


if __name__ == "__main__":

    ## Uncomment the lines below when your function passes the test!
    # data = get_test_data(day)
    real_data = get_data(day)
    # parsed_data = _parse_source_data(data)
    # test_mapping_dict = [{'dest' : 50, 'source' : 98, 'range_len' : 2}]
    # _destination(99, test_mapping_dict)

    print(f'part 1 solution = {part_1(real_data)}')
    # print(f'part 2 solution = {part_2(real_data)}')


    pass
