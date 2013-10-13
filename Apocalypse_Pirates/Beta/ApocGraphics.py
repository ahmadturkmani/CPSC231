###########################################################################################
# By:     Ahmed Elbannan, Hilmi Abou-Saleh, Ahmad Turkmani, Namhyuk Woo, Nasir Osman      #
# Date:   September 25th 2013                                                             #
# Name:   Apocalypse Tutorial II Collector's Edition                                      #
###########################################################################################

import TKLib

WIDTH = 960
HEIGHT = 720

x = ord('A');
y = 0;

# Draws the title screen!!!!!!!!!!!!!!!!!!!!!!!
def print_titlescreen():
	print('###################################################');
	print('#    #   ###  #=# #==   #   #   \ / ###  === #==  #');
	print('#   #=#  #==# # # #    #=#  #    #  #==# \=  #=   #');
	print('#  #   # #    #=# #== #   # #==  #  #    ==/ #==  #');
	print('###################################################');
	print("~~~~~~~~~~TUTORIAL II COLLECTOR'S EDITION~~~~~~~~~~");
	print('\\\\\\\\\\###############################//////////');
	print();
	print('~~~~~~~~\Created by the Apocalyptic Pirates/~~~~~~~');
	print('~~~~~~~~~\________copyright 2013(c)_______/~~~~~~~~');
	print();
	return;

# Gets input for a piece and sets it's location to global x/y
def input_piece(name, color):
	# Let's us edit global x/y
	global x;
	global y;
	# Ask the user where he wants to place his piece
	print('Where would you like to place your ' + color + ' ' + name + '?');
	x = (ord(input('Row (a-e)    : ')) - ord('a'));
	y = (int(input('Column (1-5) : ')) - 1);
	print();
	# Print it
	print_piece(name, color);
	return;

# Prints out a piece of chosen color 	
def print_piece(name, color):
	print('A ' + color + ' ' + name + ' is located at (' + (chr(x + ord('a'))) + ',' + str(y + 1) + ').');
	print();
	return;

# Calculate where the other pieces are, one by one
def calc_position(name, color, move_x, move_y):
	# Let's us edit global x/y
	global x;
	global y;
	# Now... CALCULATION TIME! ~(o_o)~
	x = (x + move_x) % 5;
	y = (y + move_y) % 5;
	print_piece(name, color);
	
# Functions chill here 	
def main():
	global root
	root = TKLib.window('spr_back.gif', WIDTH, HEIGHT)
	
	title = TKLib.LabelImg(root.name, 0, 0, 960, 128)
	title.init('spr_title.gif')
	
	canvas = TKLib.MyCanvas(root.name, 336, 264, 288, 192)
	canvas.init('black')
	canvas.add_pic('spr_board.gif', 24, 24)
	
	entry1 = TKLib.Entry(root.name, 800, 512, 96, 32)
	entry1.init(20, 'Enter Location')
	
	button1 = TKLib.Button(root.name, 896, 512, 64, 32)
	button1.init('', 'Button!')
	label1 = TKLib.Label(root.name, 336, 456, 288, 48)
	label1.init('-')
	label2 = TKLib.Label(root.name, 336, 456 + 48, 288, 48)
	label2.init('-')
	label3 = TKLib.Label(root.name, 336, 456 + 92, 288, 48)
	label3.init('-')
	#print_titlescreen();
	#input_piece('Pawn', 'white');
	#calc_position('Pawn', 'black', 0, 1);
	#calc_position('Knight', 'black', 1, 1);
	root._loop()
	return;

main();
