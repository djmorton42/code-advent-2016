from rotate_command import RotateCommand

class RotateBasedOnPositionCommand:
    def __init__(self, letter):
        self.letter = letter

    def process(self, input):
        index = input.index(self.letter)
        if index >= 4:
            index += 1

        return RotateCommand('right', index + 1).process(input)
