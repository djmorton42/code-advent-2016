keypad = { 
    '0,0': '0', '1,0': '0', '2,0': '1', '3,0': '0', '4,0': '0',
    '0,1': '0', '1,1': '2', '2,1': '3', '3,1': '4', '4,1': '0',
    '0,2': '5', '1,2': '6', '2,2': '7', '3,2': '8', '4,2': '9',
    '0,3': '0', '1,3': 'A', '2,3': 'B', '3,3': 'C', '4,3': '0',
    '0,4': '0', '1,4': '0', '2,4': 'D', '3,4': '0', '4,4': '0',
}

x = 0
y = 2

code = ''

def build_coordinates(x, y):
    return str(x) + ',' + str(y)

def coordinate_in_bounds(x, y):
    return keypad.get(build_coordinates(x, y), '0') != '0'

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
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
