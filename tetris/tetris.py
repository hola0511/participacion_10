class Tetromino:
    def __init__(self, shape):
        self.shape = shape

    def rotate_clockwise(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def print_tetromino(self):
        for row in self.shape:
            print("".join(['@' if cell else '.' for cell in row]))

    def __eq__(self, other):
        return self.shape == other.shape

    def check_similarity(self, other):
        for _ in range(4):
            if self == other:
                return True
            other.rotate_clockwise()
        return False


T_shape = [[False, False, False, False],
           [False, True, True, True],
           [False, False, True, False],
           [False, False, False, False]]

Z_shape = [[False, False, False, False],
           [False, False, True, True],
           [False, True, True, False],
           [False, False, False, False]]

T_tetromino = Tetromino(T_shape)
Z_tetromino = Tetromino(Z_shape)

T_tetromino.print_tetromino()
T_tetromino.rotate_clockwise()
print("Semejanza: ", T_tetromino.check_similarity(Z_tetromino))
T_tetromino.print_tetromino()
T_tetromino.rotate_clockwise()
print("Semejanza: ", T_tetromino.check_similarity(Z_tetromino))
T_tetromino.print_tetromino()
T_tetromino.rotate_clockwise()
print("Semejanza: ", T_tetromino.check_similarity(Z_tetromino))
T_tetromino.print_tetromino()

print("\n")
Z_tetromino.print_tetromino()

print("\nIgualdad: ", T_tetromino == T_tetromino)
print("Semejanza: ", T_tetromino.check_similarity(T_tetromino))
