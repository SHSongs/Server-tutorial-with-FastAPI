class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)


class Player:
    def __init__(
            self, pos: Point = Point(0, 0), canFly: bool = False
    ) -> None:
        self.pos = pos
        self.canFly = canFly


player_1 = Player(pos=Point(3, 4), canFly=True)

print(player_1)  # <__main__.Player object at 0x102a5c7c0>
print("위치: ", player_1.pos.x, player_1.pos.y)  # 위치:  3 4
print("날 수 있나?: ", player_1.canFly)  # 날 수 있나?:  True

pos1 = Point(1, 1)
pos2 = Point(1, 1)
print(pos1 == pos2)
