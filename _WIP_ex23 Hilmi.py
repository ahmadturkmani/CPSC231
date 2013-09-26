"""
I'm having troubles with running this program, need to debug before finalization. 
"""
#Import is used to have user input characters without the user being able to see it. 
#Purely for asthetics at this point. 
from getpass import getpass

#Global Variables
row = 1
direction = 'AC'
column = ord('A')
"""
This function is the bit where the formatting and output is sent the console.
linea is the top and bottom border, while lineb is simply a space, to make formatting
look nicer.
"""

def titlescreen(): 
	#The following 5 lines set variables to various lines of text
	global linea
	global lineb
	linea = "################################################" 
	line1 = "# Welcome to a Battlefield game like no other! #"
	line2 = "#  This game was written by Hilmi Abou-Saleh   #"
	line3 = "#          Get ready to begin the game!        #"
	lineb = "#                                              #" 	
	#The text is the sent to the console after being centered
	print(linea.center(80))
	print(lineb.center(80))	
	print(line1.center(80))
	print(line2.center(80))
	print(line3.center(80))
	print(lineb.center(80))
	print(linea.center(80))
	
	beginscpt = "#          Please press enter....              #" #Format
	getpass(beginscpt.center(79)) #Nice bit of text to make letter(s) entered invisible


def initdisplay():
	
	guide1a = "#   The following will guide you place your    #" 
	guide1b = "#         aircraft carrier (5 spaces).         #"
	print(linea.center(80))
	print(lineb.center(80))
	print(guide1a.center(80))
	print(guide1b.center(80))
	
	#Battlefield Grid; displays empty grid with coordinates. Setting up grid.
	row0 = "#  | A | B | C | D | E | F | G | H | I | J |   #" 
	row1 = "# 1|   |   |   |   |   |   |   |   |   |   |   #"
	row2 = "# 2|   |   |   |   |   |   |   |   |   |   |   #"
	row3 = "# 3|   |   |   |   |   |   |   |   |   |   |   #"
	row4 = "# 4|   |   |   |   |   |   |   |   |   |   |   #"	
	row5 = "# 5|   |   |   |   |   |   |   |   |   |   |   #"
	row6 = "# 6|   |   |   |   |   |   |   |   |   |   |   #"
	row7 = "# 7|   |   |   |   |   |   |   |   |   |   |   #"
	row8 = "# 8|   |   |   |   |   |   |   |   |   |   |   #"
	row9 = "# 9|   |   |   |   |   |   |   |   |   |   |   #"
	row10 = "#10|   |   |   |   |   |   |   |   |   |   |   #"
	#Setting user input up
	uirow1 = "#                    Inputs:                   #"							
	
	#Printing grid to console while centering it.
	print(row0.center(80))
	print(row1.center(80))
	print(row2.center(80))
	print(row3.center(80))
	print(row4.center(80))
	print(row5.center(80))
	print(row6.center(80))
	print(row7.center(80))
	print(row8.center(80))
	print(row9.center(80))
	print(row10.center(80))
	print(lineb.center(80))
	print(linea.center(80))
	print(uirow1.center(80)) #Printing user input title
	print(linea.center(80))
	print(lineb.center(80))
	
	
"""This """
def vessel_input():
	global row
	global column	
	#Vessel formatting, setting up for user input
	nameo = "#    Which Vessel would you like to enter:     #"	
	
	_acd = "#           Aircraft Carrier - AC              #"
	_bsd = "#             Battleship - BS                  #"
	_smd = "#              Submarine - SM                  #"
	_dsd = "#              Destroyer - DS                  #"
	print(nameo.center(80))
	print(_acd.center(80))
	print(_bsd.center(80))
	print(_smd.center(80))
	print(_dsd.center(80))
	print(lineb.center(80))
	print(linea.center(80))
	print(lineb.center(80))
	#User input for later call 
	nameso = "#         Please enter the vessel:             #"
	print(nameso.center(80))
	name = input("\033[23;51H")	
	columno = "#              Left Column (A-J):              #"
	print(columno.center(80))
	column = input("\033[23;50H") #Using ANSI escape seq to move cursor
	column = column.upper() #To ensure lowercases aren't different positions
	column = ord(column)
	row = "#               Top Row (1-10):                #"
	print(row.center(80))
	row = input("\033[023;48H")	
	directiono = "#            Direction (H, or V):              #"
	print(directiono.center(80))
	direction = input("\033[023;50H")
	#Final formatting before call
	print(lineb.center(80))
	print(linea.center(80))

	#Call to function
	get_location(name, direction)

def modify_row(previous_vessel_size, name):
	#
	global row
	#global column
	
	#Row calculation to move vessel row
	row = (int(row) + int(previous_vessel_size)) % 10
	
	#Formatting + Displaying Vessel Information
	ro = "#                   Row:"
	ro1 = "                      #"
	co = "#                  Column:" 
	co1 = "                    #"
	#columno = co + str(column) + co1
	rowo = ro + str(row) + ro1
	head1 = "#              Vessel Type: "
	head2 = "                 #"
	header = head1 + name + head2
	print(linea.center(80))
	print(header.center(80))	
	print(rowo.center(80))
	#print(columno.center(80))
	print(linea.center(80))
	
def modify_column(previous_vessel_size, name):
	#Defining Global Variables
	global row
	global column
	
	#Column calculation to move vessel column
	#previous_vessel_size = int(previous_vessel_size) #ISSUE HERE 
	column = (column + int(previous_vessel_size)) % 10
	column = column
	#Formatting + Displaying Vessel Information
	ro = "#                   Row:"
	ro1 = "                      #"
	co = "#                  Column:" 
	co1 = "                    #"
	head1 = "#              Vessel Type: "
	head2 = "                 #"
	header = head1 + name + head2
	rowo = ro + row + ro1
	columno = co + chr(column) + co1
	#print(linea.center(80))
	print(header.center(80))	
	print(rowo.center(80))
	print(columno.center(80))
	#print(linea.center(80))
	



def get_location(name, direction):
	
	#Set up if statement for Different ships
	#Formatting
	print(lineb.center(80))
	print(linea.center(80))
	head1 = "#              Vessel Type: "
	head2 = "                 #"
	header = head1 + name + head2
	di = "#            Direction (H, or V):"
	di1 = "             #"
	dio = di + direction + di1
	print(header.center(80))


	print(dio.center(80))
	print(linea.center(80))
def main():
	titlescreen()
	#initdisplay()
	vessel_input()
	#Battleship Placement
	direction = "V"
	modify_column(5, "BS")
	
	#Submarine Placement
	#direction = "H"
	#modify_row(4, "SM")
	
	#Destroyer Placement
	#direction = "V"
	#modify_column(3, "DS")
	
main()
