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

def _parse_source_data(data: str) -> dict:
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


def part_1():
    pass

def part_2():
    pass


if __name__ == "__main__":

    ## Uncomment the lines below when your function passes the test!
    data = get_test_data(day)
    _parse_source_data(data)
    # print(f'part 1 solution = {part_1(real_data)}')
    # print(f'part 2 solution = {part_2(real_data)}')


    pass
