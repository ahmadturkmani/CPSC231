#Grid Program

#Global grid constants

GRID_HEIGHT = 5
GRID_WIDTH = 5
NUM_OF_PIECES = 7 # number of pieces for each side
PIECE_W_START = [15, 21, 22, 23, 19, 20, 24] # starting location for white pieces
PIECE_W = ['WP', 'WP', 'WP', 'WP', 'WP', 'WK', 'WK'] # white pieces
PIECE_B_START = [5, 1, 2, 3 ,9, 0, 4] # starting location for white pieces
PIECE_B = ['BP', 'BP', 'BP', 'BP', 'BP', 'BK', 'BK'] # black pieces
KNIGHT_MOVE = [[2,1], 
			  [2,-1], 
			  [-2,1], 
			  [-2,-1], 
			  [1,2], 
			  [1,-2], 
			  [-1,2], 
			  [-1,-2]] # all moves a knight can make
			  
#Grid; Global variables 
b = '[]'
grid = [b for i in range(GRID_WIDTH * GRID_HEIGHT)]


# puts all pieces on board
def setup_board():
	
	# place pieces on board according to thier locations in the arrays
	for i in range(7):
		grid[PIECE_W_START[i]] = PIECE_W[i]
		grid[PIECE_B_START[i]] = PIECE_B[i]

# changes a 2d index to a 1d index in a list
def List2Dto1D(row, col):
	return (col + (row * GRID_WIDTH))

# prints out the grid		
def print_board():

	# board header
	print('__________________________');
	print('|  |  A  B  C  D  E |');
	print('--------------------------');

	for row in range(GRID_HEIGHT):
		# print row number
		print( '|0' + str(row + 1) + '| ', end = '');

		# print entire row on one line
		for col in range(GRID_WIDTH):
			print(grid[List2Dto1D(row, col)] + ' ', end = '');
		print('|');

	print();
	print('WP = White Pawn \t WK = White Knight') # tell user what piece is what
	print('BP = Black Pawn \t BK = Black Knight') 
	print()
	
	
def check_knight(): #Checks if Pawn can become a knight. 4 is the end of the grid, 0 is the other end. 
	for i in range(GRID_WIDTH):
		if grid[List2Dto1D(0, i)] == 'WP':
			grid[List2Dto1D(0, i)] = 'WK'
		if grid[List2Dto1D(4, i)] == 'BP':
			grid[List2Dto1D(4, i)] = 'BK'
	
	
	
