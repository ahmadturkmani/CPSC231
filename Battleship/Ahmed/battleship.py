#AHMED ELBANNAN
#T2G5

import grid
import t2_g5_ai
import human

def main():
	
	for i in range(grid.NUM_OF_VESSELS):
		human.get_location(i)
		t2_g5_ai.get_location(i)
		grid.print_grid(t2_g5_ai.defend_grid)
		grid.print_grid(human.defend_grid)

	while not all_vessels_sunk():
		row, col = human.get_choice()
		grid.drop_bomb(human.attack_grid, t2_g5_ai.defend_grid, row, col)
	
		row, col = t2_g5_ai.get_choice()
		grid.drop_bomb(t2_g5_ai.attack_grid, human.defend_grid, row, col)

main()
	
	
	


