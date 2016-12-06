from position import Position

TUPLE_TURN_DIRECTION_INDEX = 0
TUPLE_STEP_COUNT_INDEX = 1

found_solution = False

def handle_step(position, step):
    global found_solution

    position.turn(step[TUPLE_TURN_DIRECTION_INDEX])
    for _ in range(step[TUPLE_STEP_COUNT_INDEX]):
        position.step_forward()
        if position.visited_location_previously():
            found_solution = True
            return

with open('input.txt') as f:
    instructions = f.read()

    steps = [(step[0], int(step[1:])) for step in [step.strip() for step in instructions.split(',')]]

    position = Position()

    for step in steps:
        handle_step(position, step)
        if found_solution:
            break
                
    print "Final Position: " + str(position.get_coordinates())
    print "Distance From Origin: " + str(position.distance_from_origin())

