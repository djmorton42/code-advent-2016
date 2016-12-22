class SwapPositionCommand:
    def __init__(self, from_position, to_position):
        self.from_position = from_position
        self.to_position = to_position

    def process(self, input):
        input_chars = list(input)

        first_char = input_chars[self.from_position]
        second_char = input_chars[self.to_position]

        input_chars[self.from_position] = second_char
        input_chars[self.to_position] = first_char

        return ''.join(input_chars)
    
    def process_inverse(self, input):
        return SwapPositionCommand(self.to_position, self.from_position).process(input)
