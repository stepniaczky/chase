import os
import logging
import argparse

from .common import reports
from .core import Parser, config, Settings
from .models import Wolf, Sheep

logger = logging.getLogger(__name__)


def simulation(settings: Settings, args: argparse.Namespace) -> None:

    if settings.LOGGING_TYPE != 'NONE' and reports.GLOBALS['LOG_FILE_PATH'] is not None:
        logging.basicConfig(filename=reports.GLOBALS['LOG_FILE_PATH'], level=settings.LOGGING_TYPE,
                            format='%(asctime)s - %(name)s - %(levelname)s : %(message)s')

    logger.debug('Program was executed from the path: %s', os.getcwd())
    logger.debug('Program was initialized with arguments: %s', [
                 f'{arg}: {value}' for arg, value in vars(args).items() if value is not None])
    logger.debug('Program validated all arguments correctly.')
    logger.info('Simulation has started.')

    wolf = Wolf(settings)
    sheep_flock = [Sheep(i + 1, settings)
                   for i in range(settings.SIZE_OF_FLOCK)]
    logger.info('Wolf and sheep flock initialized.')

    for _round in range(1, settings.MAX_NUMBER_OF_ROUNDS+1):
        logger.info('Round %s has started.', _round)

        for sheep in sheep_flock:
            sheep.move()
        logger.info('All of the sheep have moved.')

        wolf.find_nearest_sheep(sheep_flock=sheep_flock)
        wolf.move()
        logger.info('Wolf has moved to: %s.', wolf.pos)

        # INFO
        print()
        print(f'Round: {_round}')
        print(f'Wolf position: ({wolf.pos.x}, {wolf.pos.y})')

        alive_sheep_count = len(
            [sheep for sheep in sheep_flock if sheep.is_alive])
        print(f'Number of alive sheeps: {alive_sheep_count}')

        last_wolf_interaction = 'Chased sheep ID:' if wolf.nearest_sheep.is_alive else 'Eaten sheep ID:'
        logger.info('%s %s', last_wolf_interaction, wolf.nearest_sheep.id)
        print(last_wolf_interaction, wolf.nearest_sheep.id)

        reports.to_json(round_no=_round, wolf_pos=(wolf.pos.x, wolf.pos.y), sheep_pos=[
            (sheep.pos.x, sheep.pos.y) if sheep.is_alive else None for sheep in sheep_flock])
        reports.to_csv(round_noumber=_round,
                       number_of_alive_sheep=alive_sheep_count)

        if not any(sheep.is_alive for sheep in sheep_flock):
            print(_round)
            logger.info('All of the sheep have been eaten in %(_round)s.')
            break

        if settings.WAIT_FOR_USER_INPUT:
            input('Press Enter to continue...')

    logger.info('Simulation has ended.')


if __name__ == '__main__':
    parser = Parser()
    args = parser.get_args()
    settings = config(args)
    reports.report_config(settings)
    simulation(settings, args)
