###############################
# Ahmed Elbannan, Nasir Osman
# Tutorial 2 Group 5
# Battleship
###############################

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
		col = random.randint(0,grid.GRID_WIDTH - 1 - grid.VESSEL_SIZES[index])
		row = random.randint(0,grid.GRID_HEIGHT - 1)
		
	else:
	
		dir = 'v'
		col = random.randint(0,grid.GRID_WIDTH - 1)
		row = random.randint(0,grid.GRID_HEIGHT - 1 - grid.VESSEL_SIZES[index])
	
	if grid.has_overlap(defend_grid, index, row, col, dir):
		get_location(index)
	else:
		defend_grid = grid.add_vessel(defend_grid, index, row, col, dir)
	
###################################################################################








       
def get_choice():
	
	pre_ships = []
	smallest_ship = 20
	found_ships = []
	
	for i in range(grid.GRID_HEIGHT):
		
		for j in range(grid.GRID_WIDTH):
			
			if attack_grid[i][j] == 'X':
				found_ships.append([j,i])
				
	if len(found_ships) > 0 :			
		row, col = analyse_grid(found_ships)
	else:
		row, col = get_probability()
		
	return row, col		
	
def find_ships(pre_ships):
	end_1 = False
	end_2 = False
	
	for i in range(len(pre_ships)):
		if col > 9:
			pass
			
	
def analyse_grid(found_ships):
	
	for i in range(len(found_ships)):
	
		col = found_ships[i][0]
		row = found_ships[i][1]		
		
		if col > 0:
			if attack_grid[row][col - 1] == grid.B:
				if col < 9:
					if attack_grid[row][col + 1] == grid.HIT:
						return row, (col - 1)
				elif col == 9:
					return row, (col - 1)
		if  row > 0:
			if attack_grid[row - 1][col] == grid.B:
				if row < 9:
					if attack_grid[row + 1][col] == grid.HIT:
						return (row - 1), (col)
				elif row == 9:
					return (row - 1), (col)

		if col < 9:
			if attack_grid[row][col + 1] == grid.B:
				if col > 0:
					if attack_grid[row][col - 1] == grid.HIT:
						return row, (col + 1)
				elif col == 0:
					return row, (col + 1)
		if row < 9:
			if attack_grid[row + 1][col] == grid.B:
				if col > 0:
					if attack_grid[row - 1][col] == grid.B:
						return (row + 1), (col)	
				elif col == 0:
					return (row + 1), (col)	
		
	for i in range(len(found_ships)):
		
		col = found_ships[i][0]
		row = found_ships[i][1]	
		
		if col > 0:
			if attack_grid[row][col - 1] == grid.B:
				return row, (col - 1)
		if  row > 0:
			if attack_grid[row - 1][col] == grid.B:
				return (row - 1), (col)
		if col < 9:
			if attack_grid[row][col + 1] == grid.B:
				return row, (col + 1)
		if row < 9:
			if attack_grid[row + 1][col] == grid.B:
				return (row + 1), (col)
				
	row, col = get_probability()
	return row, col
	
	
	
	
	
	
	
#############################################################3
	
def get_probability():

	pgrid =        [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0] ]
                
	for size in range(len(grid.VESSEL_SIZES)):
	
		for y in range(grid.GRID_HEIGHT):
			for x in range(grid.GRID_WIDTH - (size - 1)):
				if_miss = 1 

				for z in range(size):
					if(attack_grid[y][x+z]) == grid.MISS:
						if_miss = 0
					
				for z in range(size):
					pgrid[y][x + z] += 1 * if_miss

		for y in range(grid.GRID_HEIGHT - (size - 1)):
		
			for x in range(grid.GRID_WIDTH):
				if_miss = 1 
				for z in range(size): 
					if(attack_grid[y+z][x] == grid.MISS):
						if_miss = 0
			
				for z in range(size):
					pgrid[y + z][x] += 1 * if_miss

	prob_list = get_highest_prob(pgrid)
	coords = prob_list[select_random(prob_list)]
	
	#print (prob_list,'\n',coords)
	
	return coords[0], coords[1]


def get_highest_prob(pgrid):
	prob_coords = []
	highest = 0 
	for y in range(grid.GRID_HEIGHT):
		for x in range(grid.GRID_WIDTH):
			if(pgrid[y][x] > highest) and on_checkerboard(y,x):
				highest = pgrid[y][x]
	
	for y in range(grid.GRID_HEIGHT):
		for x in range(grid.GRID_WIDTH):
			if(pgrid[y][x] == highest) and on_checkerboard(y,x):
				prob_coords.append([y,x])
	return prob_coords

def select_random(_list):
	return random.randint(0,len(_list) - 1)	
	
def on_checkerboard(row, col):
	if (col%2) == (row%2):
		return True
					
				# gonna use this later

