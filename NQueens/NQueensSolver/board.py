class Board:
    def __init__(self, size):
        self.positions = [[' ' for i in range(size)] for j in range(size)]
        self.size = size

    # Method for printing out the board, for debug or for displaying solutions
    def print_board(self):
        # Create divider line for printing board to console
        div_line = "+"
        for i in range(self.size):
            div_line += "---+"

        print(div_line)

        # Create and print lines based on the board object
        for i in range(self.size):
            board_line = "|"
            for j in range(self.size):
                board_line += " " + self.positions[i][j] + " |"
            print(board_line)
            print(div_line)

    def remove_queen(self, row, col):
        self.positions[row][col] = ' '

    def place_queen(self, row, col):
        self.positions[row][col] = 'Q'


# Test of board functionality
board = Board(8)
board.place_queen(0, 2)
board.place_queen(3, 4)
board.place_queen(0, 1)
board.remove_queen(0, 1)
board.print_board()
