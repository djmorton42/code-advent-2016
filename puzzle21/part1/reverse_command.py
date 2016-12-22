class ReverseCommand:
    def __init__(self, from_position, to_position):
        self.from_position = from_position
        self.to_position = to_position

    def process(self, input):
        intermediate_value = (input[0:self.from_position] + 
            input[self.from_position:self.to_position + 1][::-1]
        )
        
        if self.to_position < len(input) - 1:
           intermediate_value += input[self.to_position + 1:] 

        return intermediate_value
