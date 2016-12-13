from generator import Generator
from microchip import Microchip
from world import World
from world_state import WorldState
import sys

sys.setrecursionlimit(100000)
step_count = 0
max_items_on_level_4 = 0

def get_initial_state():

    generators = [
        Generator('S', 1),
        Generator('P', 1),
        Generator('T', 2),
        Generator('R', 2),
        Generator('C', 2)
    ]

    microchips = [
        Microchip('S', 1),
        Microchip('P', 1),
        Microchip('T', 3),
        Microchip('R', 2),
        Microchip('C', 2)
    ]

    elevator_floor = 1

    return World(generators, microchips, elevator_floor)

initial_world = get_initial_state()

state_history = set()
state_history.add(initial_world.code())

world_state = WorldState(initial_world)

def handle_new_world(world_state, new_world, state_history):
    global max_items_on_level_4

    new_world_code = new_world.code()
  
    if new_world_code not in state_history and new_world.is_valid():
        state_history.add(new_world_code)
        new_state = WorldState(new_world)
        world_state.add_child_state(new_state)

        items_on_4th_level = new_world.get_items_on_level(4)
        if len(items_on_4th_level) > max_items_on_level_4:
            max_items_on_level_4 = len(items_on_4th_level)
        #    print(' '.join([item.abbreviation for item in items_on_4th_level]))

        return new_state
    else:
        return None

def move_permutations(world, permutations, direction):
    new_states = []

    destination_floor = world.elevator_floor + direction
    if destination_floor >= 1 and destination_floor <= 4:
        for permutation in permutations:
            new_world = world.clone()
            for item in list(permutation):
                if direction == 1:
                    new_world.move_up(item)
                elif direction == -1:
                    new_world.move_down(item)

            new_world.elevator_floor += direction
            
            new_state = handle_new_world(world_state, new_world, state_history)
            if new_state is not None:
                new_states.append(new_state)

    return new_states

def process_child_states(world_states, state_history):
    global step_count

    if max_items_on_level_4 == 10:
        print "Found Result!"
        return world_states

    step_count += 1
    print "Steping down to level " + str(step_count)
    print "State Count: " + str(len(state_history))
    print "States at this level: " + str(len(world_states))
    print "Max Items on Level 4: " + str(max_items_on_level_4)
    print ''
    print ''

    child_states = set()

    dead_ends = []

    for world_state in world_states:
        current_world = world_state.world
        permutations = current_world.get_movable_permutations()

        child_states.update(move_permutations(current_world, permutations, 1))
        child_states.update(move_permutations(current_world, permutations, -1))

        if len(world_state.child_states) == 0:
            dead_ends.append(world_state)

    found_end_state = False

    for dead_end in dead_ends:
        world_states.remove(dead_end)
        dead_end.parent_state.child_states.remove(dead_end)
        dead_end.parent_state = None

    del dead_ends[:]

    if found_end_state:
        return child_states
    else:
        return process_child_states(child_states, state_history)

process_child_states([world_state], state_history)
