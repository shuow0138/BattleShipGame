class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def to_str(self):
        return f"({self.row}, {self.col})"
