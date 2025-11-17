class Cell:
    # initialization of an individual cell
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch = []
    # change cell value
    def set_cell_value(self, value):
        self.value = value
        self.sketch = []
    # change sketched/user-input cell value
    def set_sketched_value(self, value):
        self.value = 0
        self.sketch.append(value)
    # draw cell onscreen, using row and col for location
    def draw(self):
        pass