import move_interpreter
import valid_move
import valid_move_2
import flip_piece
import game_board


def index_swap(player,move):  # function for playing a move
	if player == 1:
		for x in valid_move_2.r_val(1,move):
			for i in x:
				k = move_interpreter.rev_move_conv(i)
				game_board.black_index.append(k)
				if game_board.white_index.count(k) == 0:
					continue
				else:
					game_board.white_index.remove(k)
	elif player==2:
		for x in valid_move_2.r_val(2,move):
			for i in x:
				k = move_interpreter.rev_move_conv(i)
				game_board.white_index.append(k)
				if game_board.black_index.count(k) == 0:
					continue
				else:
					game_board.black_index.remove(k)

def play_move(player,move):
	index_swap(player,move)
	flip_piece.flip(player, move)
	x,y = move_interpreter.move_conv(move)
	game_board.gb()[x][y] = player
	if player == 1:
		game_board.black_index.append(move.upper())
	else:
		game_board.white_index.append(move.upper())
	game_board.black_index = list(dict.fromkeys(game_board.black_index))
	game_board.white_index = list(dict.fromkeys(game_board.white_index))