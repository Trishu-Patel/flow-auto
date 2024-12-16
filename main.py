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
    def is_blank(self):
        return self.color == BLACK

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

    @property
    def surrounding_cells(self):
        return 

    def print(self):
        r = self.color[0]
        g = self.color[1]
        b = self.color[2]

        print(f"\033[48;2;{r};{g};{b}m  \033[0m", end="")


class Path:
    def __init__(self, start_cell):
        self.path = [start_cell]
        self.color = start_cell.color

    @property
    def head(self):
        return self.path[-1]

    @property
    def neck(self):
        if len(self.path) == 1:
            return self.path[-1]

        return self.path[-2]

    def print(self):
        self.head.print()
        print(" ", end="")

        for cell in self.path:
            print(f"({cell.x}, {cell.y}) ->")

    def expand(self):
        surrounding_cells = [self.head.top_cell, self.head.left_cell, self.head.bottom_cell, self.head.right_cell]

        surrounding_cells = [cell for cell in surrounding_cells if cell != None]
        surrounding_cells = [cell for cell in surrounding_cells if cell != self.neck]

        for cell in surrounding_cells:
            if cell.color == self.color:
                return self

        surrounding_cells = [cell for cell in surrounding_cells if cell.is_blank]

        if len(surrounding_cells) != 1:
            return self

        next_cell = surrounding_cells[0]

        next_cell.color = self.color
        self.path.append(next_cell)

        return self.expand()

class Free_Flow:
    def __init__(self, board):
        self.board = []
        self.size = len(board)
        self.paths = []

        for y, row in enumerate(board):
            board_row = []
            for x, color in enumerate(row):
                cell = Cell(color, x, y, self)
                board_row.append(cell)

                if not cell.is_blank:
                    self.paths.append(Path(cell))

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

    def solve(self):
        for path in self.paths:
            path.expand()

        for row in self.board:
            for cell in row:
                if cell.is_blank:
                    self.solve()


if __name__ == "__main__":

    board = [
        [BLACK, BLACK, BLACK, BLACK, BLACK, ORANGE],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, YELLOW, RED, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, GREEN, BLACK, YELLOW],
        [BLACK, GREEN, BLACK, ORANGE, RED, BLUE],
        [BLACK, BLACK, BLACK, BLUE, BLACK, BLACK],
    ]

    game = Free_Flow(board)

    game.print()

    game.solve()
    game.print()
