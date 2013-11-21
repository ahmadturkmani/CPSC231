import grid

KNIGHT_MOVE = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]


class node:
	parent = 'none'
	children = []
	level = 0
	board_human = []
	board_ai = []
	dic_human = {}
	dic_ai = {}
	
	def __init__(self):
		pass
		
	def add_child(self):
		new_node = node()
		self.children.append(new_node)
		new_node.parent = self
		new_node.level = self.level + 1
		return new_node
		
	def get_ancestor(self):
		cur = self
		while cur.level !=2:
			cur = cur.parent
			
		anc = cur
		
		return anc
		
	def get_valid_moves(self, board, dic, other_board, other_dic ):
			
		print(id(board_2), id(board))

		
		for piece in dic:

			loc = dic[piece]
			
			if loc != 'dead':
	
        		#If piece selected is a knight
				if piece[1] == 'K':
					
            # We check if the knight is moving in an L-shape, and if the spot is either empty or has an enemy piece
					for i in range(8):
						
						new_row = loc[0] + KNIGHT_MOVE[i][0]
						new_col = loc[1] + KNIGHT_MOVE[i][1]  
						print(piece, new_row, new_col, loc[0], loc[1])
						
						 
						if 0 <= new_col < 5 and 0 <= new_row < 5:   
							if board[new_row][new_col] == grid.b:
							
								new = self.add_child()
								
								
								board[new_row][new_col] = piece
								board[loc[0]][loc[1]] = grid.b
								dic[piece] = [new_row, new_col]
								
								print(self.level)
								if self.level%2==0:
								
									new.board_human = board
									new.board_ai = other_board
									new.last_piece = piece
									if self.level < difficulty:
										new.get_valid_moves(other_board[:], other_dic, board[:], dic)
									else:
										possible_moves.append(new)
								
								else:
									print(id(board), id(new.board_human))
									new.board_ai = board[:]
									new.board_human = other_board[:]
									new.last_piece = piece[:]
									if self.level < difficulty:
										new.get_valid_moves(other_board, other_dic, board, dic)
									else:
										possible_moves.append(new)
										
								for j in board:
									print(j)
																			
									
								board[loc[0]][loc[1]] = piece
								board[new_row][new_col] = grid.b
								
								"""for k in new.board_human:
									print(k)
								for k in new.board_ai:
									print(k)"""
								
       
				elif piece[1] == 'P':
					
					if piece[0] == 'W':
						forward = -1
					elif piece[0] == 'B':
						forward = 1
					
            # If there's nothing in front of the piece, move it up 
					new_row = loc[0] + forward
					new_col = loc[1]

					if 0 <= new_col < 5 and 0 <= new_row < 5:
					    
						if board[new_row][new_col] == grid.b and other_board[new_row][new_col] == grid.b:

							new = self.add_child()
								
							board[new_row][new_col] = piece
							board[loc[0]][loc[1]] = grid.b								
								
								
							if self.level%2==0:
								
								new.board_human = board 
								new.board_ai = other_board
								new.last_piece = piece
    
								if self.level < difficulty:
									new.get_valid_moves(other_board, other_dic, board, dic)
								else:
									possible_moves.append(new)
								
							else:
									
								new.board_ai = board 
								new.board_human = other_board
								new.last_piece = piece
								if self.level < difficulty:
									new.get_valid_moves(other_board, other_dic, board, dic)
								else:
									possible_moves.append(new)
										
    									
									
							board[loc[0]][loc[1]] = piece
							board[new_row][new_col] = grid.b
								
								
								
					new_row = loc[0] + forward
					new_col = loc[1] - 1
				
					if 0 <= new_col < 5 and 0 <= new_row < 5:
					
						if board[new_row][new_col] == grid.b and other_board[new_row][new_col] != grid.b:
								
							new = self.add_child()
								
							board[new_row][new_col] = piece
							board[loc[0]][loc[1]] = grid.b
								
								
								
							if self.level%2==0:
								
								new.board_human = board 
								new.board_ai = other_board
								new.last_piece = piece
    
								if self.level < difficulty:
									new.get_valid_moves(other_board, other_dic, board, dic)
								else:
									possible_moves.append(new)
								
							else:
									
								new.board_ai = board 
								new.board_human = other_board
								new.last_piece = piece
								if self.level < difficulty:
									new.get_valid_moves(other_board, other_dic, board, dic)
								else:
									possible_moves.append(new)
										
    									
									
							board[loc[0]][loc[1]] = piece
							board[new_row][new_col] = grid.b
								
								
					new_row = loc[0] + forward
					new_col = loc[1] + 1
				
					if 0 <= new_col < 5 and 0 <= new_row < 5:
					
						if board[new_row][new_col] == grid.b and other_board[new_row][new_col] != grid.b:
								
							new = self.add_child()
								
							board[new_row][new_col] = piece
							board[loc[0]][loc[1]] = grid.b
								
								
								
							if self.level%2==0:
								
								new.board_human = board 
								new.board_ai = board
								new.last_piece = piece
    
								if self.level < difficulty:
									new.get_valid_moves(other_board, other_dic, board, dic)
								
							else:
									
								new.board_ai = board 
								new.board_human = other_board 
										
    									
									
							board[loc[0]][loc[1]] = piece
							board[new_row][new_col] = grid.b



b = '[ ]'

board_1 = [['BP2',b,'BP3',b,b], \
                [b,b,b,b,'BK1'], \
                [b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b]]
                
board_2 = [[b,b,b,b,b], \
                [b,'WP1',b,b,b], \
                [b,b,b,b,b], \
                ['WK1',b,b,b,b], \
                [b,b,'WP3',b,b]]
                
                
dic_1 = {'BP3':[0,2], 'BK1':[1,4], 'BP2':[0,0]}
dic_2 = {'WP3':[4,2], 'WK1':[3,0], 'WP1':[1,1]}

possible_moves = []
difficulty = 1
top = node()
top.board_ai = board_2
top.board_human = board_1

top.get_valid_moves(board_2[:], dic_2, board_1[:], dic_1)

for e in possible_moves:
	print(e.last_piece, e.level)
	for o in e.board_human:
		print(o)
	print()
	for o in e.board_ai:
		print(o)
	input('...')
	
