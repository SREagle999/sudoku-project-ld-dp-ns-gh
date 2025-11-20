class Board:
    # initialization of a game board
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
    # draws outline of 9x9 board, outlines all 3x3 blocks, and draws every cell
    def draw(self):
        pass
    # marks the cell of row and col, allowing value and sketched value editing
    def select(self, row, col):
        pass

    # returns tuple of row and col of cell clicked; otherwise None
    def click(self, x, y):
        pass

    # clears value cell (can only remove cell & sketched values filled themselves)
    def clear(self):
        pass

    # sets sketch value of current selection; displayed top left
    def sketch(self, value):
        pass

    # sets value of current selected cell equal to user entered value; called by Enter key
    def place_number(self, value):
        pass

    # resets all board cells to original value (0 if cleared)
    def reset_to_original(self):
        pass

    # returns Boolean value indicating whether board is full
    def is_full(self):
        pass

    # updates 2D board with cell values
    def update_board(self):
        pass

    # finds empty cell; returns row & column tuple (x,y)
    def find_empty(self):
        pass

    # checks if board is correct
    def check_board(self):
        pass



