#********************************************
# By Ahmed Elbannan
# September 18th 2013
# Battleship CPSC231 (Limited Edition! ;] )
#********************************************

# Title Screen! Now a function!
def draw_titlescreen():
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

# Ask user to place aircraft carrier
print ('Where would you like to place your Aircraft Carrier? (5 spaces)');
x_air = ord(input('Enter horizontal position (A-J):\t')) - ord('A');
y_air = (int(input('Enter vertical position (1-10):\t\t')) - 1);
print();

# based on input, calculate the position of the battleship
x_bat = (x_air + 5) % 10;
y_bat = y_air;

# now calculate position of sub
x_sub = x_bat;
y_sub = (y_bat + 4) % 10;

# the same with the destroyer
x_des = (x_sub + 3) % 10;
y_des = y_sub;

# tell the user the position of their fleet
print ('Your Aircraft Carrier is located at (' + chr(x_air + ord('A')) + ', ' + str(y_air + 1) + ')');
print ('Your Battleship is located at (' + chr(x_bat + ord('A')) + ', ' + str(y_bat + 1) + ')');
print ('Your Submarine is located at (' + chr(x_sub + ord('A')) + ', ' + str(y_sub + 1) + ')');
print ('Your Destroyer is located at (' + chr(x_des + ord('A')) + ', ' + str(y_des + 1) + ')');
