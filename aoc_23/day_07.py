from load_data import get_data,get_test_data
import re
import numpy as np
import pandas as pd
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

def _hand_dict(hand_str:str) -> dict:
    """Takes in hand as a string or list and returns a dictionary of the hand
    """
    hand_dict = {}
    for card in hand_str:
        if str(card) not in hand_dict.keys():
            hand_dict[str(card)] = 1
        else:
            hand_dict[str(card)] += 1
    return hand_dict

def _sort_dict_val(original_dict:dict) -> dict:
    """ Takes in a dictionary and returns it sorted by value
    """
    return {k: v for k, v in sorted(original_dict.items(), key=lambda x: x[1])}

def _wildcard(original_hand_str: str) -> int:
    """Takes in original hand and returns the updated hand taking into account the wild card
    """
    modified_hand = original_hand_str

    hand_dict=_sort_dict_val(_hand_dict(original_hand_str))
    if 'J' in hand_dict.keys():
        if hand_dict['J'] ==5:
            modified_hand = original_hand_str
        else:
            del hand_dict['J'] # Delete J from the dictionary
            j_wild = list(hand_dict.keys())[-1] # j wild will now be the most represented letter
    
            modified_hand = original_hand_str.replace('J', j_wild)

    return modified_hand

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
        if max(_hand_dict(hand_str).values()) == 4:
            hand = 5 
        else:
            hand = 4

    # Check for three-of-a-kind vs two-pair
    elif len (check_set) == 3:  
        if max(_hand_dict(hand_str).values()) == 3:
            hand = 3
        else:
            hand = 2
    return hand

