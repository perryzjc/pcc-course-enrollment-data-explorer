"""Parse html data and return a dictionary of course data.

Typical usage example:

    with open('sample_html/all_courses_data.html', 'r') as f:
        html = f.read()
    data = parse_html(html)
"""

from bs4 import BeautifulSoup
import collections.abc
import data_sourcing.constants as const


def parse_html(html: str) -> dict[str, list[str, str, str, str]]:
    """Parse HTML data and return a dictionary of course data.

    Args:
        html: HTML data returned at PCC course schedule page

    Returns:
        A dict mapping keys to the corresponding course data. Each course data is a list
        of Cap, Act, Rem, and status. For example:

        {'course_crn': [num1, num2, num3, course_status],]}
        num1 is Cap, num2 is Act, num3 is Rem. For example:
        {'37200': ['20', '15', '2', 'OPEN']}
    """

    lst_iter = iter(parse_to_raw_list(html))
    course_dict = {}
    try:
        while True:
            status = next_status(lst_iter)
            crn = next_crn(lst_iter)
            course_data = next_course_data(lst_iter)
            course_data.append(status)
            course_dict[crn] = course_data
    except StopIteration:
        pass
    return course_dict


def parse_to_raw_list(html: str) -> list[str, ...]:
    """Parse HTML data and return a list of raw data which is a list of string separated by

    Returns:
        a list of raw data
        For example:

        OPEN
        LL
         31486
          6.0
        Lecture
        M
        T
        W
        Th



        02:10pm - 03:00pm
        IT 140
        20
        4
        8
        Kevin  Keane
        01/09-05/07
        16
    """
    soup = BeautifulSoup(html, 'html.parser')
    raw_data = []
    for tr in soup.body.find_all('tr'):
        lines = tr.text.split('\n')
        if lines is None:
            continue
        for line in lines:
            raw_data.append(line)
    return raw_data


def next_status(data_lst_iter: collections.abc.Iterator) -> str:
    """Return the next course status in iterator and move the iterator to the next data

    There are many status other than OPEN, ClOSED, Waitlisted
    Check data_sourcing.constants.COURSE_STATUS_LIST for more information

    Args:
        data_lst_iter: iterator of the list of data

    Returns:
        first course status appeared in the list

    Raises:
        StopIteration: if there is no more data in the iterator
    """
    assert isinstance(data_lst_iter, collections.abc.Iterator)
    status_found = False
    status = None
    while not status_found:
        item = next(data_lst_iter).strip()
        if any(item == s for s in const.COURSE_STATUS_LIST):
            status_found = True
            status = item

    return status


def next_crn(data_lst_iter: collections.abc.Iterator) -> str:
    """Return the next CRN in iterator and move the iterator to the next data

    Function should be called after next_status() is called.

    Args:
        data_lst_iter: iterator of the list of data

    Returns:
        first CRN appeared in the list

    Raises:
        StopIteration: if there is no more data in the iterator
    """
    assert isinstance(data_lst_iter, collections.abc.Iterator)
    crn_found = False
    crn = None
    while not crn_found:
        item = next(data_lst_iter).strip()
        if len(item) == 5 and item.isdigit():
            crn_found = True
            crn = item

    return crn


def next_course_data(data_lst_iter: collections.abc.Iterator) -> list[str, str, str]:
    """Return the next course data in iterator and move the iterator to the next data

    Course data is a list of size 3, containing Cap, Act and Rem.
    Function should be called after next_crn() is called.

    Args:
        data_lst_iter: iterator of the list of data

    Returns:
        first course data appeared in the list

    Raises:
        StopIteration: if there is no more data in the iterator
    """
    assert isinstance(data_lst_iter, collections.abc.Iterator)

    def move_iter_to_first_course_data() -> str:
        """Move iterator to the second course data and return the first course data

        Returns:
            first course data (Cap). For example, '30'
        """
        while True:
            item = next(data_lst_iter)
            if not is_location(item):
                continue
            else:
                first_course_data = next(data_lst_iter)
                if first_course_data.isdigit():
                    return first_course_data

    course_data = [move_iter_to_first_course_data()]
    for data in range(2):
        course_data.append(next(data_lst_iter))

    return course_data


def is_location(text: str) -> bool:
    """Return True if the string is a location at PCC

    If the text is obtained after calling next_crn(), the returned
    value will be more likely to be a location.

    PCC locations could have Online ZOOM, Online ASYNCH, PCC Rosemead 106,
    C 361, IT 212, etc.

    Args:
        text: string to be checked

    Returns:
        True if the string is a location at PCC, False otherwise
    """
    # based on observation, PCC locations are always at least 5 characters long after stripping
    # , they are not entirely digits
    # , none of them starts with a digit (this case is for time, e.g. 10:30am - 02:05pm)
    stripped_text = text.strip()
    return len(stripped_text) >= 5 \
           and not stripped_text.isdigit() \
           and not stripped_text[0].isdigit()
