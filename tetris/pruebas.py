import unittest
from tetris import Tetromino


class TestTetromino(unittest.TestCase):
    def setUp(self):
        self.T_shape = [[False, False, False, False], [False, True, True, True], [False, False, True, False], [False, False, False, False]]
        self.S_shape = [[False, False, False, False], [False, False, True, True], [False, True, True, False], [False, False, False, False]]
        self.T_tetromino = Tetromino(self.T_shape)
        self.S_tetromino = Tetromino(self.S_shape)

    def test_rotation(self):
        self.T_tetromino.rotar()
        self.assertEqual(self.T_tetromino.shape, [[False, False, True, False], [False, True, True, False], [False, False, True, False], [False, False, False, False]])

    def test_equality(self):
        self.assertTrue(self.T_tetromino == self.T_tetromino)

    def test_similarity(self):
        self.assertTrue(self.T_tetromino.similar(Tetromino(self.T_shape)))
        self.assertTrue(self.T_tetromino.similar(Tetromino(self.T_shape)))
        self.assertFalse(self.T_tetromino.similar(self.S_tetromino))


if __name__ == '__main__':
    unittest.main()
