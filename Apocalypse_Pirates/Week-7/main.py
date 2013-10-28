#This program is the 7th week submission for Tutorial 2 Group 5's game apocalypse
###################################################################################
#Imports
import grid
import human
import ai


def show_title():#Printing initialziation - intro screen

        print('###################################################')
        print('#    #   ###  #=# #==   #   #   \ / ###  === #==  #')
        print('#   #=#  #==# # # #    #=#  #    #  #==# \=  #=   #')
        print('#  #   # #    #=# #== #   # #==  #  #    ==/ #==  #')
        print('###################################################')
        print("~~~~~~~~~~TUTORIAL II COLLECTOR'S EDITION~~~~~~~~~~")
        print('\\\\\\\\\\###############################//////////')
        print()
        print('~~~~~~~~\Created by the Apocalyptic Pirates/~~~~~~~')
        print('~~~~~~~~~\________copyright 2013(c)_______/~~~~~~~~')
        print()



		
		

def get_winner(): #Checks if AI, or Human has won, prints trophy if human wins, otherwise prints you lose. 
	black_alive = False
	white_alive = False
	for i in range(grid.GRID_HEIGHT * grid.GRID_WIDTH): #Running loop a total of 5x5 times; 25
		if grid.grid[i] == "BP" or grid.grid[i] ==  "BK": 
			black_alive = True
		if grid.grid[i] == "WP" or grid.grid[i] == "WK":
			white_alive = True
	if white_alive == True and black_alive == True:		
		return True
	elif white_alive == True and black_alive == False:
		print(	'/---------------------------\\n|----------YOU WIN!----------|\n==============================\n| | | | | | | | | | | | | | ||\n******************************\n             | |                \n       ==============')
		return False
	elif black_alive == True and white_alive == False:
		print("You Lose.")
		return False
		

def main():
	#Initialization
	# add pieces to board and print board. 
	grid.setup_board()
	grid.print_board()

	# game loop. Play till user decides to quit
	while get_winner():
		grid.check_knight()
		human.get_choice()
		ai.get_move()
			
main()
