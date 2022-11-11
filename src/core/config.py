import os

from dataclasses import dataclass, field
from configparser import ConfigParser


@dataclass
class Settings:
    MAX_NUMBER_OF_ROUNDS: int = 50
    SIZE_OF_FLOCK: int = 15

    INIT_POS_LIMIT: float = field(default=10.0, init=False)
    SHEEP_MOVE_DIST: float = field(default=0.5, init=False)
    WOLF_MOVE_DIST: float = field(default=1.0, init=False)

    WOLF_INIT_POS_X: float = field(default=0.000, init=False)
    WOLF_INIT_POS_Y: float = field(default=0.000, init=False)

    CONFIG_FILE_PATH: str = 'NONE'
    SUBDIRECTORY_PATH: str = field(default='.')
    LOGGING_TYPE: str = 'NONE'

    WAIT_FOR_USER_INPUT: bool = False

    def __post_init__(self):
        if self.CONFIG_FILE_PATH != 'NONE':
            self.load_config_file()

        if self.SUBDIRECTORY_PATH != '.':
            if os.path.exists(self.SUBDIRECTORY_PATH) is False:
                os.makedirs(self.SUBDIRECTORY_PATH)

    def load_config_file(self):
        config = ConfigParser()
        config.read(self.CONFIG_FILE_PATH)

        try:
            if config == []:
                raise FileNotFoundError

            for category in config.values():
                for value in category.values():
                    if value <= 0:
                        raise AttributeError

            self.INIT_POS_LIMIT = float(config['Terrain']['InitPosLimit'])
            self.SHEEP_MOVE_DIST = float(config['Movement']['SheepMoveDist'])
            self.WOLF_MOVE_DIST = float(config['Movement']['WolfMoveDist'])

        except KeyError:
            print('Config file is missing some parameters!')
        except ValueError:
            print('All values in config file must be numbers!')
        except FileNotFoundError:
            print('Config file not found!')
        except AttributeError:
            print('All values in config file must be positive!')
