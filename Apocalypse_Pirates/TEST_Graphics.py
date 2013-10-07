from tkinter import *
from tkinter import ttk


class window:
	def __init__(self):
		self.root = Tk()
		self.name = ttk.Frame(self.root).grid(column = 0, row = 0, sticky = (N,E,W,S))
		
	def _loop(self):
		self.root.mainloop()
		
class widget:
	def __init__(self, parent, column, row):
		self.parent = parent
		self._column = column
		self._row = row
		self.name = ''
		

class Entry(widget):
	def init(self, width, text):
		self.txt_var = StringVar()
		self.txt_var.set(text)
		self._width = width
		self.name = ttk.Entry(self.parent, width = self._width, textvariable = self.txt_var).grid(column = self._column, row = self._row)
		
class Button(widget):
	def init(self, image, text):
		self.text = text
		
		self.image = image
		self.name = ttk.Button(self.parent, text = self.text, image = self.image).grid(column = self._column, row = self._row)

