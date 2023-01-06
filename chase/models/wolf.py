import math
import logging

from typing import List
from dataclasses import dataclass, field

from chase.models.point import Point
from chase.models.sheep import Sheep
from chase.core.settings import Settings

logger = logging.getLogger(__name__)


@dataclass
class Wolf:
    pos: Point = field(init=False)
    move_dist: float = field(init=False)
    nearest_sheep: Sheep = field(init=False)

    def __init__(self, settings: Settings):
        self.move_dist = settings.WOLF_MOVE_DIST
        self.pos = Point(x=settings.WOLF_INIT_POS_X, y=settings.WOLF_INIT_POS_Y)
        logger.debug('Wolf.__init__() called with pos: %s', self.pos)

    def find_nearest_sheep(self, sheep_flock: List[Sheep]):
        logger.debug('find_nearest_sheep() called')

        filtered_flock = [sheep for sheep in sheep_flock if sheep.is_alive]
        sorted_flock = sorted(filtered_flock, key=self.get_distance)
        self.nearest_sheep = sorted_flock[0]
        
        logger.debug('find_nearest_sheep() finished with nearest_sheep: Sheep(id=%s, pos=%s)', self.nearest_sheep.id, self.nearest_sheep.pos)

    def move(self):
        logger.debug('move() called')
        
        dist = self.get_distance(self.nearest_sheep)
        if dist <= self.move_dist:
            self.nearest_sheep.is_alive = False
            self.pos = self.nearest_sheep.pos
        else:
            sin_alfa = abs(self.nearest_sheep.pos.y - self.pos.y) / dist
            abs_x = self.move_dist * sin_alfa
            abs_y = math.sqrt(self.move_dist ** 2 - abs_x ** 2)

            self.pos.x += abs_x if self.nearest_sheep.pos.x - self.pos.x > 0 else -abs_x
            self.pos.y += abs_y if self.nearest_sheep.pos.y - self.pos.y > 0 else -abs_y

            self.pos.x = round(self.pos.x, 3)
            self.pos.y = round(self.pos.y, 3)
            
        logger.debug('move() finished with pos: %s', self.pos)

    def get_distance(self, sheep: Sheep) -> float:
        distance = math.sqrt((self.pos.x - sheep.pos.x) ** 2 + (self.pos.y - sheep.pos.y) ** 2)
        
        logger.debug('get_distance() from the sheep with id: %s finished with value: %s', sheep.id, distance)
        return distance
