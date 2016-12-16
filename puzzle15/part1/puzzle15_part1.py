import re
import sys
from operator import attrgetter
from disc import Disc
from world import World

DISC_STATE_PATTERN = re.compile(
    'Disc #([0-9]+) has ([0-9]+) positions; at time=0, it is at position ([0-9]+).'
)

world = World()

with open('input.txt') as file_handle:
    setup = file_handle.readlines()
  
    discs = []

    for setup_line in setup:
        match = DISC_STATE_PATTERN.match(setup_line)
        if match is None:
            print "Error parsing instruction line: " + setup_line
            sys.exit()
       
        discs.append(
            Disc(
                int(match.group(1)), 
                int(match.group(2)), 
                int(match.group(3))
            )
        )

    world.add_discs(sorted(discs, key = attrgetter('index')))

time_to_drop = 0
maximum_time = 1000000

for time_to_drop in range(maximum_time):
    if (time_to_drop % 1000) == 0:
        print "Testing TTD: " + str(time_to_drop)

    world.reset()
    world.fast_forward(time_to_drop)
    while(True):
        if world.time == time_to_drop:
            world.drop_capsule()
        
        if not world.tick():
            break

        if world.capsule_is_dropped and world.capsule_has_cleared_machine():
            print "Cleared machine when dropped at t=" + str(time_to_drop)
            sys.exit()
