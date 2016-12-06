def is_possible_triangle(sides):
    for i in range(3):
        is_possible = sides[i] + sides[(i + 1) % 3] > sides[(i + 2) % 3]
        if not is_possible:
            return False

    return True

def line_to_triangle_sides(line):
    return [int(side) for side in line.strip().split()]

def extract_triangles(triangle_lines):
    matrix = [line_to_triangle_sides(line) for line in triangle_lines]
    return [[matrix[0][0], matrix[1][0], matrix[2][0]], 
            [matrix[0][1], matrix[1][1], matrix[2][1]], 
            [matrix[0][2], matrix[1][2], matrix[2][2]]
    ]

def read_triangles(file_handle):
    candidate_triangles = []
    triangle_lines = []
    counter = 0
    for line in file_handle:
        triangle_lines.append(line)
        counter += 1

        if counter == 3:
            counter = 0
            candidate_triangles.extend(extract_triangles(triangle_lines))
            triangle_lines = []

    return candidate_triangles

with open('input.txt') as file_handle:
    print str(
        sum(
            is_possible_triangle(triangle_sides)
            for triangle_sides
            in read_triangles(file_handle)
        )
    ) + " triangles are possible"
