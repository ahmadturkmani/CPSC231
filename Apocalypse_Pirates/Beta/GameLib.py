
import TKLib # graphics (not used here YET)
import cfg # variables

# Implements the 'terminal' (makes the lines move up). used instead of print
def output_text(string):

	empty = 0 # if any line is empty
	
	# check if any line is empty, if so then use it
	for i in range(6):
		if cfg.label[i].txt_var.get() == '':
			cfg.label[i].txt_var.set(string)
			empty = 1
			break
			
	# if all lines are full, then move all lines up one and insert new line in bottom
	if empty == 0:
		for i in range(5):
			cfg.label[i].txt_var.set(cfg.label[i+1].txt_var.get())
		cfg.label[5].txt_var.set(string)


# React after button press
def button_press():
	
	# get row and column from input fields
	cfg.col = ord(cfg.entry[0].txt_var.get()) - ord('A')
	cfg.row = int(cfg.entry[1].txt_var.get()) - 1
	
	# calculate piece position based on board size/row/column/border
	x = ((cfg.BOARD_W/2) * cfg.SQ_WID) + cfg.BOARD_BRDR - ((cfg.SQ_WID/2)*cfg.row) + ((cfg.SQ_WID/2)*cfg.col) - (cfg.UNIT_W / 2)
	y = cfg.BOARD_BRDR + ((cfg.SQ_HEI/2)*cfg.row) + ((cfg.SQ_HEI/2)*cfg.col)
	
	# print location to the terminal 
	output_text("You entered (" + chr(cfg.col + ord('A')) + "," + str(cfg.row + 1) + ').')
	
	# move the pawn to the location
	cfg.canvas[0].name.coords('pawn', x,y)