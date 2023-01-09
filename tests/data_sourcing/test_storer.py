"""Test for storer of data_sourcing package

Testing strategy

partition on the input:
    curr_time1
    curr_time2

Two sample time should have successfully stored data at the correct location.
"""
import os.path
import time

import pytest
from data_sourcing.storer import store_data


@pytest.fixture
def setup_data():
    sample_dict = {'32767': ['30', '12', '18', 'OPEN']}
    target_base_path = '.pytest_cache'
    return [sample_dict, target_base_path]


def test_curr_time1(setup_data):
    sample_dict = setup_data[0]
    curr_time = time.struct_time((2023, 1, 13, 12, 34, 56, 0, 0, 0))
    target_base_path = setup_data[1]
    store_data(sample_dict, curr_time, target_base_path)
    assert os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       target_base_path,
                                       '2023', '1', '13', '2023-1-13-12-34-56.csv'))
