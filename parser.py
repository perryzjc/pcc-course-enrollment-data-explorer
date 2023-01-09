"""Parse html data and return a dictionary of course data.

Typical usage example:

    with open('sample_html/all_courses_data.html', 'r') as f:
        html = f.read()
    data = parse_html(html)
"""

from bs4 import BeautifulSoup
import collections.abc


def parse_html(html: str) -> dict[str, list[str, str, str]]:
    """Parse HTML data and return a dictionary of course data.

    Args:
        html: HTML data returned at PCC course schedule page

    Returns:
        A dict mapping keys to the corresponding course data. Each course data is a list
        of Cap, Act, Rem, and status. For example:

        {'course_crn': [num1, num2, num3]}
        num1 is Cap, num2 is Act, num3 is Rem
    >>> with open('sample_html/one_course_data.html', 'r') as f:
    ...     html_data = f.read()
    ...     parse_html(html_data)
    {'37200': ['20', '15', '2', 'OPEN']}
    """
    def parse_to_raw_list():
        """Parse HTML data and return a list of raw data which is a list of string separated by

        @return: list of raw data
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

    lst_iter = iter(parse_to_raw_list())
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


def next_status(data_lst_iter: collections.abc.Iterator) -> str:
    """Return the next course status in iterator and move the iterator to the next data

    There are 3 status: OPEN, ClOSED, Waitlisted

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
        if item == 'OPEN' or item == 'CLOSED' or item == 'Waitlisted':
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
    offset = 12
    # course data is 12 \n away from CRN
    for _ in range(offset - 1):
        next(data_lst_iter)

    course_data = []
    for data in range(3):
        course_data.append(next(data_lst_iter))

    return course_data
