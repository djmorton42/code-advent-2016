class Disc:
    def __init__(self, index, total_positions, current_position):
        self.index = index
        self.total_positions = total_positions
        self.current_position = current_position
        self.initial_position = current_position

    def advance_position(self):
        self.current_position = (self.current_position + 1) % self.total_positions 

    def is_passable(self):
        return self.current_position == 0

    def reset(self):
        self.current_position = self.initial_position

    def fast_forward(self, seconds):
        self.current_position = (self.current_position + seconds) % self.total_positions
