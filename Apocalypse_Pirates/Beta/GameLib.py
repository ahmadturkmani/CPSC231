
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
def button_go():
	
	# get row and column from input fields
	col = ord(cfg.entry[0].txt_var.get().upper()) - ord('A')
	row = int(cfg.entry[1].txt_var.get()) - 1
	
	if cfg.chosen == cfg.empty:
		if cfg.grid[row][col] != cfg.empty:
			for i in range(5):
				if cfg.grid[row][col] == cfg.whitepieces[i]:
					cfg.chosen = cfg.grid[row][col]
					output_text('Move this piece (' + chr(col + ord('A')) + "," + str(row + 1) + ') where?')
					cfg.row = row
					cfg.col = col
					cfg.grid[row][col] = cfg.empty
			if cfg.chosen == cfg.empty:
				output_text("That's not your piece!")
		else:
			output_text('That spot is empty')
	else:
		if cfg.grid[row][col] == cfg.empty:
			cfg.grid[row][col] = cfg.chosen
			cfg.chosen = cfg.empty
			redraw_board()
			output_text("Moved piece from (" + chr(cfg.col + ord('A')) + "," + str(cfg.row + 1) + ") to (" + chr(col + ord('A')) + "," + str(row + 1) + ").")
			cfg.button[3].name.config(state = 'normal')
			cfg.button[0].name.config(state = 'disabled')
	# print location to the terminal 
	#output_text("You entered (" + chr(col + ord('A')) + "," + str(row + 1) + ').')
	
	
def redraw_board():

	for i in range(cfg.BOARD_W):
		for j in range(cfg.BOARD_H):
			if cfg.grid[i][j] != cfg.empty:
				# calculate piece position based on board size/row/column/border
				x = ((cfg.BOARD_W/2) * cfg.SQ_WID) + cfg.BOARD_BRDR - ((cfg.SQ_WID/2)*i) + ((cfg.SQ_WID/2)*j) - (cfg.UNIT_W / 2)
				y = cfg.BOARD_BRDR + ((cfg.SQ_HEI/2)*i) + ((cfg.SQ_HEI/2)*j)
				# move the pawn to the location
				cfg.canvas[0].name.coords(cfg.grid[i][j], x, y)
				
def button_move():
	output_text('Choose a piece to move by entering coordinates.')
	cfg.button[0].name.config(state = 'normal')
	cfg.button[3].name.config(state = 'disabled')
	cfg.chosen = cfg.empty
	cfg.entry[0].txt_var.set('COLUMN (A-E)')
	cfg.entry[1].txt_var.set('ROW (1-5)')