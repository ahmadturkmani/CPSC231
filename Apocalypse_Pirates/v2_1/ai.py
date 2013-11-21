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
			child.grow_tree()
			
		elif self.state == 'human':
		
			self.get_valid_moves(self.dic_human, self.dic_ai)
			

			best, worst = best_moves(self.children)
			
			for w in worst:
				
				if self.level < difficulty:
				
					self.children[w].grow_tree()
				
				else:
				
					possible_moves.append(self.children[w])
			
		elif self.state == 'ai':
		
			self.get_valid_moves(self.dic_ai, self.dic_human)
			
			
			for c in self.children:
				
				if self.level < difficulty:
				
					c.grow_tree()
				
				else:
				
					possible_moves.append(c)
			
				
			
			
			
			
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
								
								
								if self.state == 'human':
									child.dic_human[piece] = [new_row, new_col]
									child.state = 'ai'
								else:
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
			
			if cur_score < low_score: # if lowscore beats previous, add it
				
				low_score = cur_score
			
		e = 0 # reset e
		
		for e in range(len(node_list)): # loop thru list again, this time adding best and worst
		
			cur_score = (analyze_board(node_list[e].dic_ai) - analyze_board(node_list[e].dic_human)) # ai score - human score
			
			if cur_score == hi_score: # if cur score equals high score, add it!
			
				hi_list.append(e)
			
			if cur_score == low_score: # if cur score equals low score, add it!
			
				low_list.append(e)
				
		return hi_list, low_list
									

				
top = node()
top.state = 'original'
top.dic_ai = { 'BP1':[1,0],'BP2':[0,1], 'BP3':[0,2], 'BP4':[0,3], 'BP5':[1,4], 'BK1':[0,0], 'BK2':[0,4] }
top.dic_human = { 'WP1':[3,0],'WP2':[4,1], 'WP3':[4,2], 'WP4':[4,3], 'WP5':[3,4], 'WK1':[4,0], 'WK2':[4,4] }
top.grow_tree()

for e in possible_moves:
	print(e.last_piece, e.level)
	print(e.parent.dic_human)
	print(e.parent.dic_ai)
	print(e.dic_human)
	print(e.dic_ai)
	for u in grid.recreate_grid(e.dic_human):
		print(u)
	for u in grid.recreate_grid(e.dic_ai):
		print(u)
	input('...')
