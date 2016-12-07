import re
from operator import itemgetter

class Room:
    ASCII_CODE_LOWER_CASE_A = 97
    LETTERS_IN_ALPHABET = 26

    PATTERN = re.compile('([a-z\-]+)-([0-9]+)\[([a-z]{5})\]')
    
    def __init__(self, room_code):
        match = self.PATTERN.match(room_code)
        if match is None:
            raise ValueError("Could not parse room code: " + room_code)
        
        self.room_name = match.group(1)
        self.sector_id = int(match.group(2))
        self.checksum = match.group(3)

    def calculate_checksum(self):
        character_histogram = {}
        for character in self.room_name.replace('-', ''):
            if character in character_histogram:
                character_histogram[character] += 1
            else:
                character_histogram[character] = 1

        character_value_list = [(key, character_histogram[key]) for key in character_histogram.keys()]
       
        primary_sorted_list = sorted(character_value_list, key=itemgetter(0)) 
        secondary_sorted_list = sorted(primary_sorted_list, key=itemgetter(1), reverse = True)

        return ''.join([
            character_value[0] 
            for character_value 
            in secondary_sorted_list[0:5]
        ])

    def decrypt_name(self):
        return ''.join(
            [
                self.rotate_character(char, self.sector_id) 
                for char 
                in self.room_name
            ]
        )

    def rotate_character(self, char, rotations):
        if char == '-':
            return ' '
        else:
            return chr(
                self.ASCII_CODE_LOWER_CASE_A + 
                    (ord(char) - self.ASCII_CODE_LOWER_CASE_A + rotations) % self.LETTERS_IN_ALPHABET
            )
