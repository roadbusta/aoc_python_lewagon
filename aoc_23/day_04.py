from load_data import get_data,get_test_data
import re
import numpy as np
from itertools import chain
day = 4
"""
Part 1 Pseudo Code:
1. Take in each line, and create a dictionary for each card. The dictionary key
is the Card number, and the dictionary value is a list of two lists. The first
list is the list of winning numbers, the second list is the list of my numbers
    Tests:
        - Dictionary output
        - Non-empty lists
        - Only positive integers in the lists including 0

2. Iterate through my list of numbers, and check to see if any of them are
winners. Count the number of winners as 'n'.
    Tests:
    - Number of winners is a positive integer

3. Create a dictionary that calculates 2^(n-1) for each card. Create an
exception for 0. This is the point value of the card.
    Tests:
    - Point value is a positive integer (including zero)

4. Sum the cards.
    Tests:
    - Sum is a positive integer
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

def _card_dict(data:str )-> dict:
    """
    Takes in raw data (Card number and winning/ my numbers) as a multiline
    string and returns a dictionary with the following structure:
    { <card_id> : [ [winning numbers], [my numbers]]}
    """
     # split data into vector/list of numbers
    raw_list = data.strip().split('\n')

    # Create a game dictionary
    card_dict = {}

    for line in raw_list:
        colon_idx = line.find(':') # Find the colon index
        full_card_id = line[:colon_idx] # Find the full card
        card_id = re.findall(r'\d+', full_card_id)[0] # Get the game ID

        full_card_info = line[colon_idx+1:].split('|') # Separate out the numbers
        winning_numbers = full_card_info[0].strip().split() # Get a list of winning numbers
        winning_numbers = [int(i) for i in winning_numbers] # Convert to integers
        my_numbers = full_card_info[1].strip().split() # Get a list of my numbers
        my_numbers = [int(i) for i in my_numbers] # Convert to integers

        card_dict[card_id] = [winning_numbers, my_numbers]

    return card_dict

def _points_dict(card_dict: dict) -> dict:
    """ Takes in the card dictionary and returns a count dictionary with the
    following structure:
    {
    <card_id> : <number of points>,
    ...
    }
    """
    points_dict = {}
    for card, card_info in card_dict.items():
        win_count = 0
        winning_numbers = card_info[0]
        my_numbers = card_info[1]

        for my_number in my_numbers:
            if my_number in winning_numbers:
                win_count +=1

        if win_count == 0:
            points = 0
        else:
            points = 2**(win_count-1)

        points_dict[card] = points

    return points_dict



def part_1(data:str) ->int:
    """
    Takes in raw data (card number and winning/ my numbers) the sum of scores
    """
    card_dict = _card_dict(data)
    points_dict=_points_dict(card_dict)
    pass

def part_2():
    pass


if __name__ == "__main__":

    ## Uncomment the lines below when your function passes the test!
    data = get_test_data(day)
    card_dict = _card_dict(data)
    _points_dict(card_dict)
    # print(f'part 1 solution = {part_1(real_data)}')
    # print(f'part 2 solution = {part_2(real_data)}')


    pass
