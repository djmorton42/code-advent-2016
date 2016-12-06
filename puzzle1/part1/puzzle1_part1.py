from position import Position

TUPLE_TURN_DIRECTION_INDEX = 0
TUPLE_STEP_COUNT_INDEX = 1

with open('input.txt') as f:
    instructions = f.read()

    steps = [(step[0], int(step[1:])) for step in [step.strip() for step in instructions.split(',')]]

    position = Position()

    for step in steps:
        position.turn(step[TUPLE_TURN_DIRECTION_INDEX])
        for _ in range(step[TUPLE_STEP_COUNT_INDEX]):
            position.step_forward()

    print "Final Position: " + str(position.get_coordinates())
    print "Distance From Origin: " + str(position.distance_from_origin())

