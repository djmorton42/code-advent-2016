import re
import time
import sys

class Interpreter:


    JUMP_COMMAND_PATTERN = re.compile('jnz ([a-d]{1}|[0-9]+) ([\-0-9]+)')
    COPY_COMMAND_PATTERN = re.compile('cpy ([a-d]{1}|[0-9]+) ([a-d]{1})')
    INC_COMMAND_PATTERN = re.compile('inc ([a-d]{1})')
    DEC_COMMAND_PATTERN = re.compile('dec ([a-d]{1})')
    REGISTER_PATTERN = re.compile('[a-d]{1}')

    def __init__(self):
        self.registers = {'a':0, 'b':0, 'c':1, 'd':0}

    def print_registers(self):
        for register_name in self.registers:
            print register_name + ' = ' + str(self.registers[register_name])

    def get_register_value(self, register_name):
        return self.registers[register_name]

    def get_register_or_literal(self, value):
        if self.REGISTER_PATTERN.match(value):
            return self.registers[value]
        else:
            return int(value)

    def execute(self, instructions):
        instruction_count = len(instructions)

        instruction_index = 0

        while instruction_index < instruction_count:
            current_instruction = instructions[instruction_index]

            match = self.JUMP_COMMAND_PATTERN.match(current_instruction)
            
            if match is not None:
                jump_value = int(match.group(2))
                check_value = match.group(1)

                if self.get_register_or_literal(check_value) != 0:
                    instruction_index += jump_value
                else:
                    instruction_index += 1

                continue

            match = self.COPY_COMMAND_PATTERN.match(current_instruction)
            
            if match is not None:
                target_register = match.group(2)
                source = match.group(1)
                self.registers[target_register] = self.get_register_or_literal(source)  
                instruction_index += 1
                continue

            match = self.INC_COMMAND_PATTERN.match(current_instruction)

            if match is not None:
                self.registers[match.group(1)] += 1
                instruction_index += 1
                continue

            match = self.DEC_COMMAND_PATTERN.match(current_instruction)

            if match is not None:
                self.registers[match.group(1)] -= 1
                instruction_index += 1
                continue

            if match is None:
                print "No Match Found for instruction: " + current_instruction
                sys.exit()
               
        print "Final Register State:"
        self.print_registers()


