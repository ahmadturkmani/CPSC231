#Comments

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import functools
import grid
#import ai

big_font = ('Trebuchet MS', 16)
little_font = ('Trebuchet MS', 10)

###### APOCALYPSE GUI ######
class ApocalypseGUI:
	
	### initialization ###
	def __init__(self, w, h):
		
		self.CON_LINES = 8
		# the board for the human
		self.human_board = grid.Grid()
		
		test_dic = { 'BP1':[3,0],'BP2':[4,1], 'BP3':[4,2], 'BP4':[4,3], 'BP5':[3,4], 'BK1':[4,0], 'BK2':[4,4] }
		self.human_board.setup_board(test_dic)
		
		# create the main window
		self.root = Tk()
		
		# make the screen size stay the same
		self.root.minsize(w,h)
		self.root.maxsize(w,h)
		
		# save width and height
		self.w = w
		self.h = h
		
		# load sprites
		self.load_resources()
		
		# make the titlescreen
		self.setup_titlescreen()
		
		# tkinter loop
		self.root.mainloop()
		
		
	def load_resources(self):
		
		self.bac = (PhotoImage(file = 'images/TitleScreen.gif'))
		
		# these lists will hold the images
		self.spr_board = []
		self.spr_pieces = []

		
		# empty pieces
		self.spr_board.append((PhotoImage(file = 'images/LightBlock.gif')))
		self.spr_board.append((PhotoImage(file = 'images/DarkBlock.gif')))
		
		# Load the pieces 
		self.spr_pieces.append((PhotoImage(file = 'images/BPawn_Lblock.gif')))
		self.spr_pieces.append((PhotoImage(file = 'images/BPawn_Dblock.gif')))
		self.spr_pieces.append((PhotoImage(file = 'images/BKnight_Lblock.gif')))
		self.spr_pieces.append((PhotoImage(file = 'images/BKnight_Dblock.gif')))
		
		
		
	### updates the grid ###
	def update_grid(self):
		
		# loop through the grid
		for i in range(len(self.grid)):
			
			for j in range(len(self.grid[i])):
				
				block_color = 1
				
				if (i%2)==(j%2):
					block_color = 0
				
				piece = self.human_board.board[i][j]
				
					 
				if piece[:2] == "BP":
					
					button = self.grid[i][j]
					button['image'] = self.spr_pieces[block_color]
					
				elif piece[:2] == 'BK':
					
					button = self.grid[i][j]
					button['image'] = self.spr_pieces[2 + block_color]

				else:

						button = self.grid[i][j]
						button['image'] = self.spr_board[block_color]

					
		#self.root.after(100, self.update_grid)
		
	def setup_titlescreen(self):
	
			
		self.main_frame = ttk.Frame(self.root)
		self.main_frame.place(x = 0, y = 0, width = self.w, height = self.h)
		
		self.bac_canvas = Canvas(self.main_frame)
		self.bac_canvas.place(x = 0, y = 0, width = self.w, height = self.h)	
		
		self.button = ttk.Button(self.main_frame, text = "Continue", command = self.titlescreen_clicked)
		self.button.place(x= self.w/2 - 32, y = self.h - 48, width = 64, height = 32)
		
	
	### sets up main game area ###
	def titlescreen_clicked(self):
	
		self.button.destroy()
		
		self.grid = []
		
		## sets up the game board ##
		
		self.board_frame = ttk.Frame(self.root)
		self.board_frame.place(x = self.w/2 - 6*64, y = self.h/2 - 5*64, width = 5*64, height = 5*64)
		
		for i in range(5):
			row = []
			for j in range(5):
				button = ttk.Button(self.board_frame, text = str(i)+ ", " + str(j) , command = functools.partial(self.grid_button_clicked, i, j) )
				button.place(y = i * 64, x = j * 64, height = 64, width = 64)
				row.append(button)
			self.grid.append(row)
		
		self.update_grid()
		
		## sets up the console ##
		
		self.console_text = [StringVar() for i in range(self.CON_LINES)]
		

		
	def grid_button_clicked(self, x, y):
		pass
	


				
		