"""Output log related information.
"""
import os


LOG_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output/log')
LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, 'log.txt')


def write_to_log_file(log_file_path: str, msg: str):
    """Write additional msg to log file

    Args:
        log_file_path: path of log file
        msg: msg to be written to log file
    """
    with open(log_file_path, 'a') as f:
        f.writelines(msg + '\n')
