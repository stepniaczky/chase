import random

from dataclasses import dataclass, field

from src.models.point import Point
from src.common import INIT_POS_LIMIT, SHEEP_MOVE_DIST


@dataclass
class Sheep:
    id: int
    pos: Point = field(init=False)
    move_dist: float = field(init=False, default=SHEEP_MOVE_DIST)
    is_alive: bool = field(init=False, default=True)

    def __post_init__(self):
        self.pos = Point(x=round(random.uniform(-INIT_POS_LIMIT, INIT_POS_LIMIT), 1),
                         y=round(random.uniform(-INIT_POS_LIMIT, INIT_POS_LIMIT), 1))

    def move(self):
        axis: list = ['x', 'y']
        dist: list = [-self.move_dist, self.move_dist]

        rand_axis = random.choice(axis)
        rand_dist = random.choice(dist)

        attr_value = getattr(self.pos, rand_axis)
        setattr(self.pos, rand_axis, round(attr_value + rand_dist, 1))
