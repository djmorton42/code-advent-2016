class OutputBin:
    
    def __init__(self, id):
        self.id = id
        self.chips = []

    def add_chip(self, value):
        self.chips.append(value)

    def responsible_for(self, chip_ids):
        return False

    def get_chip_values(self):
        return sorted(self.chips)
    
    def __str__(self):
        return "Output Bin: " + str(self.id)
