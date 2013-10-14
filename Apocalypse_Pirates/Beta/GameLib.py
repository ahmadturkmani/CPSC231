import TKLib
import cfg

# Implements the text box (makes the lines move up	
def output_text(string):
	if cfg.label[0].txt_var.get() == '':
		cfg.label[0].txt_var.set(string)
	else:
		if cfg.label[1].txt_var.get() == '':
			cfg.label[1].txt_var.set(string)
		else:
			if cfg.label[2].txt_var.get() == '':
				cfg.label[2].txt_var.set(string)
			else:
				if cfg.label[3].txt_var.get() == '':
					cfg.label[3].txt_var.set(string)
				else:
					cfg.label[0].txt_var.set(cfg.label[1].txt_var.get())
					cfg.label[1].txt_var.set(cfg.label[2].txt_var.get())
					cfg.label[2].txt_var.set(cfg.label[3].txt_var.get())
					cfg.label[3].txt_var.set(string)

# Calculate where the other pieces are, one by one
def button_press():
	output_text("you entered '" + cfg.entry[0].txt_var.get() + "'")
	cfg.canvas[0].name.coords('pawn', 24,12)