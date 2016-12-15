from map_status_calculator import MapStatusCalculator
from operator import attrgetter
from config import Config

class Move:
    def __init__(self, parent_move, x, y, weight):
        self.parent_move = parent_move
        self.x = x
        self.y = y
        self.weight = weight
        self.child_moves = []

    def equal_position(self, move):
        if move is None:
            return False

        return self.x == move.x and self.y == move.y

    def child_moves_contain(self, move):
        for child_move in self.child_moves:
            if child_move.equal_position(move):
                return True

        return False

    def calculate_weight(self, x, y):
        distance = self.distance_to_target(x, y)
        if distance == 0:
            return 1
        else:
            return 1.0 / distance

    def distance_to_target(self, x, y):
        delta_x = abs(Config.target_x - x)
        delta_y = abs(Config.target_y - y)

        if delta_x == 0:
            return delta_y
        else:
            return 1.0 * delta_y / delta_x

        return 1.0 * delta_y / delta_x

    def get_move_history(self):
        if self.x > Config.max_x:
            Config.max_x = self.x
        
        if self.y > Config.max_y:
            Config.max_y = self.y

        if self.parent_move is None:
            return [(self.x, self.y)]
        else:
            move_history = self.parent_move.get_move_history()
            move_history.append((self.x, self.y))

            return move_history

    def get_neighbouring_moves(self):
        moves = []
       
        if self.x - 1 >= 0: 
            new_move = Move(self, self.x - 1, self.y, self.calculate_weight(self.x - 1, self.y))
            if (
                not new_move.equal_position(self.parent_move) 
                and MapStatusCalculator.is_passable(new_move.x, new_move.y)
            ):
                moves.append(new_move)

        if self.y - 1 >= 0:
            new_move = Move(self, self.x, self.y - 1, self.calculate_weight(self.x, self.y - 1))
            if (
                not new_move.equal_position(self.parent_move) 
                and MapStatusCalculator.is_passable(new_move.x, new_move.y)
            ):
                moves.append(new_move)

        new_move = Move(self, self.x + 1, self.y, self.calculate_weight(self.x + 1, self.y))
        if (
            not new_move.equal_position(self.parent_move) 
            and MapStatusCalculator.is_passable(new_move.x, new_move.y)
        ):
            moves.append(new_move)
        
        new_move = Move(self, self.x, self.y + 1, self.calculate_weight(self.x, self.y + 1))
        if (
            not new_move.equal_position(self.parent_move) 
            and MapStatusCalculator.is_passable(new_move.x, new_move.y)
        ):
            moves.append(new_move)

        return sorted(self.filter_out_higher_children(self.filter_out_loops(moves)), key = attrgetter('weight'))

    def filter_out_loops(self, moves):
        filtered_list = [move for move in moves if not move.equal_position(self)] 
       
        if len(filtered_list) == 0:
            return filtered_list

        if self.parent_move is not None:
            return self.parent_move.filter_out_loops(filtered_list)
        else:
            return filtered_list

    def filter_out_higher_children(self, moves):
        if self.parent_move is None:
            return moves

        filtered_list = [move for move in moves if not self.parent_move.child_moves_contain(move)]
        
        if len(filtered_list) == 0:
            return filtered_list

        return self.parent_move.filter_out_higher_children(filtered_list)



