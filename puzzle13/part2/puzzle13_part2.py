from move import Move
from map_status_calculator import MapStatusCalculator
from config import Config

initial_move = Move(None, Config.starting_x, Config.starting_y, 0)

positions = {(1, 1)}

def check_position(position):
    position.child_moves = position.get_neighbouring_moves()

    for move in position.child_moves:
        if move.calculate_depth() <= Config.max_depth:
            positions.add((move.x, move.y))        
            check_position(move)

check_position(initial_move)

print "Unique Positions: " + str(len(positions))
