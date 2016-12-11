import unittest
from decompressor import Decompressor

class TestDecompressor(unittest.TestCase):
   
    def test_decompressor(self):
        decompressor = Decompressor()

        self.assertEqual(decompressor.decompress('ADVENT'), 'ADVENT')
        self.assertEqual(decompressor.decompress('A(1x5)BC'), 'ABBBBBC')
        self.assertEqual(decompressor.decompress('(3x3)XYZ'), 'XYZXYZXYZ')
        self.assertEqual(decompressor.decompress('A(2x2)BCD(2x2)EFG'), 'ABCBCDEFEFG')
        self.assertEqual(decompressor.decompress('(6x1)(1x3)A'), '(1x3)A')
        self.assertEqual(decompressor.decompress('X(8x2)(3x3)ABCY'), 'X(3x3)ABC(3x3)ABCY')

if __name__ == '__main__':
    unittest.main()

