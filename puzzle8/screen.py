class Screen:

    def __init__(self, height, width):
        self.pixel_matrix = [[0 for x in range(width)] for y in range(height)]

    def set_pixel(self, x, y, state):
        self.pixel_matrix[y][x] = state

    def turn_on_rect(self, width, height):
        for y in range(height):
            for x in range(width):
                self.pixel_matrix[y][x] = 1

    def rotate_row(self, row_index, number_to_rotate):
        self.pixel_matrix[row_index] = self.rotate_array(
            self.pixel_matrix[row_index], 
            number_to_rotate
        )

    def rotate_array(self, array, number_to_rotate):
        first_segment = array[-number_to_rotate:]
        second_segment = array[:-number_to_rotate] 

        new_array = []
        new_array.extend(first_segment)
        new_array.extend(second_segment)

        return new_array

    def rotate_column(self, column_index, number_to_rotate):
        self.set_column(column_index, self.rotate_array(self.get_column(column_index), number_to_rotate))

    def get_row(self, row_index):
        return self.pixel_matrix[row_index]

    def get_column(self, column_index):
        return [row[column_index] for row in self.pixel_matrix]

    def set_column(self, column_index, array):
        for index, value in enumerate(array):
            self.pixel_matrix[index][column_index] = value

    def print_row(self, row):
        print ' '.join('#' if x == 1 else '_' for x in row)

    def print_matrix(self):
        for row in self.pixel_matrix:
            self.print_row(row)

    def get_lit_pixel_count(self):
        return sum(sum(c for c in row) for row in self.pixel_matrix)






