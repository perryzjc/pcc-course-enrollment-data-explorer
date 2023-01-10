"""Main logic for the application.

This module currently only have data_sourcing related functions.
It currently can store the parsed files obtained through PCC course schedule web
in a fixed time interval.
"""

from data_sourcing.requester import get_html_of_course_web
from data_sourcing.parser import parse_html
from data_sourcing.storer import store_data
import time
import data_sourcing.constants as constants
import os


while True:
    html = get_html_of_course_web()
    data = parse_html(html)
    curt_time = time.localtime(time.time())
    store_data(data, curt_time, os.path.join(os.path.dirname(os.path.abspath(__file__)), constants.OUTPUT_DATA_SOURCING_FOLDER))
    print('successfully store a data file at time: ', time.strftime('%Y-%m-%d %H:%M:%S', curt_time))
    time.sleep(constants.REQUEST_INTERVAL)
