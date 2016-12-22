class RotateCommand:
    def __init__(self, direction, steps):
        self.direction = direction
        self.steps = steps

    def process(self, input):
        output = input
        for _ in range(self.steps):
            if self.direction == 'right':
                output = output[-1] + output[0:-1]    
            elif self.direction == 'left':
                output = output[1:] + output[0]
 
        return output

    def opposite_direction(self):
        return 'right' if self.direction == 'left' else 'left'

    def process_inverse(self, input):
        return RotateCommand(self.opposite_direction(), self.steps).process(input)

    def __str__(self):
        return "Rotate[direction: " + self.direction + ", steps: " + str(self.steps) + "]"
