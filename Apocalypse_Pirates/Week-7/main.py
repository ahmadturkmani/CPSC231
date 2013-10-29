#This program is the 7th week submission for Tutorial 2 Group 5's game apocalypse
###################################################################################
#Imports
import grid
import human
import ai

board = [grid.b for i in range(grid.GRID_WIDTH * grid.GRID_HEIGHT)]

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
		

def main():
	global board
	#Initialization
	# add pieces to board and print board. 
	board = grid.setup_board(board)
	grid.print_board(board)

	# game loop. Play till user decides to quit
	while grid.get_winner(board):
		
		human.get_choice() 
		ai.get_move()
		board = grid.check_knight(board)
			
main()
