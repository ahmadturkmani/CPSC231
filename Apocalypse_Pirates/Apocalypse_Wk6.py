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
        

def input_location(color,name): #Function, gets input from user

        #Global variables
        global column
        global row
        
        #Prompt for user input
        print ('Please indicate the column, and row at which the', color,name, 'will be placed at:')
        column= input('column (a-e): ')
        row= input('row (1-5): ')
        print()

        #Call to validate location
        validate_input()

def store_piece(x, y, piece, player):
	global grid
	
	if y > 0:
		x_pos = ((GRID_WIDTH * y) + x) - 1
		print(x_pos)
		grid[x_pos] = 't'

	else:
		x_pos = x
		grid[x_pos] = 't'
		print(x_pos)
		
	
	
	
def print_grid():
	global grid
	print('________________')
	print('|  | A B C D E |')
	print('----------------')
	x_counter = 0
	y_counter = 0
	for y_counter in range(GRID_HEIGHT):
		print( '|0' + str(y_counter + 1) + '| ', end = '')
			
		for x_counter in range(0, GRID_WIDTH):
			x_pos = (x_counter * 5)+ x_counter -1 
			print(grid[x_pos] + ' ', end = '')
		print('|')
		print()

		
def validate_input(): #Validates location and prompts user to fix error

       #Global variables
       global row
       global column
       
       #Checks if length is appropriate for input
       if 0 < len(column) < 2 and 0 < len(row) < 2:
       
           row = int(row) - 1 #converting row into integer, and storing it from 0-4
           column = ord(column) - ord('a')# converting column into ordinal values, and storing it from 0-4
           #Checking if row is less acceptable limits
           if  0 <= row < 5:
           	
               #Checking if column is within acceptable limits
               if 0 <= column < 5:
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
		
		print("The location of the " + color + ' ' + name + " is (", chr(column + ord('a')), ',',  str(row + 1), ')')
		print()

def main():
	
	#Setting global variables
        global color
        global x
        global y
        global name

        show_title() #Prints titlescreen
        input_location('white','pawn') #Inputs user row, column location
        store_piece(row, column, name, color)
        print_grid()
        
main()
