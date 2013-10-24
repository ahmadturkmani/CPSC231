###############################
# Ahmed Elbannan, Nasir Osman
# Tutorial 2 Group 5
# Battleship
###############################

import grid
import random

grid_attack = [ [grid.B for i in range(grid.GRID_WIDTH)] for j in range(grid.GRID_HEIGHT)]
grid_defend = [ [grid.B for i in range(grid.GRID_WIDTH)] for j in range(grid.GRID_HEIGHT)]

def get_location(index):

	global grid_defend
	
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
	
	if grid.has_overlap(grid_defend, index, row, col, dir):
		get_location(index)
	else:
		grid_defend = grid.add_vessel(grid_defend, index, row, col, dir)
	

       
def get_choice():
	
	found_ships = []
	
	for i in range(grid.GRID_HEIGHT):
		
		for j in range(grid.GRID_WIDTH):
			
			if grid_attack[i][j] == 'X':
				found_ships.append([j,i])
				
	if len(found_ships) > 0 :			
		row, col = analyse_grid(found_ships)
	else:
		row, col = random_move()
	return row, col		
	
def random_move():
	
	col = random.randint(0,grid.GRID_WIDTH - 1)
	row = random.randint(0,grid.GRID_HEIGHT - 1)
	
	while grid_attack[row][col] != '~':
		
		col = random.randint(0,grid.GRID_WIDTH - 1)
		row = random.randint(0,grid.GRID_HEIGHT - 1)
		
	return row, col
	
def analyse_grid(found_ships):
	for i in range(len(found_ships)):
		col = found_ships[i][0]
		row = found_ships[i][1]		
		
		if col > 0:
			if grid_attack[row][col - 1] == grid.B:
				return row, (col - 1)
			elif  row > 0:
				if grid_attack[row - 1][col] == grid.B:
					return (row - 1), (col)
			elif col < 9:
				if grid_attack[row][col + 1] == grid.B:
					return row, (col + 1)
			elif row < 9:
				if grid_attack[row + 1][col] == grid.B:
					return (row + 1), (col)
				
	row, col = random_move()
	return row, col
					
				# gonna use this later
"""nearby_x =[]
                col = found_ships[i][0]
                row = found_ships[i][1]
                
                for j in range(4):
                        
                        if (col - j) > -1:
                                
                                if grid_attack[row][col - j] == grid.HIT:
                                        nearby_x.append([grid.HIT, 'l'
"""
