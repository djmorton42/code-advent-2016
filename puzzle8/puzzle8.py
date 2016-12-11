import re
from screen import Screen

ROTATE_ROW_PATTERN = re.compile('rotate row y=([0-9]+) by ([0-9]+)')
ROTATE_COL_PATTERN = re.compile('rotate column x=([0-9]+) by ([0-9]+)')
SET_RECT_PATTERN = re.compile('rect ([0-9]+)x([0-9]+)')

screen = Screen(6, 50)

with open('input.txt') as file_handle:
    for line in file_handle:
        match = ROTATE_ROW_PATTERN.match(line)

        if match is not None:
            screen.rotate_row(int(match.group(1)), int(match.group(2)))
            continue

        match = ROTATE_COL_PATTERN.match(line)

        if match is not None:
            screen.rotate_column(int(match.group(1)), int(match.group(2)))
            continue

        match = SET_RECT_PATTERN.match(line)
        
        if match is not None:
            screen.turn_on_rect(int(match.group(1)), int(match.group(2)))
            continue

    screen.print_matrix()
    print ''
    print 'Number of Lit Pixels: ' + str(screen.get_lit_pixel_count())
