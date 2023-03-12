"""Test for requester of data_sourcing package

Testing strategy

partition on the data:
    not empty
    contain CLOSED word
    contain OPEN word
    contain Waitlisted word
    should contain many lines

This strategy does not cover every possibility,
but it is nearly sufficient to test the data of the function.
"""
import pytest
from backend.data_sourcing.requester import get_html_of_course_web


html_requested = False
returned_html = None


@pytest.fixture
def setup_html_data():
    global html_requested
    global returned_html
    if not html_requested:
        returned_html = get_html_of_course_web()
        html_requested = True
    return returned_html


def test_not_empy(setup_html_data):
    assert setup_html_data is not None
    assert len(setup_html_data) > 0


def test_contain_CLOSED_word(setup_html_data):
    assert 'CLOSED' in setup_html_data


def test_contain_OPEN_word(setup_html_data):
    assert 'OPEN' in setup_html_data


def test_contain_Waitlisted_word(setup_html_data):
    assert 'Waitlisted' in setup_html_data


def test_contain_many_lines(setup_html_data):
    assert len(setup_html_data.splitlines()) > 50000
