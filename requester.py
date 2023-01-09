"""Access PCC course schedule web and return html data

"""

import requests
import constants


def get_html_of_course_web() -> str:
    """Return html data of PCC course schedule web
    """
    response = requests.request("POST",
                                constants.ALL_COURSES_URL,
                                headers=constants.HEADER,
                                data=constants.POST_DATA)
    return response.text
