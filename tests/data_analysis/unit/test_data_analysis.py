"""Test data_analysis package
"""
import os
import pytest
from data_analysis.data_analysis import get_all_course_status


SOURCE_HTML_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data_sourcing/sample_html')
SOURCE_HTML_FILE_1_COURSE_PATH = os.path.join(SOURCE_HTML_DIR_PATH, 'one_course_data.html')
SOURCE_HTML_FILE_11_COURSES_PATH = os.path.join(SOURCE_HTML_DIR_PATH, 'few_courses_data.html')
SOURCE_HTML_FILE_all_COURSES_PATH1 = os.path.join(SOURCE_HTML_DIR_PATH, 'all_courses_data.html')
SOURCE_HTML_FILE_all_COURSES_PATH2 = os.path.join(SOURCE_HTML_DIR_PATH, 'all_courses_data2.html')


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


def output_all_courses_data():
    """Output all courses status as a set to a file
    >>> output_all_courses_data()
    """
    import csv
    with open(SOURCE_HTML_FILE_all_COURSES_PATH1, 'r') as f:
        html1 = f.read()
    with open(SOURCE_HTML_FILE_all_COURSES_PATH2, 'r') as f:
        html2 = f.read()
    status_set1 = get_all_course_status(html1)
    status_set2 = get_all_course_status(html2)
    target_output_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.pytest_cache')
    target_output_file_path1 = os.path.join(target_output_dir_path, 'all_courses_status1.csv')
    target_output_file_path2 = os.path.join(target_output_dir_path, 'all_courses_status2.csv')
    if not os.path.exists(target_output_dir_path):
        os.mkdir(target_output_dir_path)
    with open(target_output_file_path1, 'w') as f:
        writer = csv.writer(f)
        for status in status_set1:
            writer.writerow([status])
    with open(target_output_file_path2, 'w') as f:
        writer = csv.writer(f)
        for status in status_set2:
            writer.writerow([status])

