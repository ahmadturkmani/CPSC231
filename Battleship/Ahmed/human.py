
import grid

attack_grid = [ [grid.B for i in range(grid.GRID_WIDTH)] for j in range(grid.GRID_HEIGHT)]
defend_grid = [ [grid.B for i in range(grid.GRID_WIDTH)] for j in range(grid.GRID_HEIGHT)]

# let's the user choose where to place vessel
def get_location(index):
	print ('Where would you like to place your ' + grid.VESSEL_NAME[index] + '? (' + str(grid.VESSEL_SIZE[index]) + ' spaces)');
	col = input('Horizontal position?\t(A-J):');
	row = input('Vertical position? \t(1-10):');
	dir = input('Direction? [h]orizontal or [v]ertical:');
	print();
	validate_location(index, row, col, dir)
	
	
def validate_location(index, row, col, dir):


	col = (ord(col.upper()) - ord('A'));
	row = (int(row) - 1);
		
	print(row, col)	
	if (dir == 'h') and (-1 < col < (grid.GRID_WIDTH - grid.VESSEL_SIZE[index])) and (-1 < row < grid.GRID_HEIGHT):
		if not grid.has_overlap(defend_grid, index, row, col, dir):
			grid.add_vessel(defend_grid, index, row, col, dir)
		else:
			print('This ship overlaps with another!')
			get_location(index);
			validate_location(index, row, col, dir);
			
	elif dir == 'v' and (-1 < row < (grid.GRID_HEIGHT - grid.VESSEL_SIZE[index])) and (-1 < col < grid.GRID_WIDTH):  
		if not grid.has_overlap(defend_grid, index, row, col, dir):
			grid.add_vessel(defend_grid, index, row, col, dir)
		else:
			print('This ship overlaps with another!')
			get_location(index);
			validate_location(index, row, col, dir);

	else:
		print('Not a valid location!')
		get_location(index);
		validate_location(index, row, col, dir);
	print()
