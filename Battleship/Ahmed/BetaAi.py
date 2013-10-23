
import grid
import random

attack_grid = [ [grid.B for i in range(grid.GRID_WIDTH)] for j in range(grid.GRID_HEIGHT)]
defend_grid = [ [grid.B for i in range(grid.GRID_WIDTH)] for j in range(grid.GRID_HEIGHT)]

def get_location(index):

	global defend_grid
	
	dir = random.randint(0,1)
	# if horizontal
	if dir == 0:
		# place on a valid spot (taking ship size into account)
		dir = 'h'
		col = random.randint(0,grid.GRID_WIDTH - 1 - grid.VESSEL_SIZE[index])
		row = random.randint(0,grid.GRID_HEIGHT - 1)
		
	else:
	
		dir = 'v'
		col = random.randint(0,grid.GRID_WIDTH - 1)
		row = random.randint(0,grid.GRID_HEIGHT - 1 - grid.VESSEL_SIZE[index])
	
	if grid.has_overlap(defend_grid, index, row, col, dir):
		get_location(index)
	else:
		defend_grid = grid.add_vessel(defend_grid, index, row, col, dir)
	

       
def find_ships():
	
	found_ships = []
	
	for i in range(GRID_HEIGHT):
		
		for j in range(GRID_WIDTH):
			
			if attack_grid[i][j] == 'X':
				found_ships.append([j,i])
				
	if len(found_ships) > 0			
		analyse_grid(found_ships)
	else:
		row, col = random_move()
		
	
def random_move():
	
	col = random.randint(0,grid.GRID_WIDTH - 1)
	row = random.randint(0,grid.GRID_HEIGHT - 1)
	
	while attack_grid[row][col] != '~':
		
		col = random.randint(0,grid.GRID_WIDTH - 1)
		row = random.randint(0,grid.GRID_HEIGHT - 1)
		
	return row, col
	
def analyse_grid(found_ships):
	pass;
				
