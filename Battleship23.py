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
    return;
# end

def print_vessel(name):
    print('Your ' + name + ' is located at (' + chr(x + ord('A')) + ', ' + str(y + 1) + ')');
    print('It is positioned ' + direction + 'y.');
    print();
    return;
# end

def input_vessel(name, spaces):
    global x; # this function can edit x
    global y; # this function can edit y
    print ('Where would you like to place your ' + name + ' (' + str(spaces) + 'spaces)');
    x = ord(input('Enter horizontal position (A-J):\t')) - ord('A');
    y = (int(input('Enter vertical position (1-10):\t\t')) - 1);
    print();
    return;
# end
    
# Calculate next ship position based on previous ship dimentions   
def calc_position(name, h_size_prev, v_size_prev):
    global x; # this function can edit x
    global y; # this function can edit x
    x = (x + h_size_prev) % 10;
    y = (y + v_size_prev) % 10;
    print_vessel(name);
    return;
# end

def main():
    global direction;  # this function can edit direction
        # prints name, location, and orientation of a vessel
    print_titlescreen();
        # Ask user to place aircraft carrier
    input_vessel('Aircraft Carrier', 5);
    direction = 'horizontal';
    print_vessel('Aircraft Carrier');
        # based on input, calculate the position of the battleship
    direction = 'vertical';
    calc_position('Battleship', 5, 0);
        # now calculate position of sub
    direction = 'horizontal';
    calc_position('Submarine', 0, 4);
        # the same with the destroyer
    direction = 'vertical';
    calc_position('Destroyer', 3, 0);
    return;
# end

main(); 
