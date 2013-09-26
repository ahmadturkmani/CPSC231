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

def print_vessel(name, x, y, direction):
    print('Your ' + name + ' is located at (' + chr(x + ord('A')) + ', ' + str(y + 1) + ')');
    print('It is positioned ' + direction + 'y.');
    print();
    return;
# end

def get_location(name, spaces):
    global x; # this function can edit x
    global y; # this function can edit y
    print ('Where would you like to place your ' + name + ' (' + str(spaces) + 'spaces)');
    x = ord(input('Enter horizontal position (A-J):\t')) - ord('A');
    y = (int(input('Enter vertical position (1-10):\t\t')) - 1);
    print();
    return;
# end
    
# Calculate next ship position based on previous ship dimensions   
def modify_row(name, size):
    global y; # this function can edit y
    y = (y + size) % 10;
    print_vessel(name, x, y, direction);
    return;
# end

# Calculate next ship position based on previous ship dimensions   
def modify_column(name, size):
    global x; # this function can edit x
    x = (x + size) % 10;
    print_vessel(name, x, y, direction);
    return;
# end

def main():
    global direction;  # this function can edit direction
        # prints name, location, and orientation of a vessel
    print_titlescreen();
        # Ask user to place aircraft carrier
    get_location('Aircraft Carrier', 5);
    direction = 'horizontal';
    print_vessel('Aircraft Carrier', x, y, direction);
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
