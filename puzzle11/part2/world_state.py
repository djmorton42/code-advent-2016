class WorldState:
    def __init__(self, world):
        self.world = world
        self.child_states = set()
        self.parent_state = None

    def add_child_state(self, child_state):
        self.child_states.add(child_state)
        child_state.parent_state = self

    def state_history(self):
        if self.parent_state is None:
            return self.world.code()
        else:
            return self.parent_state.state_history() + ' -> ' + self.world.code()    

