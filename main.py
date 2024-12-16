from PIL import Image, ImageDraw

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)


class Cell:
    def __init__(self, color, x, y, board):
        self.color = color
        self.x = x
        self.y = y
        self.board = board

    @property
    def top_cell(self):
        return self.board.get_cell(self.x, self.y - 1)

    @property
    def left_cell(self):
        return self.board.get_cell(self.x - 1, self.y)

    @property
    def bottom_cell(self):
        return self.board.get_cell(self.x, self.y + 1)

    @property
    def right_cell(self):
        return self.board.get_cell(self.x + 1, self.y)

    def print(self):
        r = self.color[0]
        g = self.color[1]
        b = self.color[2]

        print(f"\033[48;2;{r};{g};{b}m  \033[0m", end="")

        print(f" ({self.x}, {self.y})")

    def deep_print(self):
        r = self.color[0]
        g = self.color[1]
        b = self.color[2]

        print(f"\033[48;2;{r};{g};{b}m  \033[0m", end="")

        print(f" ({self.x}, {self.y})")

        print("top: ", end="")
        if self.top_cell != None:
            self.top_cell.print()
        else:
            print("None")

        print("left: ", end="")
        if self.left_cell != None:
            self.left_cell.print()
        else:
            print("None")

        print("bottom: ", end="")
        if self.bottom_cell != None:
            self.bottom_cell.print()
        else:
            print("None")

        print("right: ", end="")
        if self.right_cell != None:
            self.right_cell.print()
        else:
            print("None")


class Free_Flow:
    def __init__(self, board):
        self.board = []
        self.size = len(board)

        for y, row in enumerate(board):
            board_row = []
            for x, color in enumerate(row):
                cell = Cell(color, x, y, self)
                board_row.append(cell)
            self.board.append(board_row)

    def get_cell(self, x: int, y: int) -> Cell | None:
        if x < 0 or x >= self.size:
            return None

        if y < 0 or y >= self.size:
            return None

        return self.board[y][x]

    def print(self):
        for row in self.board:
            for cell in row:
                cell.print()
            print()


if __name__ == "__main__":

    board = [
        [BLUE, RED, RED, RED, ORANGE],
        [BLUE, RED, YELLOW, YELLOW, ORANGE],
        [BLUE, RED, YELLOW, ORANGE, ORANGE],
        [BLUE, RED, ORANGE, ORANGE, GREEN],
        [BLUE, BLUE, GREEN, GREEN, GREEN],
    ]

    game = Free_Flow(board)

    game.get_cell(0, 0).deep_print()
