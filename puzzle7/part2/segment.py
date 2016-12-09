class Segment:
    def __init__(self, sequence):
        if sequence[0] == '[':
            self.sequence = sequence[1:-1]
            self.is_hypernet_segment = True
        else:
            self.sequence = sequence    
            self.is_hypernet_segment = False
        
    def is_hypernet_segment(self):
        return self.is_hypernet_segment

    def get_aba_sequences(self):
        aba_sequences = []

        for i in range(1, len(self.sequence) - 1):
            if (
                self.sequence[i - 1] != self.sequence[i] and 
                self.sequence[i - 1] == self.sequence[i + 1] 
            ):
                aba_sequences.append(self.sequence[i - 1 : i + 2])
        return aba_sequences

    def contains_bab_sequence(self, aba_sequences):
        for aba_sequence in aba_sequences:
            bab_sequence = aba_sequence[1] + aba_sequence[0:2]

            if bab_sequence in self.sequence:
                return True

        return False
