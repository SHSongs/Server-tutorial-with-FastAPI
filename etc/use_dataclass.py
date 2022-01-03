from dataclasses import dataclass


@dataclass
class Point:
    x: int = 0
    y: int = 0


@dataclass
class Player:
    pos: Point = Point(0, 0)
    canFly: bool = False


player_1 = Player(pos=Point(3, 4), canFly=True)
print(player_1)  # Player(pos=Point(x=3, y=4), canFly=True)

pos1 = Point(1, 1)
pos2 = Point(1, 1)
print(pos1 == pos2)  # True

from dataclasses import dataclass, field
from typing import List


@dataclass
class Record:
    player: Player = Player()
    foot_print: List[Point] = field(default_factory=list)


record = Record()
record.foot_print.append(Point(1, 1))
record.foot_print.append(Point(2, 2))
print(record.foot_print)  # [Point(x=1, y=1), Point(x=2, y=2)]
