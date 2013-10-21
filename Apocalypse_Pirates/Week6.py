#This program is the 6th week submission for Tutorial 2 Group 5's game apocalypse
#####################################################################################

#CONSTANTS
GRID_HEIGHT = 5
GRID_WIDTH = 5
NUM_OF_PIECES = 7 # number of pieces for each side
PIECE_W_START = [15, 21, 22, 23, 19, 20, 24] # starting location for white pieces
PIECE_W = ['WP', 'WP', 'WP', 'WP', 'WP', 'WK', 'WK'] # white pieces
PIECE_B_START = [5, 1, 2, 3 ,9, 0, 4] # starting location for white pieces
PIECE_B = ['BP', 'BP', 'BP', 'BP', 'BP', 'BK', 'BK'] # black pieces
KNIGHT_MOVE = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]] # all moves a knight can make
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

# changes a 2d index to a 1d index in a list
def List2Dto1D(row, col):
	return (col + (row * GRID_WIDTH))

# puts all pieces on board
def setup_board():
	
	# place pieces on board according to thier locations in the arrays
	for i in range(7):
		grid[PIECE_W_START[i]] = PIECE_W[i]
		grid[PIECE_B_START[i]] = PIECE_B[i]

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


# asks user to move or quit ###
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
		
		
# asks user to select a piece to move ###
def get_move():
	
	print_board()

	# Prompt user to choose piece to move
	print('Where is the piece you would like to move located?')
	col = ord(input('COLUMN\t(A-E):').lower()) - ord('a')
	row = int(input('ROW \t(1-5):')) - 1
	print()
	
	# Checks if user's location is on the board 
	if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:

		# Checks if chosen location isn't blank
		if grid[List2Dto1D(row, col)] != b:

			#If space has either a white pawn or white knight
			if grid[List2Dto1D(row, col)] == 'WK' or grid[List2Dto1D(row, col)] == 'WP':

				# ask where the user wants to place this piece
				get_endmove(row, col, grid[List2Dto1D(row, col)])

			# dont try stealin other pieces
			else:
				print("That's not your piece!\n")
				get_move()

		# can't select an empty space
		else:
			print('That space is empty.\n')
			get_move()

	# can't choose a place in China
	else:
		print('Not on the board!\n')
		get_move()
		
		
# Asks user to place the piece selected in get_move() ###
def get_endmove(row, col, piece):

	print('Where would you like to move your piece? (' + piece + ' at ' + (chr(col + ord('a')).upper()) + str(row + 1) + ')')
	new_col = ord(input('COLUMN\t(A-E):').lower()) - ord('a')
	new_row = int(input('ROW \t(1-5):')) - 1
	
	#Check if new location is within the grid 
	if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
		
		# if move is valid, then move the piece
		if validate_move(row, col, new_row, new_col, piece):
			grid[List2Dto1D(new_row, new_col)] = piece
			grid[List2Dto1D(row, col)] = b
			print('Moved ' + piece + ' from ' + chr(col + ord('a')).upper() + str(row) + ' to ' + chr(new_col + ord('a')).upper() + str(new_row) + '.\n' )
			print_board()
		
		# if not valid, tell the player. Then ask again where they want to move
		else:
			print("Not a valid move!\n")
			get_endmove(row, col, piece)
	
	# same as above		
	else:
		print('Not on the board!\n')
		get_endmove(row, col, piece)
		
		
## Checks if the move is valid according to piece type ####	
def validate_move(row, col, new_row, new_col, piece):

	#If piece selected is a white knight
	if piece == 'WK':

		# We check if the knight is moving in an L-shape, and if the spot is either empty or has an enemy piece
		for i in range(8):	
			if (new_col == col + KNIGHT_MOVE[i][0]) and (new_row == row + KNIGHT_MOVE[i][1]) and ((grid[List2Dto1D(new_row, new_col)] == 'BK') or (grid[List2Dto1D(new_row, new_col)] == 'BP') or (grid[List2Dto1D(new_row, new_col)] == b)):
				
				# if enemy is killed, taunt them!
				if (grid[List2Dto1D(new_row, new_col)] == 'BK' or grid[List2Dto1D(new_row, new_col)] == 'BP'): 
					print('~(o_o)~ Ooh, kill em! ~(o_o)~')
				return True
	#If piece is a white pawn
	elif piece == 'WP':

		# If there's nothing in front of the piece, move it up 
		if (new_col == col) and (new_row == row - 1) and (grid[List2Dto1D(new_row, new_col)] == b):
			return True

	        # If there is an enemy to the top right, kill it 
		elif (new_col == col + 1) and (new_row == row - 1) and ((grid[List2Dto1D(new_row, new_col)] == 'BK') or (grid[List2Dto1D(new_row, new_col)] == 'BP')):
			print('~(o_o)~ Ooh, kill em! ~(o_o)~')
			return True

		# If there is an enemy to the top left, kill it 
		elif (new_col == col - 1) and (new_row == row - 1) and ((grid[List2Dto1D(new_row, new_col)] == 'BK') or (grid[List2Dto1D(new_row, new_col)] == 'BP')):
			print('~(o_o)~ Ooh, kill em! ~(o_o)~')
			return True

def get_winner():
	if_won = True
	for i in range(GRID_HEIGHT * GRID_WIDTH):
		if grid[i] == "BP" or grid[i] ==  "BK":
			if_won = False
	if if_won == True:
		print(	'/---------------------------\\n|----------YOU WIN!----------|\n==============================\n| | | | | | | | | | | | | | ||\n******************************\n             | |                \n       ==============')

def main():
	
	# add pieces to board
	setup_board()

	# print the board
	print_board()

	# game loop. Play till user decides to quit
	while get_choice():
			get_winner()
			
main()
