from load_data import get_data,get_test_data
from itertools import combinations
import re
day = 2
def game_dictionary(data: str) -> dict:
    """Takes in raw data (game data and ID) as a multiline string and returns a
    dictionary with the game ID and the information from the games
    """
    # split data into vector/list of numbers
    raw_list = data.strip().split('\n')

    # Create a game dictionary
    game_dict = {}

    for line in raw_list:
        colon_idx = line.find(':') # Find the colon index
        full_game_id = line[:colon_idx] # Get the FULL game ID
        game_id = re.findall(r'\d+', full_game_id)[0] # Get the game ID
        game_info = line[colon_idx+1:].split(';') # Get the game information]
        sub_game_list = [] # Create a sub game list
        for sub_game in game_info:
            sub_game_info = sub_game.split(',') # Split the sub_game
            sub_game_dict = {}

            for info in sub_game_info:
                colour = re.findall(r'[a-zA-Z]+',info)[0] # Find the colour
                colour_count = int(re.findall(r'\d+',info)[0].strip()) # Find the colour count
                sub_game_dict[colour] = colour_count # Create a sub game dictionary

            sub_game_list.append(sub_game_dict) # Append results to a sub_game_list

        game_dict[game_id] = sub_game_list # Add results to the game dictioary

    return game_dict

def part_1(real_data: str) -> int:
    """Takes in the game dictionary and the colour limits, and returns the sum
    of the IDs of the games with valid sub games
    """
    # Set the limits of the number of colours
    limits = {'red' : 12,
              'green' : 13,
              'blue' : 14}
    game_dict = game_dictionary(real_data)
    valid_games = [] # Create an empty games list
    for game_id, game_list in game_dict.items(): # Iterate through the games list
        game_valid = True # Set the default value to be false
        for game in game_list: # For each game
            for colour, number in game.items(): # Check the colour and number in each game
                if number > limits[colour]: # If the number of colours exceed the limit
                    game_valid = False # Convert to false

        if game_valid:
            valid_games.append(int(game_id.strip())) # Add to valid game list


    return sum(valid_games)

def part_2(data: str) ->int:
    # Create a game dictionary
    game_dict = game_dictionary(data)

    # Create an empty power dictionary
    power_dict = {}
    for game_id, game_list in game_dict.items():
        max_colour_dict = {'red' : 0, 'green' : 0, 'blue' : 0} # Set the max colour values

        for game in game_list: # For each game

            for colour, count in game.items(): # Check each colour count
                if count > max_colour_dict[colour]: # If the colour count is greater than the min
                    max_colour_dict[colour]= count  # Update the colour count

        power_value = 1
        for max_colour, max_count in max_colour_dict.items():
            power_value = power_value * max_count # Calculate the power value for a given game

        power_dict[game_id] = power_value # Generate a power dictionary with all the values

    return sum(power_dict.values()) # Return the sume of the values


## Uncomment the lines below when your function passes the test!
real_data = get_data(day)

print(f'part 1 solution = {part_1(real_data)}')
print(f'part 2 solution = {part_2(real_data)}')

if __name__ == "__main__":

    # ## Uncomment the lines below when your function passes the test!
    real_data = get_test_data(day)
    part_1(real_data)
    part_2(real_data)

    pass
