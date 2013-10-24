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
# check the location picked by ai or human is a hit or a miss and print 
#a grid with an 'X' for a hit and an 'o' for a miss	
def drop_bomb(grid_defend,grid_attack,col_bomb,row_bomb):
	#if the location picked to bomb equal any of the VESSEL_SIZE its is a hit
	if grid_attack[col_bomb][row_bomb] ==	VESSEL_SIZE[index]
			grid_attack[col_bomb][row_bomb] = HIT
			grid_defend[col_bomb][row_bomb] = HIT
			print('HIT')
	#the location is empty 	
	else:
			grid_attack[col_bomb][row_bomb] = MISS
			grid_defend[col_bomb][row_bomb] = MISS 
			print('MISS')
	print(grid_defend)
	print(grid_attack)
	

#check to see if there is any ship left on the grid, if no ship left return True as sunk else return false						
def all_ships_sunk(grid_defend):
	# TEMP VARIABLES
	check_column = 0
	check_row =0
	Sunk= False
	if direction == 'h'
            for check_column in range(col,col+VESSEL_SIZE[index]):
                if grid[check_column][check_row] != 5 or 4 or 3 or 2 :
                    return True
					
	elif direction == 'v':
            for check_y in range(row,row+GRID_HEIGHT):
                if grid[check_column][check_row] != 5 or 4 or 3 or 2:
                    return True:
	
	else:
		sunk=False
	
	return sunk

