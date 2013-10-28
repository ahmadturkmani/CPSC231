import grid
import random

def get_move():
	
	col = random.randint(0,4)
	row = random.randint(0,4)
	
		# Checks if user's location is on the board 
	if 0 <= row < grid.GRID_HEIGHT and 0 <= col < grid.GRID_WIDTH:

		# Checks if chosen location isn't blank
		if grid.grid[grid.List2Dto1D(row, col)] != grid.b:

			#If space has either a white pawn or white knight
			if grid.grid[grid.List2Dto1D(row, col)] == 'BK' or grid.grid[grid.List2Dto1D(row, col)] == 'BP':

				# ask where the user wants to place this piece
				get_endmove(row, col, grid.grid[grid.List2Dto1D(row, col)])

			# dont try stealin other pieces
			else:
				get_move()

		# can't select an empty space
		else:
			get_move()

	# can't choose a place in China
	else:
		get_move()

def get_endmove(row, col, piece):
	if piece == "BK":
		coor = random.randint(0,7)
		new_row = grid.KNIGHT_MOVE[coor][1] + row
		new_col = grid.KNIGHT_MOVE[coor][0] + col
		
	elif piece == "BP":
		new_row = row + 1
		new_col = random.randint(col-1, col+1)	
	else:
		get_move()
	print(row, col, new_row, new_col, piece)
	if 0 <= new_row < grid.GRID_HEIGHT and 0 <= new_col < grid.GRID_WIDTH:
		
		# if move is valid, then move the piece
		if validate_move(row, col, new_row, new_col, piece):
			grid.grid[grid.List2Dto1D(new_row, new_col)] = piece
			grid.grid[grid.List2Dto1D(row, col)] = grid.b
			print('Moved ' + piece + ' from ' + chr(col + ord('a')).upper() + str(row) + ' to ' + chr(new_col + ord('a')).upper() + str(new_row) + '.\n' )
			grid.print_board()
		
		# if not valid, tell the player. Then ask again where they want to move
		else:
			print("Not a valid move!\n")
			get_move()
	
	# same as above		
	else:
		print('Not on the board!\n')
		get_endmove(row, col, piece)
		
		
## Checks if the move is valid according to piece type ####	
def validate_move(row, col, new_row, new_col, piece):

	#If piece selected is a white knight
	if piece == 'BK':

		# We check if the knight is moving in an L-shape, and if the spot is either empty or has an enemy piece
		for i in range(8):	
			if (new_col == col + grid.KNIGHT_MOVE[i][0]) and (new_row == row + grid.KNIGHT_MOVE[i][1]) and ((grid.grid[grid.List2Dto1D(new_row, new_col)] == 'WK') or (grid.grid[grid.List2Dto1D(new_row, new_col)] == 'WP') or (grid.grid[grid.List2Dto1D(new_row, new_col)] == grid.b)):
				
				# if enemy is killed, taunt them!
				if (grid.grid[grid.List2Dto1D(new_row, new_col)] == 'WK' or grid.grid[grid.List2Dto1D(new_row, new_col)] == 'WP'): 
					return True
	#If piece is a Black pawn
	elif piece == 'BP':

		# If there's nothing in front of the piece, move it up 
		if (new_col == col) and (new_row == row + 1) and (grid.grid[grid.List2Dto1D(new_row, new_col)] == grid.b):
			return True

	        # If there is an enemy to the top right, kill it 
		elif (new_col == col + 1) and (new_row == row + 1) and ((grid.grid[grid.List2Dto1D(new_row, new_col)] == 'WK') or (grid.grid[grid.List2Dto1D(new_row, new_col)] == 'WP')):
			return True

		# If there is an enemy to the top left, kill it 
		elif (new_col == col - 1) and (new_row == row + 1) and ((grid.grid[grid.List2Dto1D(new_row, new_col)] == 'WK') or (grid.grid[grid.List2Dto1D(new_row, new_col)] == 'WP')):
			return True
		
