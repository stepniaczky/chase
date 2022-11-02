import math

from typing import List
from dataclasses import dataclass, field

from src.models.point import Point
from src.models.sheep import Sheep
from src.common import WOLF_MOVE_DIST, WOLF_INIT_POS_X, WOLF_INIT_POS_Y


@dataclass
class Wolf:
    pos: Point = field(init=False)
    move_dist: float = field(init=False, default=WOLF_MOVE_DIST)
    nearest_sheep: Sheep = field(init=False)

    def __post_init__(self):
        self.pos = Point(x=WOLF_INIT_POS_X, y=WOLF_INIT_POS_Y)

    def find_nearest_sheep(self, sheep_flock: List[Sheep]):
        filtered_flock = [sheep for sheep in sheep_flock if sheep.is_alive]
        sorted_flock = sorted(filtered_flock, key=self.get_distance)
        self.nearest_sheep = sorted_flock[0]

    def move(self):
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

    def get_distance(self, sheep: Sheep) -> float:
        return math.sqrt((self.pos.x - sheep.pos.x) ** 2 + (self.pos.y - sheep.pos.y) ** 2)
