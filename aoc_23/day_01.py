from load_data import get_data,get_test_data
from itertools import combinations
import re
day = 1

# Build up a string
# As soon as you can, replace the value with a number

def sum_cal_num(raw_list: list) -> int:
    """Takes in a raw list of numbers and letters. On each line, the calibration
    value can be found by combining the first digit and the last digit (in that
    order) to form a single two-digit number. This then summs the list of two-
    digit numbers
    """
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

def true_cal_num(cal_str: str) -> str:
    """ Takes in a calibration string, and returns the entire number
    """
    search_list = ['zero', 'one', 'two','three', 'four', 'five', 'six', 'seven',
                   'eight', 'nine','0','1','2','3','4','5','6','7','8','9']
    # Number dictionary
    num_dict = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
    }
    # Create an empty search dictionary
    search_dict = {}
    for test_sub in search_list:
        res = [i for i in range(len(cal_str)) if cal_str.startswith(test_sub, i)]
        search_dict[test_sub] = res


    # clean the dictionary
    clean_dict = dict(search_dict)
    for key, value in search_dict.items():
        if len(value)==0:
            clean_dict.pop(key)

    # invert the dictionary
    inv_dict = {}
    for key, value in clean_dict.items():
        for v in value:
            if key in num_dict.keys():
                key = num_dict[key]

            inv_dict[v] = key

    # Sort the dictionary
    sorted_dict = {k: v for k, v in sorted(inv_dict.items(), key=lambda item: item[0])}

    # Extract numbers into a list
    number_list = [v for k,v in sorted_dict.items()]

    #Join to a string and strip
    number_string = "".join(number_list).strip()

    return number_string




def part_1(data: str) -> int:
    """ In each line, remove all the letters to leave behind the numbers.
    Return the sum of the numbers as the output
    """
    # split data into vector/list of numbers
    raw_list = data.strip().split('\n')

    return sum_cal_num(raw_list) # Generate calibrated numbers and sum


def part_2(data: str) ->int:
    """ Takes in a data string and converts digits represented as words into
    numbers before then generating the calibration numbers and summing them
    """

    # strip, lower then split data into vector/list of numbers
    raw_list = data.strip().lower().split('\n')

    # Create an empty converted list
    converted_list = []
    for item in raw_list:
        converted_list.append(true_cal_num(item))

    return sum_cal_num(converted_list) # Generate calibrated numbers and sum


## Uncomment the lines below when your function passes the test!
real_data = get_data(day)
print(f'part 1 solution = {part_1(real_data)}')
print(f'part 2 solution = {part_2(real_data)}')

if __name__ == "__main__":
    # data_1 = get_test_data(1)
    # part_1(data_1)


    # data_2 = get_test_data('1-2')
    # part_2(data_2)

    # print(true_cal_num('two1ninetwo'))
    pass
