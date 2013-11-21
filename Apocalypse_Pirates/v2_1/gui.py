
from tkinter import *
from tkinter import ttk
import functools
import grid
import ai



big_font = ('Trebuchet MS', 16)
little_font = ('Trebuchet MS', 10)

###### APOCALYPSE GUI ######
class ApocalypseGUI:
	
	### Initialization ###
	def __init__(self, w, h):
		
		self.BASIC_UNIT = 64
		self.CON_LINES = 12
		self.CON_SIZE = self.BASIC_UNIT* 5		
		
		
		# The board for the human
		self.human_board = grid.Grid()
		ai.board = grid.Grid()
		
		# Human pieces and it's co-ordinates
		self.dic_ai = { 'BP1':[1,0],'BP2':[0,1], 'BP3':[0,2], 'BP4':[0,3], 'BP5':[1,4], 'BK1':[0,0], 'BK2':[0,4] }
		self.dic_human = { 'WP1':[3,0],'WP2':[4,1], 'WP3':[4,2], 'WP4':[4,3], 'WP5':[3,4], 'WK1':[4,0], 'WK2':[4,4] }
		
		ai.board.setup_board(self.dic_ai)
		self.human_board.setup_board(self.dic_human)
		
		ai.dic_human = self.dic_human
		ai.dic_ai = dict(self.dic_ai)
		
		
		self.cur_piece = ''
		self.last_x = 0
		self.last_y = 0
		
		# Create the main window
		self.root = Tk()
		
		# Make the screen size stay the same
		self.root.minsize(w,h)
		self.root.maxsize(w,h)
		
		# Save width and height
		self.w = w
		self.h = h
		
		# Load sprites
		self.load_resources()
		
		# Make the titlescreen
		self.setup_titlescreen()
		
		# Tkinter loop
		self.root.mainloop()
		
		
	def load_resources(self):
		
		self.title_bac = (PhotoImage(file = 'images/TitleScreen0.gif'))
		self.main_bac = (PhotoImage(file = 'images/GameScreen.gif'))
		
		# These lists will hold the images
		self.spr_board = []
		self.spr_pieces = []

		
		# Empty pieces
		self.spr_board.append((PhotoImage(file = 'images/LightBlock.gif')))
		self.spr_board.append((PhotoImage(file = 'images/DarkBlock.gif')))
		
		# Load the pieces 
		self.spr_pieces.append((PhotoImage(file = 'images/BPawn_Lblock.gif')))
		self.spr_pieces.append((PhotoImage(file = 'images/BPawn_Dblock.gif')))
		self.spr_pieces.append((PhotoImage(file = 'images/BKnight_Lblock.gif')))
		self.spr_pieces.append((PhotoImage(file = 'images/BKnight_Dblock.gif')))
		self.spr_pieces.append((PhotoImage(file = 'images/WPawn_Lblock.gif')))
		self.spr_pieces.append((PhotoImage(file = 'images/WPawn_Dblock.gif')))
		self.spr_pieces.append((PhotoImage(file = 'images/WKnight_Lblock.gif')))
		self.spr_pieces.append((PhotoImage(file = 'images/WKnight_Dblock.gif')))
		
		
		
	### updates the grid ###
	def update_grid(self):
		
		# loop through the grid
		for i in range(len(self.grid)):
			
			for j in range(len(self.grid[i])):
				
				block_color = 1
				# If co-ordinates are even, load the light coloured blocks, else the dark coloured blocks
				if (i%2)==(j%2):
					block_color = 0
				#save the current piece (for convenience)
				if self.human_board.board[i][j] != grid.b:
					piece = self.human_board.board[i][j]
				elif ai.board.board[i][j] != grid.b:
					piece = ai.board.board[i][j]
				else:
					piece = grid.b
				
				#Checks for black pawns for rows less than 2 
				if piece != grid.b:
					if piece[0] == 'W':
						col = 4
					else:
						col = 0
						
					if piece[1] == 'K':
						type = 2
					else:
						type = 0
						
					
					button = self.grid[i][j]
					button['image'] = self.spr_pieces[col + type + block_color]
				#Checks for black knights for rows less than 2	

				else:

						button = self.grid[i][j]
						button['image'] = self.spr_board[block_color]

					
		#self.root.after(100, self.update_grid)
		
	def setup_titlescreen(self):
	
			
		self.main_frame = ttk.Frame(self.root)
		self.main_frame.place(x = 0, y = 0, width = self.w, height = self.h)
		
		# add background picture
		self.bac_canvas = Canvas(self.main_frame)
		self.bac_canvas.place(x = 0, y = 0, width = self.w, height = self.h)
		self.bac_canvas.create_image(0, 0, image = self.title_bac, anchor = NW, tag = 'bac')
		self.bac_canvas.bind('<1>', self.titlescreen_clicked)
		print('hi')
		
	
	### Takes you from the main menu to the actual game ###
	def titlescreen_clicked(self, *args):
	
		self.bac_canvas.unbind('<1>')
		self.bac_canvas.create_image(0, 0, image = self.main_bac, anchor = NW, tag = 'bac')
		
		#Empty grid for buttons 
		self.grid = []
		
		## Sets up the game board ##
		
		#Container for the board 
		self.board_frame = ttk.Frame(self.root)
		self.board_frame.place(x = self.w/2 - 6*self.BASIC_UNIT, y = self.h/2 - 2*self.BASIC_UNIT, width = 5*self.BASIC_UNIT, height = 5*self.BASIC_UNIT)
		
		#Places buttons onto the empty grid
		for i in range(5):
			row = []
			for j in range(5):
				button = ttk.Button(self.board_frame, text = str(i)+ ", " + str(j) , command = functools.partial(self.grid_button_clicked, i, j) )
				button.place(y = i * self.BASIC_UNIT, x = j * self.BASIC_UNIT, height = self.BASIC_UNIT, width = self.BASIC_UNIT)
				row.append(button)
			self.grid.append(row)
		
		self.update_grid()
		
		## Sets up the console ##
		
		self.console_text = ['' for i in range(self.CON_LINES)]
		self.console_lines = []
		self.console_icons = []

		#Create canvas for the console
		self.console_canvas = Canvas(self.root, bg = 'white')
		self.console_canvas.place(x = self.w/2 + self.BASIC_UNIT, y = self.h/2 - self.BASIC_UNIT*2, width = self.BASIC_UNIT*6, height = self.CON_SIZE)
		
		#Putting the text lines onto the consoles
		for i in range(self.CON_LINES):
			self.console_lines.append(self.console_canvas.create_text(4, i*(self.CON_SIZE/self.CON_LINES) + 4, anchor = NW))
			self.console_canvas.itemconfig(self.console_lines[i], text = self.console_text[i])
			
		#Input text 
		self.entry_var = StringVar()
		self.console_entry = ttk.Entry(self.root, textvariable = self.entry_var)
		self.console_entry.place(x = self.w/2 + self.BASIC_UNIT, y = self.h/2 - self.BASIC_UNIT*2 + self.CON_SIZE + 16, width = self.BASIC_UNIT*4, height = 24)

		
		#Allows you the update the console text 
		self.entry_button = ttk.Button(text = 'Send', command = self.send_button_clicked)
		self.entry_button.place(x = self.w/2 + self.BASIC_UNIT*5.5, y = self.h/2 - self.BASIC_UNIT*2 + self.CON_SIZE + 16, width = self.BASIC_UNIT, height = 24)
		self.root.bind('<Return>', self.send_button_clicked)
		
		# Command for updating text on console
	def send_button_clicked(self,*args):
		self.output_text(self.entry_var.get())
		
		
		#Updates piece when clicked on
	def grid_button_clicked(self, x, y):
		if self.cur_piece == '':
			for e in self.dic_human:
				if self.human_board.board[x][y] == e:
					self.cur_piece = self.human_board.board[x][y]
					self.last_x = x
					self.last_y = y
		elif self.cur_piece == self.human_board.board[x][y]:
			self.cur_piece = ''
		else:
			if self.human_board.validate_location(self.last_x, self.last_y, x, y, self.cur_piece, self.dic_human):
				self.dic_human = self.human_board.move_piece(x,y,self.cur_piece, self.dic_human)
				dic_ai, piece_ai = ai.get_move()
				self.human_board.board, ai.board.board, self.dic_human, ai.dic_ai = grid.finalize_move(self.human_board.board, ai.board.board, self.cur_piece, piece_ai, self.dic_human, dic_ai)
				self.cur_piece = ''		
		self.update_grid()
		print(self.cur_piece)
			
	def output_text(self,string):
		empty = 0
		# check if any line is empty, if so then use it
		for i in range(self.CON_LINES):
			if self.console_text[i] == '':
				self.console_text[i] = string
				self.console_canvas.itemconfig(self.console_lines[i], text = self.console_text[i])
				empty = 1
				break
                        
		# if all lines are full, then move all lines up one and insert new line in bottom
		if empty == 0:
			for i in range(self.CON_LINES-1):
				self.console_text[i] = self.console_text[i+1]
				self.console_canvas.itemconfig(self.console_lines[i], text = self.console_text[i])
                        
			self.console_text[i+1]= string
			self.console_canvas.itemconfig(self.console_lines[i+1], text = self.console_text[i+1])

	
				
		
