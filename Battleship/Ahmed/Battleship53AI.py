#********************************************
# By Ahmed Elbannan
# September 22nd 2013
# Battleship CPSC231 (Limited Edition! ;] )
#********************************************

import random

# CONSTANTS
GRID_HEIGHT = 10;
GRID_WIDTH = 10;
VESSEL_NAME = ['Aircraft Carrier', 'Battleship', 'Submarine', 'Destroyer', 'Patrol Boat'];
VESSEL_SIZE = [5, 4, 3, 2, 2];
NAME = '';

# global variables
direction = 'horizontal';
x = ord('A');
y = 0;

w = '~'
grid = 		[
			[w,w,w,w,w,w,w,w,w,w],
			[w,w,w,w,w,w,w,w,w,w],
			[w,w,w,w,w,w,w,w,w,w],
			[w,w,w,w,w,w,w,w,w,w],
			[w,w,w,w,w,w,w,w,w,w],
			[w,w,w,w,w,w,w,w,w,w],
			[w,w,w,w,w,w,w,w,w,w],
			[w,w,w,w,w,w,w,w,w,w],
			[w,w,w,w,w,w,w,w,w,w],
			[w,w,w,w,w,w,w,w,w,w],
			[w,w,w,w,w,w,w,w,w,w]];
			
# print out the grid			
def print_grid():
	print('__________________________');
	print('|  | A B C D E F G H I J |');
	print('--------------------------');
	row = 0;
	column = 0;
	for row in range(GRID_HEIGHT):
		if row  == 9:
			print( '|' + str(row + 1) + '| ', end = '');
		else:
			print( '|0' + str(row + 1) + '| ', end = '');			
		for column in range(0, GRID_WIDTH):
			print(grid[column][row] + ' ', end = '');
		print('|');
	print();
			
# Title Screen! Now a function!
def print_titlescreen():
	global NAME;
	print();
	print('________________________________________');
	print('|*********WELCOME TO BATTLESHIP!*******|');
	print('|**************************************|');
	print('|**************************************|');
	print('|*********A game like no other!********|');
	print('|**************************************|');
	print('|**************************************|');
	print('|**************************************|');
	print();
	print();
# end

# let's the ai choose where to place vessel
def get_location(index):
	global x; # this function can edit x
	global y; # this function can edit y
	global direction; # this function can edit direction
	x = random.randint(0,9)
	y = random.randint(0,9)
	direction = random.randint(0,1)
	if direction == 0:
		direction = 'h'
	else:
		direction = 'v'
# end

# put vessel on board
def place_vessel(index):
	global x;
	global y;
	if direction == 'h': 
			for x in range(x, x + VESSEL_SIZE[index]):
				grid[x][y] = str(VESSEL_SIZE[index]);
	elif direction == 'v':
			for y in range(y, y + VESSEL_SIZE[index]):
				grid[x][y] = str(VESSEL_SIZE[index]);

# put vessel on board
def has_overlap(index):
	
	check_x = x;
	check_y = y;
	no_overlap = 'true';
	
	if direction == 'h': 
			for check_x in range(check_x, check_x + VESSEL_SIZE[index]):
				if grid[check_x][check_y] !='~':
						no_overlap = 'false';
						break;
					
	elif direction == 'v':
			for check_y in range(check_y, check_y + VESSEL_SIZE[index]):
				if grid[check_x][check_y] !='~':
						no_overlap = 'false';
						break;
						
	return no_overlap;

# checks if the location is valid
def validate_location(index):
	global x; # this function can edit x
	global y; # this function can edit y
	# check if string is a single letter or smaller than a three digit number, if not, asks for input again, then checks
	# checks if location is on the board and if the ship will fit, if not asks for input again and checks again
	if (direction == 'h') and (-1 < x < (GRID_WIDTH - VESSEL_SIZE[index])) and (-1 < y < GRID_HEIGHT):
		if has_overlap(index) == 'true':
			place_vessel(index);
		else:
			get_location(index);
			validate_location(index);
	elif direction == 'v' and (-1 < y < (GRID_HEIGHT - VESSEL_SIZE[index])) and (-1 < x < GRID_WIDTH):  
		if has_overlap(index) == 'true':
			place_vessel(index);
		else:
			get_location(index);
			validate_location(index);
	else:
		get_location(index);
		validate_location(index);
	
	
# doesn't quit unless q is entered	
def enter_choice():
	choice = '';
	while not choice == 'q':
		choice = input('Enter choice: ');
		
# now put it all together!
def main():
        
        # prints VESSEL_NAME[index], location, and orientation of a vessel
	print_titlescreen();
	print_grid();
        # Ask user to place aircraft carrier
	i = 0;
	for i in range(5):
		get_location(i);
		validate_location(i);
		print_grid();
	
	enter_choice();
	return;
# end

main(); 
