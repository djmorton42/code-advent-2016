from move import Move
from map_status_calculator import MapStatusCalculator
from config import Config

initial_move = Move(None, Config.starting_x, Config.starting_y, 0)
final_position = Move(None, Config.target_x, Config.target_y, 0)


def print_board(move_history):
    print "Max Coords: (" + str(Config.max_x) + ", " + str(Config.max_y) + ")"
    print move_history
    print "Number of Steps: " + str(len(move_history) - 1)

    board = []
    for y in range(Config.max_y + 2):
        board.append([ (' ' if MapStatusCalculator.is_passable(x, y) else '#') for x in range(Config.max_x + 2)   ])

    for move in move_history:
        board[move[1]][move[0]] = '.'

    for y in range(Config.max_y + 2):
        print ' '.join(board[y])

def check_position(position):
    position.child_moves = position.get_neighbouring_moves()

    for move in position.child_moves:
        if final_position.equal_position(move):
            print "Found Solution!"
            print_board(move.get_move_history())
            return True
        else:
            if check_position(move):
                return True
    
    return False

check_position(initial_move)
