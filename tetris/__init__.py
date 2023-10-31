class Tetromino:
    def __init__(self, shape):
        self.shape = shape

    def rotate(self):
        self.shape = rotate_clockwise(self.shape)

    def represent(self):
        # Represent the tetromino using the `@` character.
        representation = []
        for row in self.shape:
            representation.append("".join(["@" if square else " " for square in row]))
        return representation

    def is_equal(self, other):
        # Two tetrominoes are equal if they look the same in their current rotation.
        return self.shape == other.shape

    def is_similar(self, other):
        # Two tetrominoes are similar if they look the same in at least one of their rotations.
        for rotation in range(4):
            if self.shape == other.rotate(rotation):
                return True
        return False

def rotate_clockwise(shape):
    # Rotate the shape clockwise by 90 degrees.
    new_shape = []
    for i in range(len(shape[0]) - 1, -1, -1):
        row = []
        for j in range(len(shape)):
            row.append(shape[j][i])
        new_shape.append(row)
    return new_shape

def generate_file(representation):
    # Generate a file with the given representation.
    with open("tetris.txt", "w") as f:
        for row in representation:
            f.write(row + "\n")

def main():
    # Create a tetromino.
    tetris = Tetromino([[1, 0], [1, 1]])

    # Rotate the tetromino twice.
    tetris.rotate()
    tetris.rotate()

    # Represent the tetromino.
    representation = tetris.represent()

    # Print the representation to the console.
    for row in representation:
        print(row)

    # Generate a file with the representation.
    generate_file(representation)

if __name__ == "__main__":
    main()