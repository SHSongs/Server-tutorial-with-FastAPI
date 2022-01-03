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

print("위치: ", player_1.pos.x, player_1.pos.y)
print("날 수 있나?: ", player_1.canFly)
