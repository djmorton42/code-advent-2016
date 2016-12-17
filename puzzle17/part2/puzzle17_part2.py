import md5
import re
from position import Position

OPEN_PATTERN = re.compile('[b-f]{1}')

INPUT = 'lpvhkcbi'

starting_position = Position(0, 0, INPUT)

longest_solution = ''

def process_positions(positions, depth):
    global longest_solution

    possible_positions = set()
    for position in positions:
        possible_positions = possible_positions.union(
            set(position.get_possible_moves())
        )
   
    positions_to_cull = set()

    for position in possible_positions:
        if position.is_at_vault():
            solution = position.path.replace(INPUT, '')
            
            if len(solution) > len(longest_solution):
                longest_solution = solution
            
            positions_to_cull.add(position)

    possible_positions = possible_positions.difference(positions_to_cull)

    if len(possible_positions) > 0:
        process_positions(possible_positions, depth + 1)


process_positions([starting_position], 0)

print "Longest solution is " + str(len(longest_solution)) + " steps"
