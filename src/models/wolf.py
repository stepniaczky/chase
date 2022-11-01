import math

from typing import List
from dataclasses import dataclass, field

from src.models.point import Point
from src.models.sheep import Sheep
from src.utils.constans import WOLF_MOVE_DIST, WOLF_INIT_POS_X, WOLF_INIT_POS_Y


@dataclass
class Wolf:
    pos: Point = field(init=False, default=Point(
        x=WOLF_INIT_POS_X, y=WOLF_INIT_POS_Y))
    move_dist: float = field(init=False, default=WOLF_MOVE_DIST)

    def move(self, sheep_flock: List[Sheep]):
        sorted_distance = sorted(sheep_flock, key=self.get_distance)
        nearest_sheep = sorted_distance[0]

        dist = self.get_distance(nearest_sheep)
        if dist <= self.move_dist:
            nearest_sheep.is_alive = False
            self.pos = nearest_sheep.pos
        else:
            sin_alfa = abs(nearest_sheep.pos.y - self.pos.y) / dist
            abs_x = self.move_dist * sin_alfa
            abs_y = math.sqrt(self.move_dist ** 2 - abs_x ** 2)

            self.pos.x += abs_x if nearest_sheep.pos.x - self.pos.x > 0 else -abs_x
            self.pos.y += abs_y if nearest_sheep.pos.y - self.pos.y > 0 else -abs_y

            self.pos.x = round(self.pos.x, 3)
            self.pos.y = round(self.pos.y, 3)

    def get_distance(self, sheep: Sheep) -> float:
        return math.sqrt((self.pos.x - sheep.pos.x) ** 2 + (self.pos.y - sheep.pos.y) ** 2)
