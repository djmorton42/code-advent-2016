class World:

    def __init__(self):
        self.nodes = []
        self.node_map = {}

    @staticmethod
    def from_nodes(nodes):
        new_world = World()
        new_world.nodes = [node.clone() for node in nodes]
        new_world.node_map = {(node.x_pos, node.y_pos): node for node in new_world.nodes}
        
        return new_world

    def get_node(self, x_pos, y_pos):
        return self.node_map.get((x_pos, y_pos), None)
