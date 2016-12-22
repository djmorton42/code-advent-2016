class SwapLetterCommand:
    def __init__(self, first_letter, second_letter):
        self.first_letter = first_letter
        self.second_letter = second_letter

    def process(self, input):
        first_letter_index = input.index(self.first_letter)
        second_letter_index = input.index(self.second_letter)

        chars = list(input)  
        chars[first_letter_index] = self.second_letter
        chars[second_letter_index] = self.first_letter

        return ''.join(chars)

    def process_inverse(self, input):
        return SwapLetterCommand(self.second_letter, self.first_letter).process(input)
