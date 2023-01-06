import argparse

from core import Settings
from common import reports

proper_keys = {
    'config': 'CONFIG_FILE_PATH',
    'dir': 'SUBDIRECTORY_PATH',
    'log': 'LOGGING_TYPE',
    'rounds': 'MAX_NUMBER_OF_ROUNDS',
    'sheep': 'SIZE_OF_FLOCK',
    'wait': 'WAIT_FOR_USER_INPUT'
}


def config(args: argparse.Namespace = None) -> Settings:

    settings_params = vars(args)
    settings_params = {proper_keys[key]: value for key,
                       value in settings_params.items() if value is not None}

    for key in settings_params:
        k = settings_params[key]
        if isinstance(k, int) and k is not True and k is not False:
            if settings_params[key] <= 0:
                raise AttributeError(f'Value of {key} must be positive!')

    if 'LOGGING_TYPE' in settings_params:
        settings_params['LOGGING_TYPE'] = settings_params['LOGGING_TYPE'].upper()
        if settings_params['LOGGING_TYPE'] not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            raise AttributeError('Logging type must be one of: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL".')

    return Settings(**settings_params)
