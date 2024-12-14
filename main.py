board = [
    [1, 0, 2, 0, 4],
    [0, 0, 3, 0, 5],
    [0, 0, 0, 0, 0],
    [0, 2, 0, 4, 0],
    [0, 1, 3, 5, 0],
]

def print_cell(cell):
    colors = [
        (0, 0, 0),      # blank
        (255, 0, 0),    # red
        (0, 255, 0),    # green
        (0, 0, 255),    # blue
        (255, 255, 0),  # yellow
        (255, 165, 0),  # orange
    ]

    if cell == 0:
        print("  ", end="")
        return

    cell_color = colors[cell] 

    red = cell_color[0]
    green = cell_color[1]
    blue = cell_color[2]

    colored_squared = f"\033[48;2;{red};{green};{blue}m  \033[0m"
    print(colored_squared, end="")

def print_board(board):
    for row in board:
        for cell in row:
            print_cell(cell)
        print()

if __name__ == "__main__":
    print_board(board)