class Tetromino:
    def __init__(self, shape):
        self.shape = shape

    def rotar(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def mostrar_tetromino(self):
        for row in self.shape:
            print("".join(['@' if cell else '.' for cell in row]))

    def __eq__(self, other):
        return self.shape == other.shape

    def similar(self, other):
        for _ in range(4):
            if self == other:
                return True
            other.rotar()
        return False


T_shape = [[False, False, False, False],
           [False, True, True, True],
           [False, False, True, False],
           [False, False, False, False]]

S_shape = [[False, False, False, False],
           [False, False, True, True],
           [False, True, True, False],
           [False, False, False, False]]


T_tetromino = Tetromino(T_shape)
S_tetromino = Tetromino(S_shape)

T_tetromino.mostrar_tetromino()
T_tetromino.rotar()
print("\n")
T_tetromino.mostrar_tetromino()
T_tetromino.rotar()
print("\n")
T_tetromino.mostrar_tetromino()
T_tetromino.rotar()
print("\n")
T_tetromino.mostrar_tetromino()

print("\n")
S_tetromino.mostrar_tetromino()

print("Igualdad: ", T_tetromino == T_tetromino)
print("Igualdad: ", T_tetromino == S_tetromino)
print("Semejanza: ", T_tetromino.similar(T_tetromino))
print("Semejanza: ", T_tetromino.similar(S_tetromino))
