from load_data import get_data,get_test_data
import numpy as np

day = 6
""" Part 1 Pseudocode:
1. Find a way to parse the data such that there is a "Time" list and "Distance"
are lists within a dictionary, with a structure as follows:
{'time' : [...], 'distance' : [...]}
    - Tests:
        - Time and Distance are lists
        - Lists are the same size
        - Lists contain positive integers

2. Take in two numbers, the time and record distance.
Create a reverse list loop that does a forward iteration and reverse
iteration, multiiplying each of the numbers together.
Then take look through the loop to see how many winning combinations there are
where the distance is greater than the threshold
    - Tests:
        - Check integer
        - Check with 7, 9, should return 4
"""

""" Part 2 Pseudocode:
Join the string as one list, then let it run
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

def _num_wins(time: int, distance_record: int) -> int:
    """Takes in the time and distance record, and returns number of winning
    combinations
    """
    # create race list
    race_list = list(range(0, time+1))
    distance_list = [race_list[i] * race_list[len(race_list)-1-i] for i in race_list]
    winning_combinations = 0
    for j in distance_list:
        if j>distance_record:
            winning_combinations +=1

    return winning_combinations

def _convert(num_list:list) -> list:
    """Takes in a separate num_list and return a final int list
    """
    # Converting integer list to string list
    s = [str(i) for i in num_list]

    # Join list items using join()
    res = int("".join(s).strip())

    return [res]

def part_1(data: str) -> np.int64:
    """ Takes in the data, then returns number of way race could be won
    """
    race_data = _generate_lists(data)
    time = race_data['time']
    distance = race_data['distance']

    combo_list = [_num_wins(time[i], distance[i]) for i in range(len(time))]

    return np.prod(combo_list)

def part_2(data:str) -> np.int64:
    """ Takes in the data, joins the race number, then returns number of way race could be won
    """
    race_data = _generate_lists(data)
    time = _convert(race_data['time'])
    distance = _convert(race_data['distance'])

    combo_list = [_num_wins(time[i], distance[i]) for i in range(len(time))]

    return np.prod(combo_list)


if __name__ == "__main__":

    ## Build the data
    # data = get_test_data(day)
    # _generate_lists(data)
    # _num_wins(7,9)

    ## Uncomment the lines below when your function passes the test!
    real_data = get_data(day)
    print(f'part 1 solution = {part_1(real_data)}')
    print(f'part 2 solution = {part_2(real_data)}')


    pass
