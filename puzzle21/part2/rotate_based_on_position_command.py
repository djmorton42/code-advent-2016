from rotate_command import RotateCommand

class RotateBasedOnPositionCommand:
    def __init__(self, letter):
        self.letter = letter

    def process(self, input):
        index = input.index(self.letter)
        if index >= 4:
            index += 1

        return RotateCommand('right', index + 1).process(input)
    
    def process_inverse(self, input):
        index = input.index(self.letter)

        for candidate_initial_position in range(len(input)):
            calculated_new_position = self.calculate_new_position(len(input), candidate_initial_position)

            direction = None
            steps = None

            if candidate_initial_position > index:
                direction = 'right'
                steps = candidate_initial_position - index
            else:
                direction = 'left'
                steps = index - candidate_initial_position

            if index == calculated_new_position:
                return RotateCommand(direction, steps).process(input)


    def calculate_new_position(self, input_length, initial_position):
        return (initial_position + (
            1 + 
            initial_position + 
            (1 if initial_position >= 4 else 0)
        )) % input_length

    def __str__(self):
        return "RotateBasedOnPosition[letter: " + self.letter + "]"
