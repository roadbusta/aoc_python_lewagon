from load_data import get_data,get_test_data
import re
import numpy as np
from itertools import chain
import time



day = '9'
""" Day_09 Pseudocode
Part 1:
1. Write code that converts a string into a list
2. Write code that generates a subsequent list of values with differences

Part 2:
1. Write code that can extrapolate using history and the first number in the list
2. Work it backwards



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
    sum_hist = True
    history_list = [int_list]
    while sum_hist:
        history_list.append(_history(history_list[-1]))
        sum_hist = any(history_list[-1])
    return history_list

def _next_num(int_list):
    history_list = _history_list(int_list)
    next_num = 0
    for i in history_list:
        next_num += i[-1]
    return next_num

# troubleshoot
def _concat(int_list_of_lists):
    solutions = [ i[-1] for i in int_list_of_lists]
    concat_list = [j[0:-1] for j in int_list_of_lists]
    return concat_list, solutions


def part_1(data):
    int_list_of_lists = _string_to_list(data)
    extrapolated_value = 0
    count = 0
    for i in int_list_of_lists:
        extrapolated_value += _next_num(i)
        count += 1
        if count > 198:
            print(count)
            print(extrapolated_value)
            print('\n')

    return extrapolated_value

def part_2():
    pass


if __name__ == "__main__":

 
    int_list_test = [0, 1, 1, 0]
    print(_history_list(int_list_test))
    print(_next_num(int_list_test))
    print('\n')

    # test_data = get_test_data(day)
    # # test_data = get_data(day)
    # int_list_of_lists = _string_to_list(test_data)
    # concat_list, solutions = _concat(int_list_of_lists)
    # for i in range(len(concat_list)):
    #     try:
    #         if _next_num(concat_list[i]) != solutions[i]:
    #             print(_next_num(concat_list[i]))
    #             print(solutions[i])
    #             print(concat_list[i]) 
    #     except:
    #         print('error')

    # print(f'part 1 test solution = {part_1(test_data)}')
    ## Uncomment the lines below when your function passes the test!
    start = time.time()


    real_data = get_data(day)
    print(f'part 1 solution = {part_1(real_data)}')
    end = time.time()
    # print(end - start)
    # print(f'part 2 solution = {part_2(real_data)}')


    pass
