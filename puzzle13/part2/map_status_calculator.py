from config import Config

class MapStatusCalculator:
    @staticmethod
    def is_passable(x, y):
        number_of_on_bits = sum(
            1 
            for c 
            in bin(
                Config.favourite_number + (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
            ) if c == '1'
        )
        
        return (number_of_on_bits % 2) == 0
