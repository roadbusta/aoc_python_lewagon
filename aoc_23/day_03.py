from load_data import get_data,get_test_data
import re
import numpy as np
from itertools import chain
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

def find_valid_adj(machine_array,i,j):
    """
    Does a search around i and j and returns True if found
    """
    shape = machine_array.shape
    valid_adj = False
    ignore_list = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for a in [-1,0,1]:
        for b in [-1,0,1]:
            alpha = i+a
            beta = j+b
            if alpha > -1 and alpha < shape[0] and beta >-1 and beta < shape[1]:
                check_char = machine_array[alpha,beta]
                if check_char not in ignore_list:
                    valid_adj = True

    return valid_adj

def valid_array(machine_array: np.ndarray) -> np.ndarray:
    """
    Takes in the machine as an array and returns a validated array where a 1
    represents a value to be retained
    """
    # create an empty array same size of machine_array
    valid_array = np.full(machine_array.shape, ',')


    for i in range(len(machine_array)): # For each row
        for j in range(len(machine_array[i])): # For each item in the row
            # Check if it is a number
            char = str(machine_array[i,j]) # Look at the character
            if char.isdigit(): # If it's a digit
                if find_valid_adj(machine_array,i,j):
                    valid_array[i,j] = machine_array[i,j]

    return valid_array

def valid_number_group():
    pass




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
    validated_array = valid_array(machine_array)
    print(validated_array)
    flatten_list = list(chain.from_iterable(validated_array))
    long_string = "".join(flatten_list).split(',')
    final_list = [i for i in long_string if i]
    print(final_list)
    # num_group(num_position_list)
    # part_1(real_data)
    # part_2(real_data)

    pass
