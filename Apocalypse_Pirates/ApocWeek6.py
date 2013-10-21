#This program is the 5th week submission for Tutorial 2 Group 5's game apocalypse
#####################################################################################

#CONSTANTS
GRID_HEIGHT = 5
GRID_WIDTH = 5
NUM_OF_PIECES = 7 # number of pieces for each side
PIECE_W_START = [15, 21, 22, 23, 19, 20, 24] # starting location for white pieces
PIECE_W = ['WP', 'WP', 'WP', 'WP', 'WP', 'WK', 'WK']
PIECE_B_START = [5, 1, 2, 3 ,9, 0, 4]
PIECE_B = ['BP', 'BP', 'BP', 'BP', 'BP', 'BK', 'BK']
KNIGHT_MOVE = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]
# grid
b = '[]'
grid = [b for i in range(GRID_WIDTH * GRID_HEIGHT)]

def show_title():#Printing initialziation - intro screen

        print('###################################################')
        print('#    #   ###  #=# #==   #   #   \ / ###  === #==  #')
        print('#   #=#  #==# # # #    #=#  #    #  #==# \=  #=   #')
        print('#  #   # #    #=# #== #   # #==  #  #    ==/ #==  #')
        print('###################################################')
        print("~~~~~~~~~~TUTORIAL II COLLECTOR'S EDITION~~~~~~~~~~")
        print('\\\\\\\\\\###############################//////////')
        print()
        print('~~~~~~~~\Created by the Apocalyptic Pirates/~~~~~~~')
        print('~~~~~~~~~\________copyright 2013(c)_______/~~~~~~~~')
        print()

# puts all pieces on board
def setup_board():
	for i in range(7):
		grid[PIECE_W_START[i]] = PIECE_W[i]
		grid[PIECE_B_START[i]] = PIECE_B[i]
		
def print_board():
	# board header
	print('__________________________');
	print('|  |  A  B  C  D  E |');
	print('--------------------------');

	for row in range(GRID_HEIGHT):
		# print row number
		print( '|0' + str(row + 1) + '| ', end = '');
		# print 
		for col in range(GRID_WIDTH):
			print(grid[col + (row * GRID_WIDTH)] + ' ', end = '');
		print('|');
	print();
	print('WP = White Pawn \t WK = White Knight')
	print('BP = Black Pawn \t BK = Black Knight')
	print()

# end	

def get_choice():
	print('[M]ove\n[Q]uit')
	move = input('What is you choice:').lower()
	if  move == 'q':
		return False
	elif move == 'm':
		print()
		get_move()
		return True
	else:
		print('Invalid\n')
		return True

def get_move():
	print_board()
	print('Where is the piece you would like to move located?')
	col = ord(input('COLUMN\t(A-E):').lower()) - ord('a')
	row = int(input('ROW \t(1-5):')) - 1
	print()
	if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
		if grid[row * GRID_WIDTH + col] != b:
			if grid[row * GRID_WIDTH + col] == 'WK' or grid[row * GRID_WIDTH + col] == 'WP':
				get_endmove(row, col, grid[row * GRID_WIDTH + col])
			else:
				print("That's not your piece!\n")
				get_move()
		else:
			print('That space is empty.\n')
			get_move()
	else:
		print('Not on the board!\n')
		get_move()

def get_endmove(row, col, piece):

	print('Where would you like to move your piece? (' + piece + ' at ' + (chr(col + ord('a')).upper()) + str(row + 1) + ')')
	new_col = ord(input('COLUMN\t(A-E):').lower()) - ord('a')
	new_row = int(input('ROW \t(1-5):')) - 1
	
	if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
		if validate_move(row, col, new_row, new_col, piece):
			grid[new_col + new_row * GRID_WIDTH] = piece
			grid[col + row * GRID_WIDTH] = b
			print_board()
		else:
			print("Not a valid move!\n")
			get_endmove(row, col, piece)
	else:
		print('Not on the board!\n')
		get_endmove(row, col, piece)
		
## Checks if the move is valid according to piece type ####	
def validate_move(row, col, new_row, new_col, piece):

	if piece == 'WK':
		for i in range(8):	
			if (new_col == col + KNIGHT_MOVE[i][0]) and (new_row == row + KNIGHT_MOVE[i][1]) and ((grid[new_col + new_row * GRID_WIDTH] == 'BK') or (grid[new_col + new_row * GRID_WIDTH] == 'BP') or (grid[new_col + new_row * GRID_WIDTH] == b)):
				return True			
	elif piece == 'WP':
		if (new_col == col) and (new_row == row - 1) and (grid[new_col + new_row * GRID_WIDTH] == b):
			return True
		elif (new_col == col + 1) and (new_row == row - 1) and ((grid[new_col + new_row * GRID_WIDTH] == 'BK') or (grid[new_col + new_row * GRID_WIDTH] == 'BP')):
			return True
		elif (new_col == col - 1) and (new_row == row - 1) and ((grid[new_col + new_row * GRID_WIDTH] == 'BK') or (grid[new_col + new_row * GRID_WIDTH] == 'BP')):
			return True
	
def main():
	setup_board()
	print_board()
	while get_choice():
			pass
			
main()
