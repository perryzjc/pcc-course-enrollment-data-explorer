"""Test integration of data_sourcing package

Test strategy

Partition on the integration of the three modules:
    call parser and storer (only this implementation is provided for current version)
        partition on the sample data:
            first sample data (all courses)
            second sample data (all courses)
    call parser and requester
    call requester, parser and storer
"""
from data_clean.cleaner import clean_html
from data_sourcing.storer import store_data
import os
import time
import pytest

ABSOLUTE_CWD = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR_NAME = '.pytest_cache'
CACHE_DIR = os.path.join(ABSOLUTE_CWD, CACHE_DIR_NAME)


@pytest.fixture
def setup_html_data1():
    """Fixture for testing parser and storer without requester
    """
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)
    with open(os.path.join(ABSOLUTE_CWD, '../sample_html/all_courses_data.html'), 'r') as f:
        html = f.read()
    return html


@pytest.fixture
def setup_html_data2():
    """Fixture for testing parser and storer without requester
    """
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)
    with open(os.path.join(ABSOLUTE_CWD, '../sample_html/all_courses_data2.html'), 'r') as f:
        html = f.read()
    return html


def test_integration_parser_storer1(setup_html_data1):
    """Test the integration of parser and storer by first sample data (all courses)

    The file should be successfully stored at the correct location.
    The content of file should have correct number of data
    """
    data = clean_html(setup_html_data1)
    store_data(data,
               time.struct_time((2023, 1, 13, 12, 34, 56, 0, 0, 0)),
               CACHE_DIR)
    target_file_path = os.path.join(CACHE_DIR,
                                    '2023', '01', '13', '2023-01-13-12-34-56.csv')
    assert os.path.exists(target_file_path)
    with open(target_file_path, 'r') as f:
        assert f.read().count('\n') == 2750 + 1


def test_integration_parser_storer2(setup_html_data2):
    """Test the integration of parser and storer by second sample data (all courses)

    The file should be successfully stored at the correct location.
    The content of file should have correct number of data
    """
    data = clean_html(setup_html_data2)
    store_data(data,
               time.struct_time((2026, 6, 6, 6, 6, 6, 0, 0, 0)),
               CACHE_DIR)
    target_file_path = os.path.join(CACHE_DIR,
                                    '2026', '06', '06', '2026-06-06-06-06-06.csv')
    assert os.path.exists(target_file_path)
    with open(target_file_path, 'r') as f:
        assert f.read().count('\n') == 2751 + 1
