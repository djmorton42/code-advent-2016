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

    def has_abba_sequence(self):
        found_abba = False

        for i in range(1, len(self.sequence) - 2):
            if (
                self.sequence[i - 1] != self.sequence[i] and 
                self.sequence[i] == self.sequence[i + 1] and 
                self.sequence[i - 1] == self.sequence[i + 2]
            ):
           
                found_abba = True
                break

        return found_abba
