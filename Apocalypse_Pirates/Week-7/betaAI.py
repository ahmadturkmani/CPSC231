import grid
import __main__

PIECES = ['BK', 'BP']
OPP_PIECES = ['WP', 'WK']
KNIGHT_MOVE = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]] # all moves a knight can make
PAWN_MOVE = [[-1,1], [-1,0], [-1,-1]]


# takes a valid move
def get_move():
	
	board = __main__.board
	
	piece_loc = find_pieces(board)
	

# returns a list of all the pieces on the board
def get_pieces(board, pieces, opp_pieces):
	
	piece_loc = []	
	
	for i in range(grid.GRID_WIDTH):
		for j in range(grid.GRID_HEIGHT):
			for p in range(len(PIECES)):
				
				if board[grid.List2Dto1D(i,j)] == PIECES[p]:
					piece_loc.append(
