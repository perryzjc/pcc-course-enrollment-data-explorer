from bs4 import BeautifulSoup
import collections.abc


def parse_html(html):
    """
    Parse HTML data and return a dictionary of course data.
    @param html: HTML data returned at PCC course schedule page
    @return: dictionary of course data which is a dictionary of list
    e.g.: {'course_crn': [num1, num2, num3]}
    num1 is Cap, num2 is Act, num3 is Rem
    >>> with open('sample_html/one_course_data.html', 'r') as f:
    ...     html_data = f.read()
    ...     parse_html(html_data)
    {'37200': ['20', '15', '2']}
    """
    def parse_to_raw_list():
        """
        Parse HTML data and return a list of raw data which is a list of string separated by \n
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
            crn = next_crn(lst_iter)
            course_data = next_course_data(lst_iter)
            course_dict[crn] = course_data
    except StopIteration:
        pass
    return course_dict


def next_crn(data_lst_iter):
    """
    Return the next CRN in iterator and move the iterator to the next data
    @param data_lst_iter: iterator of the list of data
    @return: first CRN appeared in the iterator
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


def next_course_data(data_lst_iter):
    """
    Return the next course data in iterator and move the iterator to the next data
    Course data is a list of Cap, Act, Rem.
    Function should be called after next_crn() is called.
    @param data_lst_iter: iterator of the list of data
    @return: first course data appeared in the list
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
