"""Test data_analysis package
"""
import os
import pytest
from data_analysis.data_analysis import get_all_course_status


SOURCE_HTML_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data_sourcing/sample_html')
SOURCE_HTML_FILE_1_COURSE_PATH = os.path.join(SOURCE_HTML_DIR_PATH, 'one_course_data.html')
SOURCE_HTML_FILE_11_COURSES_PATH = os.path.join(SOURCE_HTML_DIR_PATH, 'few_courses_data.html')


@pytest.fixture
def setup_data1():
    with open(SOURCE_HTML_FILE_1_COURSE_PATH, 'r') as f:
        html = f.read()
    return html


@pytest.fixture
def setup_data11():
    with open(SOURCE_HTML_FILE_11_COURSES_PATH, 'r') as f:
        html = f.read()
    return html


def test_parse_html_1_course(setup_data1):
    status_set = get_all_course_status(setup_data1)
    assert len(status_set) == 1
    assert 'OPEN' in status_set


def test_parse_html_11_course(setup_data11):
    """Test get_all_course_status() with 11 courses

    This file only has 2 statuses: OPEN and CLOSED
    """
    status_set = get_all_course_status(setup_data11)
    assert len(status_set) == 2
    assert 'OPEN' in status_set
    assert 'CLOSED' in status_set
