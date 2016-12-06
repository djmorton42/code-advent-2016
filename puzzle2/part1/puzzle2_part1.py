keypad = { 
    '0,0': '1', '1,0': '2', '2,0': '3',
    '0,1': '4', '1,1': '5', '2,1': '6',
    '0,2': '7', '1,2': '8', '2,2': '9'
}

MIN_BOUND_INCLUSIVE = 0
MAX_BOUND_EXCLUSIVE = 3

code = ''

def build_coordinates(x, y):
    return str(x) + ',' + str(y)

def coordinate_in_bounds(x, y):
    return (x >= MIN_BOUND_INCLUSIVE and x < MAX_BOUND_EXCLUSIVE
        and y >= MIN_BOUND_INCLUSIVE and y < MAX_BOUND_EXCLUSIVE)
        
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        x = 1
        y = 1
        for c in line:
            new_x = x
            new_y = y

            if c == 'U':
                new_y -= 1
            elif c == 'R':
                new_x += 1
            elif c == 'D':
                new_y += 1
            elif c == 'L':
                new_x -= 1

            if coordinate_in_bounds(new_x, new_y):
                x = new_x
                y = new_y
        
        code += keypad[build_coordinates(x, y)]

print "Code: " + code
