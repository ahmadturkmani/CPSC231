#This program is the 4th week submission for Tutorial 2 Group 5's game apocalypse

name='pawn'
column=ord('a')
row=1
color='white'
x=0
y=0

def show_title():
        welcome=('###########################\n'
               '#  WELCOME TO Apocalypse  #\n'
               '###########################\n')
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

def input_location(color,name):
        global column
        global row
        print ('please indicate the column, and row at which the', color,name, 'will be placed at')
        column= ord(input('column (a-e): ')) - ord('a')
        row= int(input(' row (1-5): ')) - 1

def show_test(row, column):
       global row
       global column
       if 0 < len(column) < 2 and 0 < len(row) < 2:
           if  0 <= row < 5:
               if 0 <= column < 5:
                   print_location(player, color, name)
               else: 
                   print("You have entered an invalid column")
                   input_location(color, name)
           else:
               print("You have entered an invalid row")
               input_location(color,name)
       else:
           print("You have entered invalid coordinates")
           input_location(color,name)

def print_location(player,color,name):
        print('the player',player+"'s",color, name,'is located at:','(', chr((column) + ord('a')),',',row+1,')')



def modify(player):
        global row
        global column
        column=(column + x) % 5
        row=((row + y) % 5)
        print_location(player,color,name)

def main():
        global color
        global x
        global y
        show_title()
        input_location('white','pawn')
        show_test(row, column)
        #modify('one')
        #y=1
        #color='black'
        #modify('two')
        #x=1
        #y=1
        #modify('two')
main()

