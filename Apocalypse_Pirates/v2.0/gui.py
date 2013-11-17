#Comments

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import functools
#import grid
#import ai

big_font = ('Trebuchet MS', 16)
little_font = ('Trebuchet MS', 10)

class ApocalypseGUI:
	def __init__(self):
		#ai.board = grid.Grid()
		#human.board = grid.Grid()
		self.root = Tk()
		self.titlescreen()
		self.root.mainloop()
		
	def titlescreen(self):
		self.title_frame = Frame(self.root)
		self.title_frame.place(x = 0, y = 0, width = 200, height = 200)
		self.button = ttk.Button(self.title_frame, text = "Continue", command = self.titlescreenclicked)
		self.button.place(x= 0, y = 0)
		print("Button Place ")
	
	def titlescreenclicked(self):
		self.button.destroy()
		self.title_frame.destroy()
		grid = []
		
		self.main_frame = Frame(self.root)
		self.main_frame.place(x = 0, y = 0, width = 640, height = 640)
		
		for i in range(5):
			row = []
			for j in range(5):
				button = ttk.Button(self.main_frame, text = str(i)+ ", " + str(j) , command = functools.partial(self.grid_button_clicked, i, j) )
				button.place(x = i * 48, y = j * 48, height = 48, width = 48)
				row.append(button)
			grid.append(row)
		return grid
		
	def grid_button_clicked(self, x, y):
		pass
	


				
		
