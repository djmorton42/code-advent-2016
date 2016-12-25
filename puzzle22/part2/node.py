class Node:
    def __init__(self, x_pos, y_pos, node_type):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.node_type = node_type
    
    def clone(self):
        return Node(self.x_pos, self.y_pos, self.node_type)
