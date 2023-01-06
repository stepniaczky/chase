import os
import configparser

from dataclasses import dataclass

@dataclass
class Settings:
    MAX_NUMBER_OF_ROUNDS: int = 50
    SIZE_OF_FLOCK: int = 15

    INIT_POS_LIMIT: float = 10.0
    SHEEP_MOVE_DIST: float = 0.5
    WOLF_MOVE_DIST: float = 1.0

    WOLF_INIT_POS_X: float = 0.000
    WOLF_INIT_POS_Y: float = 0.000

    CONFIG_FILE_PATH: str = 'NONE'
    LOGGING_TYPE: str = 'NONE'

    SUBDIRECTORY_PATH: str = '.'
    JSON_FILE_NAME: str = 'pos.json'
    CSV_FILE_NAME: str = 'alive.csv'
    LOG_FILE_NAME: str = 'chase.log'

    WAIT_FOR_USER_INPUT: bool = False

    def __post_init__(self):
        if self.CONFIG_FILE_PATH != 'NONE':
            self.load_config_file()

        if self.SUBDIRECTORY_PATH != '.':
            if os.path.exists(self.SUBDIRECTORY_PATH) is False:
                try:
                    os.makedirs(self.SUBDIRECTORY_PATH)
                except OSError:
                    raise SystemExit(f'Could not create directory {self.SUBDIRECTORY_PATH}!')

    def load_config_file(self):
        config = configparser.ConfigParser()
        try:
            config.read(self.CONFIG_FILE_PATH)
            if config == []:
                raise FileNotFoundError

            for category in config.values():
                for value in category.values():
                    if float(value) <= 0:
                        raise AttributeError

            self.INIT_POS_LIMIT = float(config['Terrain']['InitPosLimit'])
            self.SHEEP_MOVE_DIST = float(config['Movement']['SheepMoveDist'])
            self.WOLF_MOVE_DIST = float(config['Movement']['WolfMoveDist'])

        except KeyError:
            raise SystemExit('Config file is missing some parameters!')
        except ValueError:
            raise SystemExit('All values in config file must be numbers!')
        except FileNotFoundError:
            raise SystemExit('Config file not found!')
        except AttributeError:
            raise SystemExit('All values in config file must be positive!')
        except configparser.Error:
            raise configparser.Error(f'Config file {self.CONFIG_FILE_PATH} is not valid!')
