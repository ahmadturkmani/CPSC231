# contains all functions relating to the grid

#CONSTANTS
GRID_HEIGHT = 10;
GRID_WIDTH = 10;
VESSEL_NAME = ['Aircraft Carrier', 'Battleship', 'Submarine', 'Destroyer', 'Patrol Boat'];
VESSEL_SIZE = [5, 4, 3, 2, 2];
NUM_OF_VESSELS = 5
B = '~' # this is water

	
	
def print_grid(grid):
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
# end		

def add_vessel(grid, index, row, col, direction):

	if direction == 'h': 
			for col in range(col, col + VESSEL_SIZE[index]):
				grid[col][row] = str(VESSEL_SIZE[index]);
	elif direction == 'v':
			for row in range(row, row + VESSEL_SIZE[index]):
				grid[col][row] = str(VESSEL_SIZE[index]);
				
	return grid
	
def has_overlap(grid, index, row, col, direction):
	# TEMP VARIABLES
	check_x = col
	check_y = row
	
	if direction == 'h': 
			for check_x in range(check_x, check_x + VESSEL_SIZE[index]):
				if grid[check_x][check_y] !='~':
						return True;
					
	elif direction == 'v':
			for check_y in range(check_y, check_y + VESSEL_SIZE[index]):
				if grid[check_x][check_y] !='~':
						return True;
	
	return False

						
# end
