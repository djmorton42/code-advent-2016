import re

rows = ['.^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....']

TRAP_PATTERN = re.compile('\^\^\.|\.\^\^|\^\.\.|\.\.\^')

NUMBER_OF_ROWS = 40

def count_safe_tiles_in_row(row):
    return sum(1 for char in row if char == '.')

def extract_relevant_tiles(row, index):
    padded_row = '.' + row + '.'
    return row[index - 1:index + 2]

def generate_new_row():
    row_to_examine = rows[-1]
    padded_row_to_examine = '.' + row_to_examine + '.'

    new_row = ''

    for tile_index in range(len(row_to_examine)):
        characters = padded_row_to_examine[tile_index:tile_index + 3]

        new_row += '^' if TRAP_PATTERN.match(characters) is not None else '.'

    return new_row

while len(rows) < NUMBER_OF_ROWS:
    rows.append(generate_new_row())

for row in rows:
    print row

print ''
print "Number of safe tiles: " + str(sum(count_safe_tiles_in_row(row) for row in rows))

