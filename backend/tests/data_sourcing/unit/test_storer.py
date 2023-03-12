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
from backend.data_sourcing.storer import store_data


ABSOLUTE_CWD = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(ABSOLUTE_CWD, '.pytest_cache')


@pytest.fixture
def setup_data():
    sample_dict = {'32767': ['30', '12', '18', 'OPEN']}
    target_base_path = '.pytest_cache'
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)
    return [sample_dict, target_base_path]


def test_curr_time1(setup_data):
    store_data(setup_data[0],
               time.struct_time((2023, 1, 13, 12, 34, 56, 0, 0, 0)),
               setup_data[1])
    assert os.path.exists(os.path.join(ABSOLUTE_CWD,
                                       setup_data[1],
                                       '2023', '01', '13', '2023-01-13-12-34-56.csv'))


def test_curr_time2(setup_data):
    store_data(setup_data[0],
               time.struct_time((2026, 6, 6, 6, 6, 6, 0, 0, 0)),
               setup_data[1])
    assert os.path.exists(os.path.join(ABSOLUTE_CWD,
                                        setup_data[1],
                                        '2026', '06', '06', '2026-06-06-06-06-06.csv'))
