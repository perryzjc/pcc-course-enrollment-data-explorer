from parser import parse_html
from storer import store_data
from requester import get_html_of_course_web
import time
import constants


while True:
    html = get_html_of_course_web()
    data = parse_html(html)
    curt_time = time.localtime(time.time())
    store_data(data, curt_time)
    time.sleep(constants.REQUEST_INTERVAL)
