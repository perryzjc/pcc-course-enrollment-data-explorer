"""Store parsed data as a csv file

The file name is based on current time parameter.
Files are stored in different folder based on current time. Folders are based
on year, month, and day.

Typical usage example:

    store_data(course_dict_data, curr_time)
"""

import csv
import os
import time
import constants


def store_data(data: dict[str, list[str, str, str]],
               curr_time: time.struct_time
) -> None:
    """Store parsed data as a csv file

    The file name of the csv file is the time the original html file is obtained,
    formatted as YYYY-MM-DD-HH-MM-SS.
    Files are stored in different folder based on the day the file is obtained.
    Each day folder are stored in different month folder.
    Each month folder are stored in different year folder.

    Args:
        data: Parsed data from parser.parse_html()
        curr_time: time.struct_time object of the time the original html file is obtained
    """
    target_folder = create_folder_needed_if_not_exists(curr_time)
    file_name = time.strftime('%Y-%m-%d-%H-%M-%S', curr_time) + '.csv'
    file_path = os.path.join(target_folder, file_name)
    with open(os.path.join(file_path), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['CRN', 'Cap', 'Act', 'Rem', 'Status'])
        for crn in data:
            writer.writerow([crn] + data[crn])


def create_folder_needed_if_not_exists(target_time: time.struct_time) -> str:
    """Create folder structure needed and return the path of the resulting folder

    The folder is created based on the target_time parameter.
    The folder is created in the following format:
    output/year/month/day
    If the folder already exists, nothing will be done.

    Args:
        target_time: target time to create folder for

    Returns:
        The path of the folder created based on the target time precise to the day.
        For example:

        output/2023/1/13
    """
    def curr_year() -> str:
        """Return the current year in string format
        """
        return str(target_time.tm_year)

    def curr_month() -> str:
        """Return the current month in string format
        """
        return str(target_time.tm_mon)

    def curr_day() -> str:
        """Return the current day in string format
        """
        return str(target_time.tm_mday)

    def create_folder_if_not_exists(folder_path: str) -> None:
        """Create folder if it does not exist
        """
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    year_folder_path = os.path.join(constants.OUTPUT_FOLDER, curr_year())
    create_folder_if_not_exists(year_folder_path)
    month_folder_path = os.path.join(year_folder_path, curr_month())
    create_folder_if_not_exists(month_folder_path)
    day_folder_path = os.path.join(month_folder_path, curr_day())
    create_folder_if_not_exists(day_folder_path)
    return day_folder_path