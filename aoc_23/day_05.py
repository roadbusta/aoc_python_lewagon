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
        {'dest' : ##, 'source' : ##, 'range' : ##},...
        ]
    }
    """

    pass


def part_1():
    pass

def part_2():
    pass


if __name__ == "__main__":

    ## Uncomment the lines below when your function passes the test!
    data = get_test_data(day)
    # print(f'part 1 solution = {part_1(real_data)}')
    # print(f'part 2 solution = {part_2(real_data)}')


    pass
