import re
from node import Node
from world import World
from Queue import PriorityQueue

#All nodes except the middle row (size around 500T) can fit
#in the empty node.  Once we get to the state where we have
#the empty node to the left of the goal, we have a fixed number
#of steps based on the number of columns.  We can treat the
#large nodes as impassible, the empty node as our starting
#position and all other nodes as passable locations.  We can
#then use A* to 'find the best path' of the empty node to the
#left of the goal.

LINE_PATTERN = re.compile('/dev/grid/node-x([0-9]+)-y([0-9]+)[\s]+([0-9]+)T[\s]+([0-9]+)T[\s]+([0-9]+)T[\s]+([0-9]+)%')

nodes = []

max_x = 0
max_y = 0

open_set = PriorityQueue()
closed_set = set()
initial_state = None

class State:
    def __init__(self, x_pos, y_pos, depth, weight):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.depth = depth
        self.weight = weight

    @property
    def f_score(self):
        return self.weight + self.depth

    def __str__(self):
        return (
            "(" + str(self.x_pos) + ", " + str(self.y_pos) + ") " + 
            " - Depth: " + str(self.depth) + 
            " - Weight: " + str(self.weight) + 
            " - f_score: " + str(self.f_score)
        )

def calc_manhattan_distance(start_x, start_y, end_x, end_y):
    return abs(start_x - end_x) + abs(start_y - end_y)

def get_child_states(world, state):
    child_states = []
    child_nodes = []
    
    child_nodes.append(world.get_node(state.x_pos - 1, state.y_pos))
    child_nodes.append(world.get_node(state.x_pos + 1, state.y_pos))
    child_nodes.append(world.get_node(state.x_pos, state.y_pos - 1))
    child_nodes.append(world.get_node(state.x_pos, state.y_pos + 1))

    child_nodes = [
        child_node 
            for child_node 
            in child_nodes 
            if (child_node is not None and child_node.node_type != 'IMPASSIBLE')
    ]

    for child_node in child_nodes:
        child_states.append(
            State(
                child_node.x_pos, 
                child_node.y_pos, 
                state.depth + 1, 
                calc_manhattan_distance(
                    child_node.x_pos, child_node.y_pos, goal[0], goal[1]
                ) 
            )
        ) 

    return child_states


with open('input.txt') as file_handle:
    for line in file_handle:
        match = LINE_PATTERN.match(line)

        if match is not None:
            x = int(match.group(1))
            y = int(match.group(2))
            size = int(match.group(3))
            used = int(match.group(4))

            new_node = None

            if used == 0:
                new_node = Node(x, y, 'EMPTY')
                initial_state = State(x, y, 0, 0)
            elif size > 100:
                new_node = Node(x, y, 'IMPASSIBLE')
            else:
                new_node = Node(x, y, 'PASSABLE')

            nodes.append(new_node)

            if new_node.x_pos > max_x:
                max_x = new_node.x_pos

            if new_node.y_pos > max_y:
                max_y = new_node.y_pos

goal = (max_x - 1, 0)
world = World.from_nodes(nodes)

solution_depth = None

open_set.put((initial_state.f_score, initial_state))

while not open_set.empty():
    search_item = open_set.get()[1]  
   
    if (search_item.x_pos, search_item.y_pos) not in closed_set:
        print "Examining State: " + str(search_item)
        if search_item.x_pos == goal[0] and search_item.y_pos == goal[1]:
            solution_depth = search_item.depth
            print "Found Solution at Depth: " + str(solution_depth)
            break;

        closed_set.add((search_item.x_pos, search_item.y_pos))

        child_states = get_child_states(world, search_item)    
        for child_state in child_states:
            open_set.put((child_state.f_score, child_state))
    

#Once we know how many steps it takes to get the empty square to the left
#of the goal square, we derive the number of movements per column necessary
#from the example and we come up with:  (number_of_columns - 2) * 5 + 1

number_of_columns = max_x + 1

print "Number of steps to solution: " + str(solution_depth + ((number_of_columns - 2) * 5 + 1))

