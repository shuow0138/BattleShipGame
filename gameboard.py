class GameBoard:
    def __init__(self, max_row, max_col):
        self.max_row = max_row
        self.max_col = max_col
        self.gameboard = [[[None, None]
                           for _ in range(max_row + 1)] for _ in range(max_col + 1)]
        self.successAttackCount = 0

    def add_ship(ship):
        return None

    def attack_ship(position):
        return None

    def get_num_success_attacks():
        return None

    def check_all_sunk():
        return None

    def to_str(gamenboard):
        return None
