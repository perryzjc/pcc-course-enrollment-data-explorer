"""Access PCC course schedule web and return html data

"""

import requests
from backend.config import config_data_sourcing as config


def get_html_of_course_web() -> str:
    """Return html data of PCC course schedule web
    """
    response = requests.request("POST",
                                config.ALL_COURSES_URL,
                                headers=config.HEADER,
                                data=config.POST_DATA)
    return response.text
