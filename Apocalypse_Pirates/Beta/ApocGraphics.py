###########################################################################################
# By:     Ahmed Elbannan, Hilmi Abou-Saleh, Ahmad Turkmani, Namhyuk Woo, Nasir Osman      #
# Date:   September 25th 2013                                                             #
# Name:   Apocalypse Tutorial II Collector's Edition                                      #
###########################################################################################

import TKLib
import GameLib
import cfg

cfg.WIDTH = 960
cfg.HEIGHT = 720
cfg.SQ_WID = 48
cfg.SQ_HEI = 24
cfg.BOARD_W = 5
cfg.BOARD_H = 5
cfg.x = ord('A');
cfg.y = 0;


	
# Functions chill here 	
def main():
	cfg.canvas = ['' for i in range(9)]
	cfg.label = ['' for i in range(99)]
	cfg.entry = ['' for i in range(9)]
	cfg.button = ['' for i in range(9)]
	cfg.img = ['' for i in range(99)]
	
	cfg.root = TKLib.window('spr_back.gif', cfg.WIDTH, cfg.HEIGHT)
	cfg.root.name.title('Apocalypse')
	
	cfg.label[0] = TKLib.LabelImg(cfg.root.name, 0, 0, 960, 128)
	cfg.img[0] = TKLib.load_image('spr_title.gif')
	cfg.label[0].init(cfg.img[0])
	
	cfg.canvas[0] = TKLib.MyCanvas(cfg.root.name, 336, 264, 288, 192)
	cfg.canvas[0].init('black')
	cfg.img[1] = TKLib.load_image('spr_board.gif')
	cfg.img[2] = TKLib.load_image('spr_whitepawn.gif')
	cfg.canvas[0].add_pic(cfg.img[1], 0, 24, 'board')
	cfg.canvas[0].add_pic(cfg.img[2], 24, 24, 'pawn')

	cfg.entry[0] = TKLib.Entry(cfg.root.name, 496, 672, 384, 32)
	cfg.entry[0].init('')
	cfg.button[0] = TKLib.Button(cfg.root.name, 880, 672, 64, 32)
	cfg.button[0].init('Go!', GameLib.button_press)

	cfg.frame = TKLib.Frame(cfg.root.name, 16, 512, 448, 192)
	cfg.frame.init()

	cfg.label[0] = TKLib.Label(cfg.frame.name, 0, 0, 288, 48)
	cfg.label[0].init('Where would you like to place your pawn?')
	cfg.label[1] = TKLib.Label(cfg.frame.name, 0, 48, 288, 48)
	cfg.label[1].init('Enter Column(A-E)')
	cfg.label[2] = TKLib.Label(cfg.frame.name, 0, 96, 288, 48)
	cfg.label[2].init('')
	cfg.label[3] = TKLib.Label(cfg.frame.name, 0, 144, 288, 48)
	cfg.label[3].init('')
	cfg.root._loop()

main()
