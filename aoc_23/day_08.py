from load_data import get_data,get_test_data
import re
import numpy as np
from itertools import chain
day = 8
"""Part 1 Pseudo Code
1. Create function that outputs dictionary for instructions, and mapping dictionary
2. Iterate through dictionary to find next step in the loop
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
    card_dict = {}
    card_dict['instructions'] = raw_list[0]
    card_dict['network'] = {}
    node_str_list = raw_list[1].strip().split('\n')
    
    for node_str in node_str_list:
      
        node = node_str[0:2]
        node_left = node_str[7:9]
        node_right = node_str[12:14]
        card_dict['network'][node] = (node_left, node_right)
    
    # for node in raw_list[1]:
    #     colon_idx = line.find(':') # Find the colon index
    #     category = line[:colon_idx].strip().lower() # Find the full card
    #     hist_data = [int(i) for i in line[colon_idx+1:].split()] # Get the historical data

    #     card_dict[category] = hist_data # Populate the card dictionary

    # return card_dict
    # pass
    print(card_dict)
    print(node_str)
    pass

def part_1():
    pass

def part_2():
    pass


if __name__ == "__main__":

     data = get_test_data(day)
     _parse_data(data)

    ## Uncomment the lines below when your function passes the test!
    # data = get_data(day)
    # print(f'part 1 solution = {part_1(real_data)}')
    # print(f'part 2 solution = {part_2(real_data)}')