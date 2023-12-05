from aoc_23.day_05 import _parse_source_data, _positive_int
from aoc_23.load_data import get_test_data
import numpy as np


test_data = get_test_data(5)
parsed_data = _parse_source_data(test_data)
seeds = parsed_data['seeds']
seed_soil = parsed_data['seed_soil']
soil_fert = parsed_data['soil_fert']
fert_water = parsed_data['fert_water']
water_light = parsed_data['water_light']
light_temp = parsed_data['light_temp']
temp_humid = parsed_data['temp_humid']
humid_loc = parsed_data['humid_loc']
expected_result_part_1 = 35
expected_result_part_2 = None


def test_part_1():
    assert type(test_data) == str # Check data type of test data
    assert type(parsed_data) == dict # Confirm data type of parsed data
    assert len(parsed_data) == 8 # Confirm correct number of values in dictionary
    assert type(seeds) == list # Confirm data type of seeds list
    assert _positive_int(seeds) == True # Confirm that data types are positive int



    pass


def test_part_2():
   pass
