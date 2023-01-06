import os
import csv
import json
import logging

from chase.core import Settings

GLOBALS = {
    'CSV_FILE_PATH': None,
    'JSON_FILE_PATH': None,
    'LOG_FILE_PATH': None
}

logger = logging.getLogger(__name__)


def report_config(settings: Settings) -> None:
    logger.debug('report_config() called')

    GLOBALS['CSV_FILE_PATH'] = os.path.join(
        settings.SUBDIRECTORY_PATH, settings.CSV_FILE_NAME)
    GLOBALS['JSON_FILE_PATH'] = os.path.join(
        settings.SUBDIRECTORY_PATH, settings.JSON_FILE_NAME)
    GLOBALS['LOG_FILE_PATH'] = os.path.join(
        settings.SUBDIRECTORY_PATH, settings.LOG_FILE_NAME)

    logger.debug('report_config() correctly set the global variables')


def to_csv(**kwargs) -> None:
    logger.debug('to_csv() called')

    file = GLOBALS['CSV_FILE_PATH']
    if file is None:
        logger.error('Cannot report to CSV file. Missing CSV file path!')
        return

    file_open_mode = 'a' if os.path.exists(file) else 'w'
    try:
        with open(file, file_open_mode, newline='', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=kwargs.keys())

            if file_open_mode == 'w':
                writer.writeheader()

            writer.writerow(kwargs)
    except IOError:
        logger.critical(
            'Cannot report to CSV file. Error while writing to file!')
    except Exception as e:
        logger.critical('Cannot report to CSV file. Unknown error: %s', e)

    logger.debug('to_csv() correctly saved the data in a file: %s', file)


def to_json(**kwargs) -> None:
    logger.debug('to_json() called')

    file = GLOBALS['JSON_FILE_PATH']
    if file is None:
        logger.error('Cannot report to JSON file. Missing JSON file path!')
        return

    file_open_mode = 'a' if os.path.exists(file) else 'w'
    obj_arr = []

    try:
        if file_open_mode == 'a':
            with open(file, encoding='UTF-8') as f:
                obj_arr = json.load(f)

        with open(file, 'w', encoding='UTF-8') as f:
            obj_arr.append(kwargs)
            json.dump(obj_arr, f, indent=2, separators=(',', ': '))
    except IOError:
        logger.critical(
            'Cannot report to JSON file. Error while writing to file!')
    except Exception as e:
        logger.critical('Cannot report to JSON file. Unknown error: %s', e)

    logger.debug('to_json() correctly saved the data in a file: %s', file)
