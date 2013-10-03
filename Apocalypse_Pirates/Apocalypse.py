############################################################################
# By:     Ahmed Elbannan, Hilmi Abou-Saleh, Ahmad Turkmani Namhyuk Woo     #
# Date:   September 25th 2013                                              #
# Name:   Apocalypse Tutorial II Collector's Edition                       #
############################################################################

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
	return;
"""
I want to add  a function which asks the user for the input of the Pawn, and then
calls the Pawn for input_piece. It can be commented-out, but for future-proof. 
I'll add it tomorrow. I finally understand how the third exercise works so I'm set. :)
Why?
"""
# Gets input for a piece and sets it's location to global x/y
def input_piece(name, color):
	# Let's us edit global x/y
	global x;
	global y;
	# Ask the user where he wants to place his piece;
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
	return;
	
# Functions chill here 	
def main():
	print_titlescreen();
	input_piece('Pawn', 'white');
	calc_position('Pawn', 'black', 0, 1);
	calc_position('Knight', 'black', 1, 1);	
	return;

main();

