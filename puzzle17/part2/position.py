import md5
import re

OPEN_PATTERN = re.compile('[b-f]{1}')

class Position:

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    MAX_ROWS = 4
    MAX_COLUMNS = 4

    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.path = path

    def hash_path(self, path):
        return md5.new(path).hexdigest().lower()

    def is_door_open(self, hashed_path, direction):
        return OPEN_PATTERN.match(hashed_path[direction]) is not None

    def get_possible_moves(self):
        possible_moves = []
        hashed_path = self.hash_path(self.path)
        if self.x > 0:
            if self.is_door_open(hashed_path, self.LEFT):
                possible_moves.append(Position(self.x - 1, self.y, self.path + 'L'))

        if self.x < self.MAX_COLUMNS - 1:
            if self.is_door_open(hashed_path, self.RIGHT):
                possible_moves.append(Position(self.x + 1, self.y, self.path + 'R'))

        if self.y > 0:
            if self.is_door_open(hashed_path, self.UP):
                possible_moves.append(Position(self.x, self.y - 1, self.path + 'U'))

        if self.y < self.MAX_ROWS - 1:
            if self.is_door_open(hashed_path, self.DOWN):
                possible_moves.append(Position(self.x, self.y + 1, self.path + 'D'))

        return possible_moves

    def is_at_vault(self):
        return self.x == self.MAX_COLUMNS - 1 and self.y == self.MAX_ROWS - 1

