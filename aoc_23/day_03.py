from load_data import get_data,get_test_data
import re
import numpy as np
day = 3
# Convert data into array 2d array
# Write a function that identifies numbers, and returns their array position
# Write a function that checks around the number for another symbol

def str_to_array(data: str) -> np.array:
    str_list = data.splitlines() # Split into an array
    list_of_lists = [] # Create an empty list
    for line in str_list:
        list_of_lists.append(list(line)) # Split each line into an array

    return np.array(list_of_lists)


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
    print(type(str_to_array(data)))
    # part_1(real_data)
    # part_2(real_data)

    pass
