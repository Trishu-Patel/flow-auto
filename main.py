class Board:
    def __init__(self, board):
        self.board = []

        for y, row in enumerate(board):
            board_row = []
            for x, cell in enumerate(row):
                board_row.append(Cell(cell, x, y))
            self.board.append(board_row)

        self.size = len(board)

    def print_board(self):
        for row in self.board:
            for cell in row:
                cell.print()
            print()

class Cell:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    @property
    def is_blank(self):
        return self.value == 0
    
    @property
    def color(self):
        colors = [
            (0, 0, 0),      # blank
            (255, 0, 0),    # red
            (0, 255, 0),    # green
            (0, 0, 255),    # blue
            (255, 255, 0),  # yellow
            (255, 165, 0),  # orange
        ]

        return colors[self.value]
    
    def print(self):
        if self.value == 0:
            print("  ", end="")
            return
        
        red = self.color[0]
        green = self.color[1]
        blue = self.color[2]

        colored_squared = f"\033[48;2;{red};{green};{blue}m  \033[0m"
        print(colored_squared, end="")

    
board = [
    [1, 0, 2, 0, 4],
    [0, 0, 3, 0, 5],
    [0, 0, 0, 0, 0],
    [0, 2, 0, 4, 0],
    [0, 1, 3, 5, 0],
]

if __name__ == "__main__":
    board = Board(board)

    board.print_board()