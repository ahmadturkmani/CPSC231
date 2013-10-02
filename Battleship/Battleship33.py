#********************************************
# By Ahmed Elbannan
# September 22nd 2013
# Battleship CPSC231 (Limited Edition! ;] )
#********************************************

# global variables
direction = 'horizontal';
x = ord('A');
y = 0;

# Title Screen! Now a function!
def print_titlescreen():
    print();
    print('________________________________________');
    print('|*********WELCOME TO BATTLESHIP!*******|');
    print('|**************************************|');
    print('|**************************************|');
    print('|*********A game like no other!********|');
    print('|**************************************|');
    print('|**************************************|');
    print('|**************************************|');
    print();
    return;
# end

def print_vessel(name):
    print('Your ' + name + ' is located at (' + chr(x + ord('A')) + ', ' + str(y + 1) + ')');
    print('It is positioned ' + direction + 'y.');
    print();
    return;
# end

def get_location(name, spaces):
    global x; # this function can edit x
    global y; # this function can edit y
    print ('Where would you like to place your ' + name + ' (' + str(spaces) + ' spaces)');
    x = input('Enter horizontal position (A-J):');
    y = input('Enter vertical position (1-10) :');
    print();
    return;
# end
    
# Calculate next ship position based on previous ship dimensions   
def modify_row(name, size):
    global y; # this function can edit y
    y = (y + size) % 10;
    print_vessel(name);
    return;
# end

# Calculate next ship position based on previous ship dimensions   
def modify_column(name, size):
    global x; # this function can edit x
    x = (x + size) % 10;
    print_vessel(name);
    return;
# end

def validate_location(name, size, direction):
	global x; # this function can edit x
	global y; # this function can edit y
	# check if string is a single letter or smaller than a three digit number, if not, asks for input again, then checks
	if (len(x) == 1) and (len(y) < 3):
		x = (ord(x) - ord('A'));
		y = (int(y) - 1);
		# checks if location is on the board and if the ship will fit, if not asks for input again and checks again
		if (direction == 'horizontal') and (-1 < x < (10 - size)) and (-1 < y < 10):
			print_vessel('Aircraft Carrier');
			print('The end of your ' + name + ' is located at (' + chr(((x + size - 1) % 10) + ord('A')) + ', ' + str(y + 1) + ')');
			print();
		elif direction == 'vertical' and (-1 < y < (10 - size)) and (-1 < x < 10):  
			print_vessel('Aircraft Carrier', x, y, direction);
			print('The end of your ' + name + ' is located at (' + chr(x + ord('A')) + ', ' + str(((y + size - 1) % 10) + 1) + ')');
			print();
		else:
			print('The location you entered is not on the board!');
			get_location('Aircraft Carrier', 5);
			validate_location(name, size, direction);
	else:
		print('Please enter a LETTER (between A-J) and a NUMBER (between 1-10!)');
		get_location('Aircraft Carrier', 5);
		validate_location(name, size, direction);
	return;
		

def main():
	global direction;  # this function can edit direction
        # prints name, location, and orientation of a vessel
	print_titlescreen();
        # Ask user to place aircraft carrier
	get_location('Aircraft Carrier', 5);
	direction = 'horizontal';	
	validate_location('Aircraft Carrier', 5, direction);
        # based on input, calculate the position of the battleship
	direction = 'vertical';
	modify_column('Battleship', 5);
        # now calculate position of sub
	direction = 'horizontal';
	modify_row('Submarine', 4);
        # the same with the destroyer
	direction = 'vertical';
	modify_column('Destroyer', 3);
	return;
# end

main(); 
