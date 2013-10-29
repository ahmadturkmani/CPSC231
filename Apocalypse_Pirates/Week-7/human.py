import sys
import grid
import  __main__

# asks user to move or quit ###
def get_choice():
	print('[M]ove\n[Q]uit')
	move = input('What is you choice:').lower() #Makes sure input is lowercase. 
	if  move == 'q':
		sys.exit() #Exits program if user asks too. 
	elif move == 'm':
		print()
		get_move()
	else:
		print('Invalid\n')
		get_choice()
		
		
# asks user to select a piece to move
def get_move():

	board = __main__.board	
	
	grid.print_board(board)

	# Prompt user to choose piece to move
	print('Where is the piece you would like to move located?')
	col = ord(input('COLUMN\t(A-E):').lower()) - ord('a')
	row = int(input('ROW \t(1-5):')) - 1
	print()
	
	# Checks if user's location is on the board 
	if 0 <= row < grid.GRID_HEIGHT and 0 <= col < grid.GRID_WIDTH:

		# Checks if chosen location isn't blank
		if board[grid.List2Dto1D(row, col)] != grid.b:

			#If space has either a white pawn or white knight
			if board[grid.List2Dto1D(row, col)] == 'WK' or board[grid.List2Dto1D(row, col)] == 'WP':

				# ask where the user wants to place this piece
				get_endmove(row, col, board[grid.List2Dto1D(row, col)], board)

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
def get_endmove(row, col, piece, board):

	print('Where would you like to move your piece? (' + piece + ' at ' + (chr(col + ord('a')).upper()) + str(row + 1) + ')')
	new_col = ord(input('COLUMN\t(A-E):').lower()) - ord('a')
	new_row = int(input('ROW \t(1-5):')) - 1
	
	#Check if new location is within the grid 
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
def validate_move(row, col, new_row, new_col, piece, board):

	#If piece selected is a white knight
	if piece == 'WK':

		# We check if the knight is moving in an L-shape, and if the spot is either empty or has an enemy piece
		for i in range(8):	
			if (new_col == col + grid.KNIGHT_MOVE[i][0]) and (new_row == row + grid.KNIGHT_MOVE[i][1]) and ((board[grid.List2Dto1D(new_row, new_col)] == 'BK') or (board[grid.List2Dto1D(new_row, new_col)] == 'BP') or (board[grid.List2Dto1D(new_row, new_col)] == grid.b)):
				
				# if enemy is killed, taunt them!
				if (board[grid.List2Dto1D(new_row, new_col)] == 'BK' or board[grid.List2Dto1D(new_row, new_col)] == 'BP'): 
					print('~(o_o)~ Ooh, kill em! ~(o_o)~')
				return True
	#If piece is a white pawn
	elif piece == 'WP':

		# If there's nothing in front of the piece, move it up 
		if (new_col == col) and (new_row == row - 1) and (board[grid.List2Dto1D(new_row, new_col)] == grid.b):
			return True

	        # If there is an enemy to the top right, kill it 
		elif (new_col == col + 1) and (new_row == row - 1) and ((board[grid.List2Dto1D(new_row, new_col)] == 'BK') or (board[grid.List2Dto1D(new_row, new_col)] == 'BP')):
			print('~(o_o)~ Ooh, kill em! ~(o_o)~')
			return True

		# If there is an enemy to the top left, kill it 
		elif (new_col == col - 1) and (new_row == row - 1) and ((board[grid.List2Dto1D(new_row, new_col)] == 'BK') or (board[grid.List2Dto1D(new_row, new_col)] == 'BP')):
			print('~(o_o)~ Ooh, kill em! ~(o_o)~')
			return True
