class World:
    def __init__(self):
        self.discs = []
        self.time = 0
        self.capsule_position = 0
        self.capsule_is_dropped = False

    def reset(self):
        self.capsule_position = 0
        self.time = 0
        self.capsule_is_dropped = False

        for disc in self.discs:
            disc.reset()

    def add_discs(self, discs):
        self.discs = discs
 
    def fast_forward(self, seconds):
        self.time += seconds
        for disc in self.discs:
            disc.fast_forward(seconds)

    def tick(self):
        self.time += 1
        for disc in self.discs:
            disc.advance_position()
      
        if self.capsule_is_dropped:
            self.capsule_position += 1

            if not self.discs[self.capsule_position - 1].is_passable():
                return False

        return True

    def capsule_has_cleared_machine(self):
        return self.capsule_position == len(self.discs)

    def drop_capsule(self):
        self.capsule_is_dropped = True
