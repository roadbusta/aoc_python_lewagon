from aoc_23.day_05 import _parse_source_data, _positive_int
from aoc_23.load_data import get_test_data
import numpy as np


test_data = get_test_data(5)
parsed_data = _parse_source_data(test_data)
seeds = parsed_data['seeds']
seed_soil = parsed_data['seed-to-soil']
soil_fert = parsed_data['soil-to-fertilizer']
fert_water = parsed_data['fertilizer-to-water']
water_light = parsed_data['water-to-light']
light_temp = parsed_data['light-to-temperature']
temp_humid = parsed_data['temperature-to-humidity']
humid_loc = parsed_data['humidity-to-location']
expected_result_part_1 = 35
expected_result_part_2 = None


def test_part_1():
    assert type(test_data) == str # Check data type of test data

    assert type(parsed_data) == dict # Confirm data type of parsed data
    assert len(parsed_data) == 8 # Confirm correct number of values in dictionary

    assert type(seeds) == list # Confirm data type of seeds list
    assert _positive_int(seeds) == True # Confirm that data types are positive int

    assert type(seed_soil) == list # Confirm data type of seeds list
    assert _positive_int([seed_soil[0]['source']]) == True # Confirm that data types are positive int

    assert type(soil_fert) == list # Confirm data type of seeds list
    assert _positive_int([soil_fert[0]['dest']]) == True # Confirm that data types are positive int







    pass


def test_part_2():
   pass
