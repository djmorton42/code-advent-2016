import md5
import re
from position import Position

OPEN_PATTERN = re.compile('[b-f]{1}')

INPUT = 'lpvhkcbi'

starting_position = Position(0, 0, INPUT)

def process_positions(positions, depth):
    possible_positions = []
    for position in positions:
        possible_positions.extend(position.get_possible_moves())

    for position in possible_positions:
        if position.is_at_vault():
            print "Found Solution at depth " + str(depth) + ": " + position.path.replace(INPUT, '')
            return

    if len(possible_positions) > 0:
        process_positions(possible_positions, depth + 1)


process_positions([starting_position], 0)
