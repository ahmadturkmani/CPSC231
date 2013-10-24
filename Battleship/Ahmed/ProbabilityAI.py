import random

GRID_HEIGHT = 10
GRID_WIDTH = 10
VESSEL_SIZE = 5


attack_grid =   [['~' for i in range(GRID_WIDTH)] for j in range(GRID_HEIGHT)]

attack_grid[0][4] = 'O'
attack_grid[4][4] = 'O'




def get_probability(size, grid):


	for y in range(GRID_HEIGHT):
		for x in range(GRID_WIDTH - (size - 1)):
			if_hit = 1
			if_miss = 1 

			for z in range(size):
				if(attack_grid[y][x+z]) == 'X':
					if_hit = 2

				if(attack_grid[y][x+z]) == 'O':
					if_miss = 0
					## we will decrease the probablilty accordingly because of less available overlaps thanks to having an 'O' in place
			
			for z in range(size):
				grid[y][x + z] += 1 * if_miss * if_hit

	for y in range(GRID_HEIGHT - (size - 1)):
		for x in range(GRID_WIDTH):
			if_hit = 1
			if_miss = 1 
			for z in range(size): 
				if(attack_grid[y+z][x] == 'X'):
					if_hit = 2
				if(attack_grid[y+z][x] == 'O'):
					if_miss = 0
				grid[y + z][x] += 1 * if_miss * if_hit

	for i in range(GRID_HEIGHT):
		print(grid[i])

	prob_list = get_highest_prob(grid)
	coords = prob_list[select_random(prob_list)]
	
	print (prob_list,'\n',coords)
	
	return grid


def get_highest_prob(grid):
	prob_coords = []
	highest = 0 
	for y in range(GRID_HEIGHT):
		for x in range(GRID_WIDTH):
			if(grid[y][x] > highest):
				highest = grid[y][x]
	
	for y in range(GRID_HEIGHT):
		for x in range(GRID_WIDTH):
			if(grid[y][x] == highest):
				prob_coords.append([y,x])
	return prob_coords

def select_random(_list):
	return random.randint(0,len(_list) - 1)	

grid =        [
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
for i in range(2,5):
	grid = get_probability(i, grid)
