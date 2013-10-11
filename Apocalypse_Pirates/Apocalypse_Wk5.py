#This program is the 5th week submission for Tutorial 2 Group 5's game apocalypse

#Setting Variables
name='pawn'
column=ord('a')
row=1
color='white'
x=0
y=0

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
        print ('please indicate the column, and row at which the', color,name, 'will be placed at')
        column= input('column (a-e): ')
        row= input(' row (1-5): ')
        
        #Call to validate location
        validate_input()

		
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
                   print_location(player, color, name) #Printing location if its valid
              
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
        print('the player',player+"'s",color, name,'is located at:','(', chr((_cold) + ord('a')),',',_rowd+1,')')


def modify(player): 
        #setting global variables
        global _cold
        global _rowd
        
        #calculates location of piece
        _cold=(column + x) #x is the shift in x direction
        _rowd=((row + y) # y is the shift in the y direction
	
	#if locations are valid, will print location of piece, otherwise, wont be printed
        if  0 =< _cold < 5 and 0 =< _rowd < 5:
        	print_location(player,color,name)

        else:
        	return

def main():
	#Setting global variables
        global color
        global x
        global y
        global player
        
        #Setting player to one; redundant, but whatever.
        player = 'one'
        
        show_title() #Prints titlescreen
        input_location('white','pawn') #Inputs user row, column location
        
        #Modifies location, to print location of different pieces 
        modify('one')
        y=1
        color='black'
        modify('two')
        x=1
        y=1
        modify('two')
main()
