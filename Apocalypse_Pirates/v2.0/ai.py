import random
import grid

KNIGHT_MOVES = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]
possible_moves = []
difficulty = 4

class node:
	
	def __init__(self):
	
		self.children = list()	# list of children objects
		self.parent = 'none'	# parent object
		self.level = 0			# level on tree
		self.state = 'none'		# which player
		self.dic_human = {}		# human pieces
		self.dic_ai = {}		# ai pieces
	
	### adds a child node, and returns it's value ###
	def add_child(self):
	
		# create the child node
		new_node = node()
		
		# setup the child, add variables, and add it to children
		self.children.append(new_node)
		new_node.parent = self
		new_node.level = self.level + 1
		
		return new_node
	
	### gets the original move to reach this state ###
	def get_ancestor(self, wanted_level):
	
		cur = self # start with me!
		
		# loop through ancestry until we find desired ancestor
		while cur.level != wanted_level:
			cur = cur.parent
			
		return cur
	
	### grows the tree to desired degree, and adds them to possible_moves
	def grow_tree(self):
		
		if self.state == 'original':
		
			child = self.add_child()
			child.dic_human = dict(self.dic_human)
			child.dic_ai = dict(self.dic_ai)
			child.state = 'human'
			child.last_piece = 'none'
			child.grow_tree()
			
		elif self.state == 'human':
		
			self.get_valid_moves(self.dic_human, self.dic_ai)
			
			for c in self.children:
				c.grow_tree()
				
		elif self.state == 'ai':
		
			self.get_valid_moves(self.dic_ai, self.dic_human)
			#print(self.children)
			for c in self.children:
				c.dic_human, c.dic_ai = grid.finalize_move(c.dic_human, c.dic_ai, self.last_piece, c.last_piece)
				
			best = best_moves(self.children)
			#print(best)
			for b in best:
				
				c = self.children[b]
				
				if self.level < difficulty:
				
					c.grow_tree()
					#print('next_level')
				
				else:
				
					possible_moves.append(c)
					#print('added!', len(possible_moves))
				
			
			
			
			
	### returns all valid moves as nodes		
	def get_valid_moves(self, dic, dic_opp):
		
		for piece in dic:  # go thru dictionary, piece by piece
		
			loc = dic[piece] # get the location of each piece(list)
		
			if loc != 'dead': # if piece isn't dead...
				
				if piece[1] == 'K': # if piece is a knight
				
					for km in KNIGHT_MOVES:
					
						can_move = True
					
						new_row = loc[0] + km[0]
						new_col = loc[1] + km[1] 
							
						#print(piece, new_row, new_col, loc[0], loc[1])
							
						if 0 <= new_col < grid.GRID_WIDTH and 0 <= new_row < grid.GRID_HEIGHT: # if move is on board
						
							# if move is not overlapping another piece
							for j in dic:
								if dic[j] == [new_row, new_col]:
									can_move = False
								
							if can_move:								
								
								child = self.add_child()
								child.dic_human = dict(self.dic_human)
								child.dic_ai = dict(self.dic_ai)
								child.last_piece = piece
								child.new_row = new_row
								child.new_col = new_col
								
								if self.state == 'human':
									child.dic_human[piece] = [new_row, new_col]
									child.state = 'ai'

								elif self.state == 'ai':
									child.dic_ai[piece] = [new_row, new_col]
									child.state = 'human'
			
				elif piece[1] == 'P':
					
					can_move = True
					
					if piece[0] == 'W':
						forward = -1
					elif piece[0] == 'B':
						forward = 1
									
					new_row = loc[0] + forward
					new_col = loc[1]
					
					if 0 <= new_col < grid.GRID_WIDTH and 0 <= new_row < grid.GRID_HEIGHT: # if move is on board
						
							# if move is not overlapping another piece
							for j in dic:
								if dic[j] == [new_row, new_col]:
									can_move = False
								
							if can_move:								
								
								child = self.add_child()
								child.dic_human = dict(self.dic_human)
								child.dic_ai = dict(self.dic_ai)
								child.last_piece = piece
								child.new_row = new_row
								child.new_col = new_col
								
								if self.state == 'human':
									child.dic_human[piece] = [new_row, new_col]
									child.state = 'ai'

								elif self.state == 'ai':
									child.dic_ai[piece] = [new_row, new_col]
									child.state = 'human'				
									
### gives a board it's score ###	
def analyze_board(dic):
		total = 0
		
		for i in dic:
		
			if dic[i] != 'dead':
			
				if i[1] == 'P':
					total += 1
					
				elif i[1] == 'K':
					total += 2
		
		return total

### checks a list of nodes for highest/lowest score ###		
def best_moves(node_list):

		hi_score = -999
		low_score = 999
		
		hi_list = []
		low_list = []
		
		for e in node_list: # loop through all nodes

			cur_score = (analyze_board(e.dic_ai) - analyze_board(e.dic_human)) # ai score - human score
			
			if cur_score > hi_score: # if hiscore beats previous, add it
			
				hi_score = cur_score
			
			#if cur_score < low_score: # if lowscore beats previous, add it
				
				#low_score = cur_score
			
		e = 0 # reset e
		
		for e in range(len(node_list)): # loop thru list again, this time adding best and worst
		
			cur_score = (analyze_board(node_list[e].dic_ai) - analyze_board(node_list[e].dic_human)) # ai score - human score
			
			if cur_score == hi_score: # if cur score equals high score, add it!
			
				hi_list.append(e)
			
			#if cur_score == low_score: # if cur score equals low score, add it!
			
				#low_list.append(e)
				
		return hi_list
									


def get_move(dic_human):
	
	global possible_moves

	top = node()
	top.state = 'original'
	top.dic_ai = dic_ai
	top.dic_human = dic_human

	top.grow_tree()
	#print(possible_moves)
	best = best_moves(possible_moves)

	num = random.randint(0, len(best) - 1)
	
	choose = best[num]
	
	chosen_node = possible_moves[choose].get_ancestor(3)
	
	dic_ai[chosen_node.last_piece] = [chosen_node.new_row, chosen_node.new_col]
	
	#print(dic_ai[chosen_node.last_piece])
	
	board.board = grid.recreate_grid(chosen_node.dic_ai)
	
	possible_moves = []
	
	return dic_ai, chosen_node.last_piece

"""for e in possible_moves:
	print(e.last_piece, e.level)
	print(e.parent.dic_human)
	print(e.parent.dic_ai)
	print(e.dic_human)
	print(e.dic_ai)
	for u in grid.recreate_grid(e.dic_human):
		print(u)
	for u in grid.recreate_grid(e.dic_ai):
		print(u)
	input('...')"""
