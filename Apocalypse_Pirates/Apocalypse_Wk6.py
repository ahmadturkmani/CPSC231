#This program is the 5th week submission for Tutorial 2 Group 5's game apocalypse

#Setting Variables
name='pawn'
column=ord('a')
row=1
color='white'
x=0
y=0
b = 'e'

#Global Constants
GRID_HEIGHT = 5
GRID_WIDTH = 5
grid = [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b]

#Initial starting position of the two player's pieces
#White Location and Name
PIECEWI = [15, 21, 22, 23, 19, 20, 24]
PIECEW = ['w1', 'w2', 'w3', 'w4', 'w5', 'W1', 'W2']

#Black Location and Name
PIECEBI = [5, 1, 2, 3 ,9, 0, 4]
PIECEB = ['b1', 'b2', 'b3', 'b4', 'b5', 'B1', 'B2']



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
        
def select_piece(player):
	global index
	print("0 - w1")
	print("1 - w2")
	print("2 - w3")	
	print("3 - w4")
	print("4 - w5")		
	print("5 - W1")
	print("6 - W2")
			
	piece = input("Please select a piece to move(0 - 6): ")
	piece = int(piece)
	if 0 <= piece < 7:
		index = piece		
	else:
		print("You have entered an invalid piece, please try again.")
		select_piece(player)
		
				
	


def input_location(color,name): #Function, gets input from user

        #Global variables
        global x
        global y
        
        #Prompt for user input
        print ('Please indicate the column, and row at which the', name, 'will be placed at:')
        x = input('column (a-e): ')
        y = input('row (1-5): ')
        print()

        #Call to validate location
        print(x,y)
        validate_input()


def validate_input(): #Validates location and prompts user to fix error

       #Global variables
       global x
       global y
       
       #Checks if length is appropriate for input
       print(x,y)
       if 0 < len(y) < 2 and 0 < len(x) < 2:
       
           y = int(y) - 1 #converting row into integer, and storing it from 0-4
           x = ord(x) - ord('a')# converting column into ordinal values, and storing it from 0-4
           
           #Checking if row is less acceptable limits
           if  0 <= y < 5:
           	
               #Checking if column is within acceptable limits
               if 0 <= x < 5:
                   #print_location(player, color, name) #Printing location if its valid
                   return True
               else: #If column is invalid prompts user for input after displaying issue
                   print("You have entered an invalid column")
                   input_location(color, name)
          
           else: #If row is invalid prompts user for input after displaying issue
               print("You have entered an invalid row")
               input_location(color,name)
       
       else: #If the string is too long for acceptable input, prompts user for re-input
           print("You have entered invalid coordinates")
           input_location(color,name)

def print_location(player,color,name): #Prints location
		
		print("The location of the " + color + ' ' + name + " is (", chr(x + ord('a')), ',',  str(y + 1), ')')
		print()


def store_piece(x, y, index, player):
	global grid
	
	if y > 0:
		x_pos = ((GRID_WIDTH * y) + x)
		print(x_pos)
		grid[x_pos] = piece[index]

	else:
		x_pos = x
		grid[x_pos] = 't'
		print(x_pos)
			
	
def print_grid():
	global grid
	print('________________')
	print('|  | A B C D E |')
	print('----------------')
	
	for y_counter in range(0, GRID_HEIGHT):
		print( '|0' + str(y_counter + 1) + '| ', end = '')
			
		for x_counter in range(0, GRID_WIDTH):
			x_pos = (y_counter * 5)+ x_counter 
			print(grid[x_pos] + ' ', end = '')
		print('|')
		print()

def set_board():
	keep_running = True
	i = 0
	
	while i < 7:
		grid[PIECEWI[i]] = PIECEW[i]
		i = i + 1 
	i = 0
	while i < 7:
		grid[PIECEBI[i]] = PIECEB[i]
		i = i + 1
	print_grid()


def enter_choice():
	choice = ''
	while not choice == 'q':
		choice = input('Enter choice: ')


def main():
	show_title() #Prints titlescreen
	set_board()
	while True:
		select_piece('white')
		input_location('white', PIECEW[index])
		store_piece(x, y, index, 'white')
		print_grid()
			        
main()
