
# import tkinter (python graphics library)
from tkinter import * # import all 
from tkinter import ttk # import the new ttk style
import GameLib # game logic

# load an image, and return it (can only load .gif)
def load_image(image):
	return (PhotoImage(file = image))

# this is the main window
class window:

	# creates the main window upon initialization, and sets a background image (if applicable)
	def __init__(self, image, w, h):
	
		# create a window
		self.name = Tk()
		
		# set the minsize/maxsize to w,h so the game is played exactly as intended
		self.name.minsize(w,h)
		self.name.maxsize(w,h)
		
		# if there is an image to be loaded, load it and place it as the background
		if image != 0:
			self.img = PhotoImage(file = image)
			self.bac = ttk.Label(self.name, image = self.img).place(x = 0, y = 0, width = w, height = h)
		
		# start the game loop
	def _loop(self):
		self.name.mainloop()
		
# this is the parent of all widgets. It has all the basic variables. this class will never be called		
class widget:
	def __init__(self, parent, x, y, w, h):
		self.parent = parent
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.name = ''
		
# an entry box for text
class Entry(widget):
	
	def init(self, text):
		
		# set txt_var to a string var, meaning tkinter will take care of it for us. we can use it to get the entry contents
		self.txt_var = StringVar()
		# since we can't set stringvars directly, we must use set() and get()
		self.txt_var.set(text)
		
		# create an entry, assign txt_var to it, and place it
		self.name = ttk.Entry(self.parent, textvariable = self.txt_var)
		self.name.place(x = self.x, y = self.y, width = self.w, height = self.h)

# A clickable button		
class Button(widget):

	# _command is the function to execute when pressed
	def init(self, text, _command):
	
		self.text = text
		self.name = ttk.Button(self.parent, text = self.text, command = _command)
		self.name.place(x = self.x, y = self.y, width = self.w, height = self.h)

# A label
class Label(widget):
	def init(self, text):
		self.txt_var = StringVar()
		self.txt_var.set(text)
		self.name = ttk.Label(self.parent, textvariable = self.txt_var, background = 'white')
		self.name.place(x = self.x, y = self.y, width = self.w, height = self.h)

# labels with images		
class LabelImg(widget):

	# image must be of the PhotoImage class (use load_image)
	def init(self, image):
	
		self.img = image
		self.name = ttk.Label(self.parent, image = self.img)
		self.name.place(x = self.x, y = self.y, width = self.w, height = self.h)

# a canvas. Can be used to draw anything
class MyCanvas(widget):

	# bac_col is the background color
	def init(self, bac_col):

		self.name = Canvas(self.parent, width = self.w, height = self.h, bg = bac_col)
		self.name.place(x = self.x, y = self.y)
		
	# Add an image to the canvas. mytag is the name we will use to refer to it
	def add_pic(self, image, x, y, mytag):
		self.name.create_image(x, y, image = image, anchor = NW, tag = mytag)

# A frame. Used to hold other widgets		
class Frame(widget):

	def init(self):
	
		self.name = ttk.Frame(self.parent)
		self.name.place(x = self.x, y = self.y, width = self.w, height = self.h)
		# make a ridge border of width 2
		self.name['borderwidth'] = 2
		self.name['relief'] = 'ridge'
		