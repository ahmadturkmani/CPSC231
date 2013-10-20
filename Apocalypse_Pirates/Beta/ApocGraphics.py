 #########################################################################################
# By:     Ahmed Elbannan, Hilmi Abou-Saleh, Ahmad Turkmani, Namhyuk Woo, Nasir Osman      #
# Date:   September 25th 2013                                                             #
# Name:   Apocalypse Tutorial II Collector's Edition                                      #
 ######################################################################################### 

# import the other modules
import TKLib # tkinter graphics
import GameLib # Game Logic
import cfg # used for variables

# CONSTANTS
# size of screen
cfg.WIDTH = 960
cfg.HEIGHT = 720
# width of board squares
cfg.SQ_WID = 48
cfg.SQ_HEI = 24
# board dimensions
cfg.BOARD_W = 5
cfg.BOARD_H = 5
# Borderaround board
cfg.BOARD_BRDR = 24
# size of unit image
cfg.UNIT_H = 48
cfg.UNIT_W = 48
# number of lines in 'terminal'
cfg.TER_LINES = 6
# terminal size
cfg.TER_SIZE = 192

# row/column variables
cfg.col = ord('A');
cfg.row = 0;

# grid stuff
cfg.empty = 'X' 
cfg.grid = [ [cfg.empty for i in range (cfg.BOARD_W)] for j in range(cfg.BOARD_H)]
	
# Functions chill here 	
def main():
	# makes a list for each kind of widget (for ease of organization/access)
	cfg.canvas = ['' for i in range(9)]
	cfg.label = ['' for i in range(99)]
	cfg.entry = ['' for i in range(9)]
	cfg.button = ['' for i in range(9)]
	cfg.img = ['' for i in range(99)]
	cfg.blackpieces = [('bpawn' + str(i)) for i in range(5)]
	cfg.whitepieces = [('wpawn' + str(i)) for i in range(5)]
	
	# make the root window (the actual window) 
	cfg.root = TKLib.window('spr_back.gif', cfg.WIDTH, cfg.HEIGHT)
	cfg.root.name.title('Apocalypse') # give it a name
	
	# Add the title in a label (may change to canvas later)
	cfg.label[0] = TKLib.LabelImg(cfg.root.name, 0, 0, 960, 128)
	cfg.img[0] = TKLib.load_image('spr_title.gif')
	cfg.label[0].init(cfg.img[0])
	
	# Add the game canvas (where the board will  be) and add a piece
	cfg.canvas[0] = TKLib.MyCanvas(cfg.root.name, 336, 264, 288, 192)
	cfg.canvas[0].init('black')
	cfg.img[1] = TKLib.load_image('spr_board.gif')
	cfg.canvas[0].add_pic(cfg.img[1], 0, 24, 'board')
	
	#add pieces
	cfg.img[2] = TKLib.load_image('spr_whitepawn.gif')
	cfg.img[3] = TKLib.load_image('spr_blackpawn.gif')
	
	for i in range(5):
		cfg.canvas[0].add_pic(cfg.img[3], 0, 0, 'bpawn' + str(i))
		cfg.grid [0][i] = 'bpawn' + str(i)
	
	for i in range(5):
		cfg.canvas[0].add_pic(cfg.img[2], 0, 0, 'wpawn' + str(i))
		cfg.grid [4][i] = 'wpawn' + str(i)
	
	# The entry boxes to enter coordinates in 
	cfg.entry[0] = TKLib.Entry(cfg.root.name, 496, 672, 192, 32)
	cfg.entry[0].init('')
	cfg.entry[1] = TKLib.Entry(cfg.root.name, 688, 672, 192, 32)
	cfg.entry[1].init('')
	
	# the confirm button (after entering a location)
	cfg.button[0] = TKLib.Button(cfg.root.name, 880, 672, 64, 32)
	cfg.button[0].init('Go!', GameLib.button_go, 'disabled')
	
	cfg.button[1] = TKLib.Button(cfg.root.name, 880, 512, 64, 32)
	cfg.button[1].init('Load', GameLib.button_go,'disabled')
	
	cfg.button[2] = TKLib.Button(cfg.root.name, 880, 560, 64, 32)
	cfg.button[2].init('Save', GameLib.button_go,'disabled')
	
	cfg.button[3] = TKLib.Button(cfg.root.name, 880, 608, 64, 32)
	cfg.button[3].init('Move', GameLib.button_move, 'normal')
	
	# the frame that will hold our 'mini terminal'
	cfg.frame = TKLib.Frame(cfg.root.name, 16, 704 - cfg.TER_SIZE, 448, cfg.TER_SIZE)
	cfg.frame.init()
	
	# add the lines to the 'terminal'
	for i in range(6):
		cfg.label[i] = TKLib.Label(cfg.frame.name, 0, (cfg.TER_SIZE/cfg.TER_LINES)*i, 288, (cfg.TER_SIZE/cfg.TER_LINES))
		cfg.label[i].init('')
	
	GameLib.redraw_board()
	# the main game loop
	cfg.root._loop()

main()
