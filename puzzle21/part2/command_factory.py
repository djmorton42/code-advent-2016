import re
from move_command import MoveCommand
from swap_position_command import SwapPositionCommand
from swap_letter_command import SwapLetterCommand
from reverse_command import ReverseCommand
from rotate_command import RotateCommand
from rotate_based_on_position_command import RotateBasedOnPositionCommand

MOVE_PATTERN = re.compile('move position ([0-9]+) to position ([0-9]+)')
SWAP_PATTERN = re.compile('swap position ([0-9]+) with position ([0-9]+)')
SWAP_LETTER_PATTERN = re.compile('swap letter ([a-z]+) with letter ([a-z]+)')
REVERSE_PATTERN = re.compile('reverse positions ([0-9]+) through ([0-9]+)')
ROTATE_PATTERN = re.compile('rotate (right|left) ([0-9]+) step(s)?')
ROTATE_BASED_ON_POSITION_PATTERN = re.compile('rotate based on position of letter ([a-z]+)')

class CommandFactory:
    def get_command(self, instruction_text):
        match = MOVE_PATTERN.match(instruction_text)
        if match is not None:
            return MoveCommand(int(match.group(1)), int(match.group(2)))
            
        match = SWAP_PATTERN.match(instruction_text)
        if match is not None:
            return SwapPositionCommand(int(match.group(1)), int(match.group(2)))

        match = SWAP_LETTER_PATTERN.match(instruction_text)
        if match is not None:
            return SwapLetterCommand(match.group(1), match.group(2))

        match = REVERSE_PATTERN.match(instruction_text)
        if match is not None:
            return ReverseCommand(int(match.group(1)), int(match.group(2)))

        match = ROTATE_PATTERN.match(instruction_text)
        if match is not None:
            return RotateCommand(match.group(1), int(match.group(2)))

        match = ROTATE_BASED_ON_POSITION_PATTERN.match(instruction_text)
        if match is not None:
            return RotateBasedOnPositionCommand(match.group(1))

        raise ValueError('Instruction ' + instruction_text + ' could not be parsed!')
