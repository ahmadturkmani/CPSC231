import grid
import random
import __main__



def get_move():
	
	board = __main__.board	
	
	col = random.randint(0,4)
	row = random.randint(0,4)
	
		# Checks if ai's location is on the board 
	if 0 <= row < grid.GRID_HEIGHT and 0 <= col < grid.GRID_WIDTH:

		# Checks if chosen location isn't blank
		if board[grid.List2Dto1D(row, col)] != grid.b:

			#If space has either a black pawn or black knight
			if board[grid.List2Dto1D(row, col)] == 'BK' or board[grid.List2Dto1D(row, col)] == 'BP':

				# ask where the user wants to place this piece
				get_endmove(row, col, board[grid.List2Dto1D(row, col)], board)

			# dont try stealin other pieces
			else:
				get_move()

		# can't select an empty space
		else:
			get_move()

	# can't choose a place in China
	else:
		get_move()

def get_endmove(row, col, piece, board):
	
	if piece == "BK":
		coor = random.randint(0,7)
		#Beginning the random initialization for a move. 
		new_row = grid.KNIGHT_MOVE[coor][1] + row
		new_col = grid.KNIGHT_MOVE[coor][0] + col
		
	#Only posibilities for a pawn move. 
	elif piece == "BP":
		new_row = row + 1
		new_col = random.randint(col-1, col+1)	
	else:
		get_move()
	
	#Debugging
	print(row, col, new_row, new_col, piece)
	
	if 0 <= new_row < grid.GRID_HEIGHT and 0 <= new_col < grid.GRID_WIDTH:
		
		# if move is valid, then move the piece
		if validate_move(row, col, new_row, new_col, piece, board):
			board[grid.List2Dto1D(new_row, new_col)] = piece
			board[grid.List2Dto1D(row, col)] = grid.b
			print('Moved ' + piece + ' from ' + chr(col + ord('a')).upper() + str(row) + ' to ' + chr(new_col + ord('a')).upper() + str(new_row) + '.\n' )
			grid.print_board(board)
		
		# if not valid, tell the player. Then ask again where they want to move
		else:
			print("Not a valid move!\n")
			get_move()
	
	# same as above		
	else:
		print('Not on the board!\n')
		get_endmove(row, col, piece, board)
		
		
## Checks if the move is valid according to piece type ####	
##This needs BETTER FORMATTING, but it does the job. ##
def validate_move(row, col, new_row, new_col, piece, board):

	#If piece selected is a black knight
	if piece == 'BK':

		# We check if the knight is moving in an L-shape, and if the spot is either empty or has an enemy piece
		for i in range(8):	
			if (new_col == col + grid.KNIGHT_MOVE[i][0]) and (new_row == row + grid.KNIGHT_MOVE[i][1]) and ((board[grid.List2Dto1D(new_row, new_col)] == 'WK') or (board[grid.List2Dto1D(new_row, new_col)] == 'WP') or (board[grid.List2Dto1D(new_row, new_col)] == grid.b)):
				
				# if enemy is killed, taunt them! Makes AI a little smarter
				if (board[grid.List2Dto1D(new_row, new_col)] == 'WK' or board[grid.List2Dto1D(new_row, new_col)] == 'WP'): 
					return True
	#If piece is a Black pawn
	elif piece == 'BP':

		# If there's nothing in front of the piece, move it up 
		if (new_col == col) and (new_row == row + 1) and (board[grid.List2Dto1D(new_row, new_col)] == grid.b):
			return True

	        # If there is an enemy to the top right, kill it 
		elif (new_col == col + 1) and (new_row == row + 1) and ((board[grid.List2Dto1D(new_row, new_col)] == 'WK') or (board[grid.List2Dto1D(new_row, new_col)] == 'WP')):
			return True

		# If there is an enemy to the top left, kill it 
		elif (new_col == col - 1) and (new_row == row + 1) and ((board[grid.List2Dto1D(new_row, new_col)] == 'WK') or (board[grid.List2Dto1D(new_row, new_col)] == 'WP')):
			return True
		
