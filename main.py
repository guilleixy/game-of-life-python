class Cell:
    def __init__(self, state = 0):
        self.current_state = state
        self.next_state = state
    def set_next_state(self, state):
        self.next_state = state
    def update_state(self):
        self.current_state = self.next_state

board_size = 10
board = [[Cell() for _ in range(board_size)] for _ in range(board_size)]

def main():
    generations = 10
    initialize_board()
    for gen in range(generations):
        print("Generación: ", gen + 1)
        print_board()
        process_generation()
        apply_next_generation()

def print_board():
    for row in board:
        print([cell.current_state for cell in row])

def initialize_board():
    board[4][5].current_state = 1
    board[5][5].current_state = 1
    board[6][5].current_state = 1

def process_generation():
    for x in range(board_size):
        for y in range(board_size):
            check_next_generation(x, y)

def check_next_generation(x, y):
    neighbours = cell_neighbours(x, y)
    if(board[x][y].current_state == 1):
        if neighbours > 3 or neighbours < 2:
            board[x][y].set_next_state(0)
        else:
            board[x][y].set_next_state(1)
    else:
        if neighbours == 3:
            board[x][y].set_next_state(1)
        else:
            board[x][y].set_next_state(0)
        

def cell_neighbours(x, y):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0: # Skip the current cell
                continue
            if 0 <= x + i < board_size and 0 <= y + j < board_size:
                if board[x + i][y + j].current_state == 1:
                    neighbours += 1
    return neighbours

def apply_next_generation():
    for row in board:
        for cell in row:
            cell.update_state()

main()