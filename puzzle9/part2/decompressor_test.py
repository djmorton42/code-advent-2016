import unittest
from decompressor import Decompressor

class TestDecompressor(unittest.TestCase):

    def test_calculate_decompressed_length(self):
        decompressor = Decompressor()

        self.assertEqual(decompressor.calculate_decompressed_length('ADVENT'), 6)
        self.assertEqual(decompressor.calculate_decompressed_length('X(8x2)(3x3)ABCY'), 20)
        self.assertEqual(decompressor.calculate_decompressed_length('(27x12)(20x12)(13x14)(7x10)(1x12)A'), 241920)
        self.assertEqual(decompressor.calculate_decompressed_length('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'), 445)

if __name__ == '__main__':
    unittest.main()

