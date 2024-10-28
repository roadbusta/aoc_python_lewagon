from load_data import get_data,get_test_data
import re
import numpy as np
from itertools import chain
import time



day = '9'
""" Day_09 Pseudocode
Step 1:
1. Write code that converts a string into a list
2. Write code that generates a subsequent list of values with differences



"""
def _string_to_list(data):
    string_list = data.split('\n')
    sub_string_list = []
    for i in string_list:
        split_list = i.split(' ')
        i_list = []
        for j in split_list:
            i_list.append(int(j))
        sub_string_list.append(i_list)

    return sub_string_list

def _history(int_list):
    history = []
    for i in range(len(int_list)):
        if i < len(int_list) - 1:
            history.append(int_list[i+1] - int_list[i])
    return history

def _history_list(int_list):
    sum_hist = 1
    history_list = [int_list]
    while sum_hist > 0:
        history_list.append(_history(history_list[-1]))
        sum_hist = sum(history_list[-1])
    return history_list

def _next_num(int_list):
    history_list = _history_list(int_list)
    next_num = 0
    for i in history_list:
        next_num += i[-1]
    return next_num


def part_1(data):
    int_list_of_lists = _string_to_list(data)
    extrapolated_value = 0
    for i in int_list_of_lists:
        extrapolated_value += _next_num(i)

    return extrapolated_value

def part_2():
    pass


if __name__ == "__main__":


    ## Uncomment the lines below when your function passes the test!
    start = time.time()


    real_data = get_data(day)
    print(f'part 1 solution = {part_1(real_data)}')
    end = time.time()
    print(end - start)
    # print(f'part 2 solution = {part_2(real_data)}')


    pass
