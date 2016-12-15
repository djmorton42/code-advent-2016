class Generator:
    def __init__(self, material, floor):
        self.material = material
        self.floor = floor
        self.abbreviation = material[0] + 'G'

    def clone(self):
        return Generator(self.material, self.floor)

    def code(self):
        return self.abbreviation + str(self.floor)

    def move_up(self):
        if self.floor < 4:
            self.floor += 1
        else:
            print "Can not move " + self.code() + " up because it is at the top floor!"

    def move_down(self):
        if self.floor > 1:
            self.floor -= 1
        else:
            print "Can not move " + self.code() + " down because it is at the bottom floor!"
