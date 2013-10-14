from tkinter import *
from tkinter import ttk
import GameLib

def load_image(image):
	return (PhotoImage(file = image))

class window:
	def __init__(self, image, w, h):
		self.name = Tk()
		self.name.minsize(w,h)
		self.name.maxsize(w,h)
		
		if image != 0:
			self.img = PhotoImage(file = image)
			self.bac = ttk.Label(self.name, image = self.img).place(x = 0, y = 0, width = w, height = h)
		
	def _loop(self):
		self.name.mainloop()
		
class widget:
	def __init__(self, parent, x, y, w, h):
		self.parent = parent
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.name = ''
		

class Entry(widget):
	def init(self, text):
		self.txt_var = StringVar()
		self.txt_var.set(text)
		self.name = ttk.Entry(self.parent, textvariable = self.txt_var)
		self.name.place(x = self.x, y = self.y, width = self.w, height = self.h)
		
class Button(widget):
	def init(self, text, _command):
		self.text = text
		self.name = ttk.Button(self.parent, text = self.text, command = _command)
		self.name.place(x = self.x, y = self.y, width = self.w, height = self.h)

class Label(widget):
	def init(self, text):
		self.txt_var = StringVar()
		self.txt_var.set(text)
		self.name = ttk.Label(self.parent, textvariable = self.txt_var, background = 'white')
		self.name.place(x = self.x, y = self.y, width = self.w, height = self.h)

		
class LabelImg(widget):
	def init(self, image):
		self.img = image
		self.name = ttk.Label(self.parent, image = self.img)
		self.name.place(x = self.x, y = self.y, width = self.w, height = self.h)

class MyCanvas(widget):
	def init(self, bac_col):
		self.name = Canvas(self.parent, width = self.w, height = self.h, bg = bac_col)
		self.name.place(x = self.x, y = self.y)
		self.name['borderwidth'] = 2
		self.name['relief'] = 'ridge'
		
	def add_pic(self, image, x, y, mytag):
		return self.name.create_image(x, y, image = image, anchor = NW, tag = mytag)
		
class Frame(widget):
	def init(self):
		self.name = ttk.Frame(self.parent)
		self.name.place(x = self.x, y = self.y, width = self.w, height = self.h)
		self.name['borderwidth'] = 2
		self.name['relief'] = 'ridge'
		