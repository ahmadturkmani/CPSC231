#********************************************
# By Ahmed Elbannan
# September 22nd 2013
# Battleship CPSC231 (Limited Edition! ;] )
#********************************************

# global variables
vessel_name = 'Aircraft Carrier';
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

def print_vessel(name, x, y, direction):
    print('Your ' + name + ' is located at (' + chr(x + ord('A')) + ', ' + str(y + 1) + ')');
    print('It is positioned ' + direction + 'y.');
    print();
    return;
# end

def input_vessel(name, spaces):
    print ('Where would you like to place your ' + name + ' (' + str(spaces) + 'spaces)');
    x = ord(input('Enter horizontal position (A-J):\t')) - ord('A');
    y = (int(input('Enter vertical position (1-10):\t\t')) - 1);
    print();
    return;
# end
    
def calc_position(name, h_size, v_size):
    x = (x + h_size) % 10;
    y = (y + v_size) % 10;
    print_vessel(name, x, y, direction);
    return;
# end

def main():
    # prints name, location, and orientation of a vessel
    print_titlescreen();
    
    # Ask user to place aircraft carrier
    input_vessel('Aircraft Carrier', 5);
    direction = 'horizontal';
    print_vessel('Aircraft Carrier', x , y, direction);
    
    # based on input, calculate the position of the battleship
    x_bat = (x_air + 5) % 10;
    y_bat = y_air;
    print_vessel('Battleship', x_bat, y_bat, 'vertical');
    
    # now calculate position of sub
    x_sub = x_bat;
    y_sub = (y_bat + 4) % 10;
    print_vessel('Submarine', x_sub, y_sub, 'horizontal');
    
    # the same with the destroyer
    x_des = (x_sub + 3) % 10;
    y_des = y_sub;
    print_vessel('Destroyer', x_des, y_des, 'vertical');
    return;
# end

main(); 