def _hand_parser(hand_str:str)-> list:
    """Takes in a string list and converts it into a list of numbers
    """
    hand_list = [] 
    face_card_map= {'T': 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
    for card in hand_str:
        if card in face_card_map.keys():
            hand_list.append(face_card_map[card]) # Replace face card with mapped value
        else:
            hand_list.append(int(card)) # Replace with integer version of string

    return hand_list

def _hand_scorer(hand_list:list, hand_type: int)-> int:
    """
    Computes score for each hand type
    """
    # High Card
    if hand_type == 0:
        score_list = hand_list  # Create a hand list 

    # Pair
    elif hand_type == 1:
        thresh = 60
        score_list = []
        hand_dict = _hand_dict(hand_list)
        for card in hand_list:
            if hand_dict[str(card)] == 2:
                score_list.append(card*thresh)
            else:
                score_list.append(card)
    

    # Two Pair
    elif hand_type == 2:
        thresh = 180
        score_list = []
        hand_dict = _hand_dict(hand_list)
        for card in hand_list:
            if hand_dict[str(card)] == 2:
                score_list.append(card*thresh)
            else:
                score_list.append(card)


    # Three of a kind
    elif hand_type == 3:
        thresh = 1800
        score_list = []
        hand_dict = _hand_dict(hand_list)
        for card in hand_list:
            if hand_dict[str(card)] == 3:
                score_list.append(card*thresh)
            else:
                score_list.append(card)


    #Full house
    elif hand_type == 4:
        thresh = 7000
        score_list = []
        hand_dict = _hand_dict(hand_list)
        for card in hand_list:
            if hand_dict[str(card)] != 1:
                score_list.append(card*thresh)
            else:
                score_list.append(card)


    #4 of a kind
    elif hand_type == 5:
        thresh = 60000
        score_list = []
        hand_dict = _hand_dict(hand_list)
        for card in hand_list:
            if hand_dict[str(card)] != 1:
                score_list.append(card*thresh)
            else:
                score_list.append(card)
    
     #5 of a kind
    elif hand_type == 6:
        thresh = 400000
        score_list = []
        hand_dict = _hand_dict(hand_list)
        for card in hand_list:
            score_list.append(card*thresh)
           
    
    return sum(score_list)

def _game_dict(data:str) -> dict:
    """Takes in a string and returns a dictionary containing the hand and bet
    """
    raw_list = data.strip().split('\n')

    # Create a game dictionary
    game_dict = {}
    for line in raw_list:
        game_info = line.strip().split(' ')
        hand = game_info[0]
        bet = game_info[1]
        game_dict[hand] = bet

    return game_dict

def _game_df(data:str) -> dict:
    """Takes in a string and returns a dataframe containing the hand and bet
    """
    raw_list = data.strip().split('\n')

    # Create a game dictionary
    hand_col = []
    bet_col = []
    for line in raw_list:
        game_info = line.strip().split(' ')
        hand_col.append(game_info[0])
        bet_col.append(int(game_info[1]))

    game_data = { 'hand' : hand_col, 'bet': bet_col}

    return pd.DataFrame.from_dict(game_data) 

def _hand_alpha(hand_str: str) -> str:
    """
    Take in the original hand_str and return the alpha string
    """
    hand_map = {'2' : 'a', 
                '3' : 'b', 
                '4' : 'c', 
                '5' : 'd',
                '6' : 'e',
                '7' : 'f',
                '8' : 'g',
                '9' : 'h',
                'T' : 'i', 
                'J' : 'j',
                'Q' : 'k',
                'K' : 'l',
                'A' : 'm'}
    hand_alpha = ''
    for card in hand_str:
        hand_alpha += (hand_map[card])

    return hand_alpha.strip()

def _hand_alpha_2(hand_str: str) -> str:
    """
    Take in the original hand_str and return the alpha string
    """
    hand_map = {'J' : 'a', 
                '2' : 'b', 
                '3' : 'c', 
                '4' : 'd',
                '5' : 'e',
                '6' : 'f',
                '7' : 'g',
                '8' : 'h',
                '9' : 'i', 
                'T' : 'j',
                'Q' : 'k',
                'K' : 'l',
                'A' : 'm'}
    hand_alpha = ''
    for card in hand_str:
        hand_alpha += (hand_map[card])

    return hand_alpha.strip()

def part_1(data:str) ->int:
    """Takes in data as a string and returns a dataframe
    """
    # Create an initial game dataframe
    game_df = _game_df(data)

    # Create column of hand types
    game_df['hand_type'] = game_df['hand'].map(lambda x: _hand(x))

    # Create a column of converted hand types
    game_df['hand_alpha'] = game_df['hand'].map(lambda x : _hand_alpha(x))

    # Sort the df by hand type
    game_df = game_df.sort_values(by = ['hand_type', 'hand_alpha'], ignore_index = True)

    # Create a column ranking
    game_df['index'] = range(len(game_df))
    game_df['rank'] = game_df.copy()['index'] + 1

    # Create winnings column
    game_df['winnings'] = game_df.copy()['bet'] * game_df.copy()['rank']

    return game_df['winnings'].sum()

def part_2(data:str):
    """Takes in data as a string and returns a dataframe
    """
    # Create an initial game dataframe
    game_df = _game_df(data)

    # Create column of hand types
    game_df['hand_type'] = game_df['hand'].map(lambda x: _hand(_wildcard(x)))

    # Create wild column
    game_df['wild'] = game_df['hand'].map(lambda x: _wildcard(x))

    # Create a column of converted hand types using the updated hand type
    game_df['hand_alpha'] = game_df['hand'].map(lambda x : _hand_alpha_2(x))

    # Sort the df by hand type
    game_df = game_df.sort_values(by = ['hand_type', 'hand_alpha'], ignore_index = True)

    # Create a column ranking
    game_df['index'] = range(len(game_df))
    game_df['rank'] = game_df.copy()['index'] + 1

    # Create winnings column
    game_df['winnings'] = game_df.copy()['bet'] * game_df.copy()['rank']
    
    return game_df['winnings'].sum()


if __name__ == "__main__":

    data = get_test_data(day)
    # print(part_2(data))

    # ## Uncomment the lines below when your function passes the test!
    real_data = get_data(day)
    print(f'part 1 solution = {part_1(real_data)}')
    print(f'part 2 solution = {part_2(real_data)}')


    pass
