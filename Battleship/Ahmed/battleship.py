
import grid
import t2_g5_ai
import human

for i in range(grid.NUM_OF_VESSELS):
	human.get_location(i)
	t2_g5_ai.get_location(i)
	grid.print_grid(t2_g5_ai.defend_grid)
	grid.print_grid(human.defend_grid)

	
	
	
	


