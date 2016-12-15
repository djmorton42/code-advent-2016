from interpreter import Interpreter

interpreter = Interpreter()

with open('input.txt') as file_handle:
    instructions = file_handle.readlines()

    interpreter.execute(instructions)
