import unittest
from main import average_blocks

class TestAverageBlocks(unittest.TestCase):

    def test_2x2x2_cube(self):
        cube = [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]]
        ]
        # Each block is one value here:
        expected = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
        result = average_blocks(cube)
        self.assertEqual(result, expected)

    def test_4x4x4_uniform(self):
        cube = [[[1 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        expected = [1.0] * 8
        result = average_blocks(cube)
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        bad_cube = [[[1, 2], [3, 4]]]
        with self.assertRaises(ValueError):
            average_blocks(bad_cube)

if __name__ == '__main__':
    unittest.main()
