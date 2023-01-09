"""Access PCC course schedule web and return html data

"""

import requests
import data_sourcing.constants as const


def get_html_of_course_web() -> str:
    """Return html data of PCC course schedule web
    """
    response = requests.request("POST",
                                const.ALL_COURSES_URL,
                                headers=const.HEADER,
                                data=const.POST_DATA)
    return response.text
