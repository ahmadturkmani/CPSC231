#Comments go here 

#Global Variables
b = '[ ]'
GRID_HEIGHT = 5
GRID_WIDTH = 5
KNIGHT_MOVE = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]

#Grid Class

class Grid:
	def __init__(self):
	

		self.board = [[b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b]]
	

	def save_grid(_file, header, grid):
	# Saves the grid to an open file
	
		_file.write(header)	
	
		for i in grid:
			
			for j in i:
				
				_file.write(str(j))
				
			_file.write('\n')



			
		
	# Used for loading a grid from a file 
	def load_file(_file):
		
		grid = []
		
		_file.readline() # reads the header
		
		#loops through each line of the file
		for i in range(GRID_WIDTH):
			line = _file.readline()[:-1]
			grid.append(list(line))
				
		return grid
		
	#initialize board 
	def setup_board(self, piece_loc):
		
		for i in piece_loc:
			
			location = piece_loc[i]
			
			if location != 'dead':
            #row and column are equal to loc's x and y co-ordinates (loc is a list with only two values)
				row = int(location[0])
				col = int(location[1])
				self.board[row][col] = i
			
   #Changes the selected piece's location and updates the grid as well as returning the new co-ordinates of all the pieces(piece_loc)
	def move_piece(self, row, col, piece, piece_loc):
		piece_loc[piece] = [row, col]
		self.update_grid(piece_loc) 
		return piece_loc
		
	def update_grid(self, piece_loc):			
		self.board = [[b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b]]
		for i in piece_loc:
			if piece_loc[i] != 'dead':
				self.board[piece_loc[i][0]][piece_loc[i][1]] = i
	
	def validate_location(self, row, col, new_row, new_col, piece, p_loc):
	
      #If piece selected is a knight
		#If piece selected is a knight
		if piece[1] == 'K':
			#Change 'BK' check to 'K' | WE DONT WANT IT TO KILL ITS OWN PIECE
            # We check if the knight is moving in an L-shape, and if the spot is either empty or has an enemy piece
			for i in range(8):        
				if (new_col == col + KNIGHT_MOVE[i][0]) and (new_row == row + KNIGHT_MOVE[i][1]) and (self.board[new_row][new_col] == b):
						# if enemy is killed, taunt them!
							return True
      #If the piece is a pawn
		elif piece[1] == 'P':
			#For white, forward is negative
			if piece[0] == 'W':
				forward = -1
			#Vice-versa 
			elif piece[0] == 'B':
				forward = 1
			
            # If there's nothing in front of the piece, move it up 
			if (new_col == col) and (new_row == row + forward) and (self.board[new_row][new_col] == b):
				return True

            # If there is an enemy to the top right, kill it 
			elif (new_col == col + 1) and (new_row == row+ forward) and (self.board[new_row][new_col][0] == 'B'):
				return True

            # If there is an enemy to the top left, kill it 
			elif (new_col == col - 1) and (new_row == row + forward) and (self.board[new_row][new_col][0] == 'B'):
				return True
                    
                    
#Where the choosen piece will land                   
def finalize_move(human_grid, ai_grid, last_human, last_ai, dic_human, dic_ai):
	for i in range(len(human_grid)):
		for j in range(len(human_grid[i])):
			if human_grid[i][j]== b or ai_grid[i][j] == b:
				pass
			else:
				if human_grid[i][j] == last_human:
					#Checks if a both pieces from the human and ai are in the same place
					if ai_grid[i][j] == last_ai:
						#If human piece is higher ranked than ai piece, ai piece dies
						if last_human[1] < last_ai[1]:
							ai_grid[i][j] == b
							dic_ai[last_ai] = 'dead'
							print('ai dead')
						#If human piece is ranked lower than ai piece, human piece dies
						elif last_human[1] > last_ai[1]:
							human_grid[i][j] == b
							dic_human[last_human] = 'dead'
							print('u dead')
						#Otherwise both pieces die simultaneously 
						else:
							human_grid[i][j] == b
							dic_human[last_human] = 'dead'
							ai_grid[i][j] == b
							dic_ai[last_ai] = 'dead'
							print('both dead')
					#Ai piece dies in this case	
					else:
						ai_grid[i][j] == b
						dic_ai[last_ai] = 'dead'
						print('ai dead')
				#Human piece dies 
				else:
					human_grid[i][j] == b
					dic_human[last_human] = 'dead'
					print('you dead')
	return human_grid, ai_grid, dic_human, dic_ai

#Prints the combined grid of the human's and ai's
def print_grid(human_grid, ai_grid):
	
	for i in range(len(human_grid)):
		for j in range(len(human_grid[i])):
			#If human piece exists at specified location, show it 
			if human_grid[i][j] != b:
				print(human_grid[i][j], end = "")
			#If ai piece exists in its board and human's doesn't, then show ai piece
			elif ai_grid[i][j] != b:
				print(ai_grid[i][j], end = "")
			else:
				print(b, end = "")
		print()


			
			
			
			
				
