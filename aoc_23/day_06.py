from load_data import get_data,get_test_data
import re
import numpy as np
from itertools import chain
day = 6
""" Part 1 Pseudocode:
- Find a way to parse the data such that there is a "Time" list and "Distance"
are lists within a dictionary, with a structure as follows:
{'time' : [...], 'distance' : [...]}
    - Tests:
        - Time and Distance are lists
        - Lists are the same size
        - Lists contain positive integers
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

def _generate_lists(data:str) -> dict:
    """Takes in a string and returns a dictionary containing the time and distance
    """
    raw_list = data.strip().split('\n')

    # Create a game dictionary
    card_dict = {}

    for line in raw_list:
        colon_idx = line.find(':') # Find the colon index
        category = line[:colon_idx].strip().lower() # Find the full card
        hist_data = [int(i) for i in line[colon_idx+1:].split()] # Get the historical data

        card_dict[category] = hist_data # Populate the card dictionary

    return card_dict

def part_1():
    pass

def part_2():
    pass


if __name__ == "__main__":

    ## Uncomment the lines below when your function passes the test!
    data = get_test_data(day)
    _generate_lists(data)
    ## Uncomment the lines below when your function passes the test!
    # data = get_data(day)
    # print(f'part 1 solution = {part_1(real_data)}')
    # print(f'part 2 solution = {part_2(real_data)}')


    pass
