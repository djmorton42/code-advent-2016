class Position:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = 0

    def step_forward(self):
        effective_facing = self.facing % 4

        if effective_facing == 0:
            self.y += 1
        elif effective_facing == 1:
            self.x += 1
        elif effective_facing == 2:
            self.y -= 1
        elif effective_facing == 3:
            self.x -= 1

    def turn_right(self):
        self.facing += 1

    def turn_left(self):
        self.facing += 3

    def turn(self, direction_character):
        if direction_character == 'R':
            self.turn_right()
        elif direction_character == 'L':
            self.turn_left()
        else:
            raise ValueError("Only 'R' and 'L' are valid directions to turn")

    def get_coordinates(self):
        return self.x, self.y

    def distance_from_origin(self):
        return abs(self.x) + abs(self.y)
