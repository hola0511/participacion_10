import unittest

from tetris import Tetromino, rotate_clockwise, generate_file

class TestTetromino(unittest.TestCase):

    def test_rotate(self):
        # Test that the rotate() method rotates the tetromino clockwise by 90 degrees.
        tetris = Tetromino([[1, 0], [1, 1]])
        tetris.rotate()
        self.assertEqual(tetris.shape, [[1, 1], [0, 1]])

    def test_represent(self):
        # Test that the represent() method returns a list of strings representing the tetromino, using the `@` character to represent squares.
        tetris = Tetromino([[1, 0], [1, 1]])
        representation = tetris.represent()
        self.assertEqual(representation, ["@ ", "@@"])

    def test_is_equal(self):
        # Test that the is_equal() method returns `True` if the two tetrominoes look the same in their current rotation, and `False` otherwise.
        tetris1 = Tetromino([[1, 0], [1, 1]])
        tetris2 = Tetromino([[1, 0], [1, 1]])
        self.assertTrue(tetris1.is_equal(tetris2))

        tetris2.rotate()
        self.assertFalse(tetris1.is_equal(tetris2))

    def test_is_similar(self):
        # Test that the is_similar() method returns `True` if the two tetrominoes look the same in at least one of their rotations, and `False` otherwise.
        tetris1 = Tetromino([[1, 0], [1, 1]])
        tetris2 = Tetromino([[1, 0], [1, 1]])
        self.assertTrue(tetris1.is_similar(tetris2))

        tetris2.rotate()
        self.assertTrue(tetris1.is_similar(tetris2))

        tetris2 = Tetromino([[0, 1], [1, 1]])
        self.assertFalse(tetris1.is_similar(tetris2))

class TestGenerateFile(unittest.TestCase):

    def test_generate_file(self):
        # Test that the generate_file() function generates a file with the given representation.
        representation = ["@ ", "@@"]
        generate_file(representation)

        with open("tetris.txt", "r") as f:
            file_contents = f.readlines()

        self.assertEqual(file_contents, representation)

if __name__ == "__main__":
    unittest.main()