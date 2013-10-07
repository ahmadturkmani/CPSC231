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
        print ('please indicate the column, and row at which the', color,
                          name, 'will be placed at')
        column= ord(input('column (a-e): ')) - ord('a')
        row= int(input(' row (1-5): ')) - 1

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
        modify('one')
        y=1
        color='black'
        modify('two')
        x=1
        y=1
        modify('two')
main()

