from load_data import get_data,get_test_data
from itertools import combinations
import re
day = '01'


def part_1(data: str) -> int:
    """ In each line, remove all the letters to leave behind the numbers.
    Return the sum of the numbers as the output
    """
    # split data into vector/list of numbers
    raw_list = data.strip().split('\n')

    # Create an empty list
    calibration_value = []

    # Iterate through each line of the document
    for line in raw_list:
        # Remove letters, convert remaining number into an integer
        f = filter(str.isdigit,line) # Filter out number
        calibration_str = "".join(f).strip()
        if len(calibration_str) == 1:
            # If the string has a length of 1, clone the digit
            calibration_str += calibration_str

        elif len(calibration_str) > 2:
            # If the string of numbers is 3, take the first and last number
            calibration_str = calibration_str[0] + calibration_str[-1]

        calibration_number = int(calibration_str) # Convert to an integer
        calibration_value.append(calibration_number) # Add number to list

    return sum(calibration_value) # Return summed list

### Uncomment the lines below when your function passes the test!
# raw_data = get_data(day)
# print(f'part 1 solution = {part_1(raw_data)}')

# def part_2(data):
#     pass

if __name__ == "__main__":
    data = get_test_data(1)
    part_1(data)
