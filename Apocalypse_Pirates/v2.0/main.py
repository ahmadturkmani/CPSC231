#V2.0 of this program will eventually contain a working version of apocalpyse playable
#to the spec. documented in the CPSC231 website. 
#This will contain the main game loop.
#T2G5 Apocalypse Project - main.py:

#Imports
import sys
import human
import ai
import grid

def title_screen():
  #Print Titlescreen
  print("Welcome to T2G5's Apocalypse Game")
  

def __main__():
  #Initialization Loop
  human.get_choice()
  while initialization is False:
    grid.initialize()
  
  #Game Loop 
  while get_winner() is False:
    human.get_choice()
    ai.get_choice()
    grid.make_move()
  
  if get_winner() is True:
    display_winner()
    save_state()
    sys.exit()

#End main.py 
