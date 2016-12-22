from command_factory import CommandFactory

commands = []
inputs = ['fbgdceah']

with open('input.txt') as file_handle:
    command_factory = CommandFactory()
    for instruction in file_handle:
        commands.insert(0, command_factory.get_command(instruction))

for input in inputs:
    current_text = input
    for command in commands:
        current_text = command.process_inverse(current_text)

    print "Solution for input " + input + " is " + current_text
