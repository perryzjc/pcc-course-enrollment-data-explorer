"""Access PCC course schedule web and return html data

"""

import requests
from backend.config import config_data_sourcing as config


def get_html_of_course_web(term: str, year: str) -> str:
    """Return html data of PCC course schedule web
    """
    if term not in config.TERM_MAP:
        raise ValueError('Invalid term')
    if not year.isdigit():
        raise ValueError('Invalid year')
    term_code = year + config.TERM_MAP[term]
    term_desc = term + '+' + year
    url = config.ALL_COURSES_URL.replace(config.DUMMY_TERM_CODE, term_code).replace(config.DUMMY_TERM_DESC, term_desc)
    response = requests.request("POST",
                                url,
                                headers=config.HEADER,
                                data=config.POST_DATA)
    return response.text
