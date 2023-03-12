"""Analyze PCC course data based on html data or parsed data
"""

from data_clean.cleaner import parse_to_raw_list, next_status


def get_all_course_status(html: str) -> set[str]:
    """Return a list of all unrepeated course status in html data

    Args:
        html: html data of PCC course schedule web

    Returns:
        a list of all unrepeated course status
    """
    assert isinstance(html, str)
    lst_iter = iter(parse_to_raw_list(html))
    status_set = set()
    try:
        status_set = set()
        while True:
            status = next_status(lst_iter)
            status_set.add(status)
    except StopIteration:
        pass
    return status_set
