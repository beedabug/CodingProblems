'''
Created on Nov 30, 2018

@author: belinda welch


0 - Hidden no mine
1 - Hidden and mine
2 - Unhidden no mine
3 - Unhidden and mine
4 - Marked as a mine


    0 1 2 3 4 5 6 7 8 9 0 1
    
 0  0 0 0 0 0 0 0 0 1 2 2 2
 1  0 0 0 0 0 0 0 0 0 1 2 2
 2  0 0 0 0 0 0 0 0 1 2 2 2
 3  0 0 0 0 0 0 0 0 0 1 2 1
 4  0 0 0 0 0 0 0 0 0 0 1 0
 5  0 0 0 0 0 0 0 0 0 0 0 0
 6  0 0 0 0 0 0 0 0 0 0 0 0
 7  0 0 0 0 0 0 0 0 0 0 0 0
 8  0 0 0 0 0 0 0 0 0 0 0 0
 9  0 0 0 0 0 0 0 0 0 0 0 0

'''

# define classes
class ClickPosition:
    def __init(self, x, y):
        self.x = x
        self.y = y
    

class Board:
    def __init__(self, length, width, mines):
        self.length = length
        self.width = width
        self.board = []
                
        for x in range(length):
            self.board.append([0] * width) 
            
        for position in mines:
            self.board[position[0]][position[1]] = 1
        
    def get_val(self, position=(0,0), move=(0, 0)):
        return self.board[position[0]+move[0]][position[1]+move[1]]
    
    def set_val(self, position, new):
        self.board[position[0]][position[1]] = new
        
    def print_board(self):
        for x in range(self.length):
            print(self.board[x])

# helper function
def in_bounds(board, pair):
    if pair[0] <= board.length - 1 and pair[0] >= 0 and pair[1] <= board.width - 1 and pair[1] >= 0:
        return True

# solve dynamic programming problem
def check_pos(board, position):
    adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for item in adjacent: 
        neighbor = tuple(map(sum, zip(position, item))) # sums two tuples position & item
        if in_bounds(board, neighbor):
            if board.get_val(neighbor) == 0:
                board.set_val(neighbor, 2)     
                check_pos(board, neighbor)

def process_board(board, click_pos):
    val = board.get_val(click_pos)
    if val == 0:
        board.set_val(click_pos, 2) 
        check_pos(board, click_pos) 
    elif val == 1:
        board.set_val(click_pos, 3)
    
    return board

# driver 
my_board = Board(10, 12, [(0, 8), (1, 9), (2, 8), (3, 9), (4, 10), (3, 11)])
my_board = process_board(my_board, (2, 10))
my_board.print_board()