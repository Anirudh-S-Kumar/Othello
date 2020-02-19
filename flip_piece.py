import valid_move_2
import game_board

def flip(player, move):
	if valid_move_2.r_val(player, move):
		for i in valid_move_2.r_val(player, move):
			for x,y in i:
				game_board.gb()[x][y] = player		
						