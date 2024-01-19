class Ship:
    def __init__(self, start_position, orientation, size):
        self.start_position = start_position
        self.orientation = orientation
        self.size = size

    def to_str(self):
        return f"Ship:{self.start_position}, {self.orientation}, {self.size}"
