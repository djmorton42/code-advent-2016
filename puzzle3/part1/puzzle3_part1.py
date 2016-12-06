def is_possible_triangle(sides):
    for i in range(3):
        is_possible = sides[i] + sides[(i + 1) % 3] > sides[(i + 2) % 3]
        if not is_possible:
            return False

    return True

def line_to_triangle_sides(line):
    return [int(side) for side in line.strip().split()]

with open('input.txt') as file_handle:
    lines = file_handle.readlines()
    print str(
        sum(
            is_possible_triangle(line_to_triangle_sides(line)) 
            for line 
            in lines
        )
    ) + " triangles are possible"
