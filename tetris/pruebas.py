import unittest
from tetris import Tetromino


class TestTetromino(unittest.TestCase):
    def setUp(self):
        self.T_shape = [[False, False, False, False], [False, True, True, True], [False, False, True, False], [False, False, False, False]]
        self.Z_shape = [[False, False, False, False], [False, False, True, True], [False, True, True, False], [False, False, False, False]]
        self.T_tetromino = Tetromino(self.T_shape)
        self.Z_tetromino = Tetromino(self.Z_shape)

    def test_rotation(self):
        self.T_tetromino.rotate_clockwise()
        self.assertEqual(self.T_tetromino.shape, [[False, False, False, False], [False, False, True, False], [False, True, True, False], [False, False, True, False]])

    def test_equality(self):
        self.assertTrue(self.T_tetromino == self.T_tetromino)

    def test_similarity(self):
        self.assertTrue(self.T_tetromino.check_similarity(Tetromino(self.T_shape)))
        self.assertTrue(self.T_tetromino.check_similarity(Tetromino(self.T_shape)))
        self.assertFalse(self.T_tetromino.check_similarity(self.Z_tetromino))


if __name__ == '__main__':
    unittest.main()
