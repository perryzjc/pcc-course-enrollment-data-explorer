"""Test for parser of data_sourcing package

Testing strategy
    provide a sample html file of 1 course
    provide a sample html file of 11 courses
    provide a sample html file of all courses
"""
import os
import pytest
from data_sourcing.parser import parse_html

ABSOLUTE_CWD = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def setup_html_1_course():
    with open(os.path.join(ABSOLUTE_CWD, 'sample_html/one_course_data.html'), 'r') as f:
        html = f.read()
    return html


@pytest.fixture
def setup_html_11_courses():
    with open(os.path.join(ABSOLUTE_CWD, 'sample_html/few_courses_data.html'), 'r') as f:
        html = f.read()
    return html


@pytest.fixture()
def setup_html_all_courses():
    with open(os.path.join(ABSOLUTE_CWD, 'sample_html/all_courses_data.html'), 'r') as f:
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


def test_parse_html_all_courses(setup_html_all_courses):
    data = parse_html(setup_html_all_courses)
    assert len(data) == 2340
    assert data['37201'] == ['20', '--', '0', 'CLOSED']
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
        assert data[d][2].isdigit()
        assert data[d][3] == 'OPEN' or data[d][3] == 'CLOSED' or data[d][3] == 'Waitlisted'
