"""Test for parser of data_sourcing package

Testing strategy
    provide a sample html file of 1 course
    provide a sample html file of 11 courses
    provide a sample html file of 35 courses
    provide a sample html file of all courses

    partition on the expected course status (refer to data_sourcing.constants.COURE_STATUS_LIST):

    Test large files by verifying the format of every course data in the dictionary
"""
import os
import pytest
import data_sourcing.constants as const
from data_sourcing.parser import parse_html

ABSOLUTE_CWD = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def setup_html_1_course():
    with open(os.path.join(ABSOLUTE_CWD, '../sample_html/one_course_data.html'), 'r') as f:
        html = f.read()
    return html


@pytest.fixture
def setup_html_11_courses():
    with open(os.path.join(ABSOLUTE_CWD, '../sample_html/few_courses_data.html'), 'r') as f:
        html = f.read()
    return html


@pytest.fixture
def setup_html_35_courses():
    with open(os.path.join(ABSOLUTE_CWD, '../sample_html/few_courses_data2.html'), 'r') as f:
        html = f.read()
    return html


@pytest.fixture()
def setup_html_all_courses():
    with open(os.path.join(ABSOLUTE_CWD, '../sample_html/all_courses_data.html'), 'r') as f:
        html = f.read()
    return html


def test_parse_html_1_course(setup_html_1_course):
    data = parse_html(setup_html_1_course)
    assert len(data) == 1
    assert data['37200'] == ['20', '15', '2', 'OPEN']


def test_parse_html_11_courses(setup_html_11_courses):
    data = parse_html(setup_html_11_courses)
    assert len(data) == 11
    assert data['37201'] == ['20', '--', '0', 'CLOSED']
    helper_check_dict_format(data)


def test_parse_html_35_courses(setup_html_35_courses):
    data = parse_html(setup_html_35_courses)
    assert len(data) == 35
    assert data['38609'] == ['25', '5', '20', 'Restricted: See Counselor']
    helper_check_dict_format(data)


def test_parse_html_all_courses(setup_html_all_courses):
    data = parse_html(setup_html_all_courses)
    assert len(data) == 2750
    helper_check_dict_format(data)


def helper_check_dict_format(data: dict):
    """Check if the format of the dictionary is correct

    Args:
        data: dictionary of course data

    Returns:
        True if the format is correct, False otherwise
    """
    for d in data:
        assert len(data[d]) == 4
        assert data[d][0].isdigit()
        assert data[d][1].isdigit() or data[d][1] == '--'
        assert data[d][2].isdigit() or data[d][2] == '--'
        assert any(data[d][3] == s for s in const.COURSE_STATUS_LIST)
