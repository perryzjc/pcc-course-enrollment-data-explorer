"""Output log related information.
"""
import os
from backend.config.config_log import LOG_FILE_PATH, ERR_LOG_FILE_PATH


def write_to_log_file(msg: str):
    """Write additional msg to log file
    """
    write_to_file(LOG_FILE_PATH, msg)


def write_to_error_log_file(msg: str):
    """Write additional msg to error log file

    """
    write_to_file(ERR_LOG_FILE_PATH, msg)


def write_to_file(file_path: str, content: str):
    """Write additional content to file
    """
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
    else:
        with open(file_path, 'a') as f:
            f.write(content)
