"""Main logic for the application.

This module currently only have data_sourcing related functions.
It currently can store the parsed files obtained through PCC course schedule web
in a fixed time interval.
"""

from data_sourcing.requester import get_html_of_course_web
from data_clean.cleaner import clean_html
from data_sourcing.storer import store_data
from data_sourcing.log import write_to_log_file, LOG_FILE_PATH
import time
import config.const_data_sourcing as config


while True:
    html = get_html_of_course_web()
    data = clean_html(html)
    curt_time = time.localtime(time.time())
    store_data(data, curt_time, config.DATA_DATA_SOURCING_FOLDER)
    msg = 'successfully store all course data as a csv file at time: ' + time.strftime('%Y-%m-%d %H:%M:%S', curt_time)
    print(msg)
    write_to_log_file(LOG_FILE_PATH, msg)
    time.sleep(config.REQUEST_INTERVAL)
