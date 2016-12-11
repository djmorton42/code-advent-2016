import unittest
from screen import Screen

class TestScreen(unittest.TestCase):
    
    def test_constructor(self):
        screen = Screen(3, 3)

        self.assertEqual(screen.get_row(0), [0, 0, 0])
        self.assertEqual(screen.get_row(1), [0, 0, 0])
        self.assertEqual(screen.get_row(2), [0, 0, 0])

        screen.print_matrix()

    def test_rotate_row(self):
        screen = Screen(3, 10)

        screen.set_pixel(1, 1, 1)
        screen.set_pixel(4, 1, 1)
        screen.set_pixel(8, 1, 1)

        screen.rotate_row(1, 4)
 
        self.assertEqual(screen.get_row(1), [0, 0, 1, 0, 0, 1, 0, 0, 1, 0])

        screen.print_matrix()

    def test_rotate_column(self):
        screen = Screen(3, 3)

        screen.set_pixel(1, 0, 1)
        screen.set_pixel(1, 2, 1)

        screen.rotate_column(1, 1)

        self.assertEqual(screen.get_column(1), [1, 1, 0])

        screen.print_matrix()

    def test_turn_on_rect(self):
        screen = Screen(3, 3)
        screen.turn_on_rect(2, 2)

        self.assertEqual(screen.get_row(0), [1, 1, 0])
        self.assertEqual(screen.get_row(1), [1, 1, 0])
        self.assertEqual(screen.get_row(2), [0, 0, 0])

        screen.print_matrix()


if __name__ == '__main__':
    unittest.main()

