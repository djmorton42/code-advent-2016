import re
from node import Node

LINE_PATTERN = re.compile('/dev/grid/node-x([0-9]+)-y([0-9]+)[\s]+([0-9]+)T[\s]+([0-9]+)T[\s]+([0-9]+)T[\s]+([0-9]+)%')

nodes = []

with open('input.txt') as file_handle:
    for line in file_handle:
        match = LINE_PATTERN.match(line)

        if match is not None:
            nodes.append(
                Node(
                    int(match.group(1)), 
                    int(match.group(2)), 
                    int(match.group(3)), 
                    int(match.group(4)), 
                    int(match.group(5))
                )
            )

viable_pair_counter = 0

for node in nodes:
    for other_node in nodes:
        if node != other_node and node.used <= other_node.available and node.used > 0:
            viable_pair_counter += 1

print str(viable_pair_counter) + " pairs found!"
