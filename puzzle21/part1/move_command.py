class MoveCommand:
    def __init__(self, from_position, to_position):
        self.from_position = from_position
        self.to_position = to_position

    def process(self, input):
        input_chars = list(input)

        removed_char = input_chars.pop(self.from_position)
        input_chars.insert(self.to_position, removed_char)

        return ''.join(input_chars)

