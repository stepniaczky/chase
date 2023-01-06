import random
import logging

from dataclasses import dataclass, field

from models.point import Point
from core.settings import Settings

logger = logging.getLogger(__name__)


@dataclass
class Sheep:
    id: int
    pos: Point = field(init=False)
    move_dist: float = field(init=False)
    is_alive: bool = field(init=False, default=True)

    def __init__(self, id: int, settings: Settings):
        self.id = id
        self.move_dist = settings.SHEEP_MOVE_DIST
        self.pos = Point(x=round(random.uniform(-settings.INIT_POS_LIMIT, settings.INIT_POS_LIMIT), 1),
                         y=round(random.uniform(-settings.INIT_POS_LIMIT, settings.INIT_POS_LIMIT), 1))

        logger.debug('Sheep.__init__() called with pos: %s', self.pos)

    def move(self):
        logger.debug('move() called for id: %s with start pos: %s', self.id, self.pos)

        axis: list = ['x', 'y']
        dist: list = [-self.move_dist, self.move_dist]

        rand_axis = random.choice(axis)
        rand_dist = random.choice(dist)

        attr_value = getattr(self.pos, rand_axis)
        setattr(self.pos, rand_axis, round(attr_value + rand_dist, 1))

        logger.debug('move() completed for id: %s with current pos: %s', self.id, self.pos)
