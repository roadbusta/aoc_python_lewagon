from load_data import get_data,get_test_data
import re
import numpy as np
from itertools import chain
day = 7
""" Part 1 Pseudocode:
1. Categorise a five letter string into a hand type based on the following logic:
- All 5 numbers are the same (dict len = 1)
- 4 numbers are the same (dict len = 2)
- 3 numbers are the same and two numbers are the same (dict len = 2)
- 3 numbers are the same (dict len = 3)
- 2 numbers and 2 numbers are the same (dict len = 3) 
- 2 numbers are the same (dict len = 4)
- no numbers are tbe same (dict len = 5)

Can do this by building a dictionary containing the character, and the number of times
that it appears in the string 

2. Find some way of accounting for each of the hand ranks. Maybe a weighting factor?
2. Assign values to each of the strings where A = 14 and 2 = 2
3. Apply weighting factor based on type of hand and calculate score
"""

def _hand(hand_str: str)->int:
    """Takes in a 5 letter string and returns the hand as per the following code:
    0: HighCard
    1: Pair
    2: Two Pair
    3: Three of a kind
    4: Full house
    5: Four of a kind
    6: Five of a kind
    """
    check_set = set(hand_str) # Find number of unique numbers
    hand = 99

    # Do simple checks to see if cards meet hand conditions
    if len(check_set) == 1:
        hand = 6
    elif len(check_set) == 4:
        hand = 1
    elif len(check_set) == 5:
        hand = 0

    # Check for four-of-a-kind vs full house
    elif len (check_set) == 2:
        hand_dict = {}
        for card in hand_str:
            if str(card) not in hand_dict.keys():
                hand_dict[card] = 1
            else:
                hand_dict[card] += 1
        if max(hand_dict.values()) == 4:
            hand = 5
        else:
            hand = 4

    return hand


    pass
def part_1():
    pass

def part_2():
    pass


if __name__ == "__main__":

    ## Uncomment the lines below when your function passes the test!
    data = get_test_data(day)
    print(_hand('22223'))
    # print(f'part 1 solution = {part_1(real_data)}')
    # print(f'part 2 solution = {part_2(real_data)}')


    pass
