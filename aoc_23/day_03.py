from load_data import get_data,get_test_data
import re
import numpy as np
day = 3
# Convert data into array 2d array -- DONE --
# Write a function that identifies numbers, and returns their array position
# Write a function that identifies a group of numbers, and returns the surrounding array positions
# Write a function that checks around the number for another symbol

def str_to_array(data: str) -> np.ndarray:
    """ Takes in the data as a multiline string and returns it as an nd.array
    with every element inside a 2D arrays
    """
    str_list = data.splitlines() # Split into an array
    list_of_lists = [] # Create an empty list
    for line in str_list:
        list_of_lists.append(list(line)) # Split each line into an array

    return np.array(list_of_lists)

def num_position(machine_array: np.ndarray) -> list:
    """
    Takes in the machine as an array and returns a list of dictionaries with
    every number and it's position in the ndarray
    """
    num_dict_list = [] # Create an empty number dictionary list
    for i in range(len(machine_array)): # For each row
        for j in range(len(machine_array[i])): # For each item in the row
            char = str(machine_array[i,j]) # Look at the character
            if char.isdigit(): # If it's a digit
                num_dict = {char : [i,j]} # Create a dictionary for it
                num_dict_list.append(num_dict) # Add it to the dictionary list

    return num_dict_list

def find_valid_adj(i,j):
    """
    Does a search around i and j and returns True if found
    """
    valid_adj = False

    return valid_adj

def valid_array(machine_array: np.ndarray) -> np.ndarray:
    """
    Takes in the machine as an array and returns a validated array where a 1
    represents a value to be retained
    """
    # create an empty array same size of machine_array
    valid_array = np.zeros(machine_array.shape)

    for i in range(len(machine_array)): # For each row
        for j in range(len(machine_array[i])): # For each item in the row
            # Check if it is a number
            char = str(machine_array[i,j]) # Look at the character
            if char.isdigit(): # If it's a digit

            # Check the top left corner produces a valid location, and if so,
            # Check to see if it is a character that is not a number or period.
            # As soon as it meets this condition, this spot is valid, and mark it's position
            # on the valid array

            # Then write a function to see if it is part of a number that exists on the valid array



    return valid_array




def part_1(data: str) -> int:
    pass

def part_2(data: str) ->int:
    pass


## Uncomment the lines below when your function passes the test!
# real_data = get_data(day)

# print(f'part 1 solution = {part_1(real_data)}')
# print(f'part 2 solution = {part_2(real_data)}')

if __name__ == "__main__":

    # ## Uncomment the lines below when your function passes the test!
    data = get_test_data(day)
    machine_array = str_to_array(data)
    print(machine_array)
    num_position_list = num_position(machine_array)
    print(valid_array(machine_array))
    # num_group(num_position_list)
    # part_1(real_data)
    # part_2(real_data)

    pass
