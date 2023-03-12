"""Configurations for logging
"""
import os

LOG_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/log')
LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, 'log.txt')
ERR_LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, 'error_log.txt')
