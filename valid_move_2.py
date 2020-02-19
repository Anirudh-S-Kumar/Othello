import valid_move
import move_interpreter
import game_board


def in_bw_pieces(op):  # taking function variable as the o/p from line_bw 
	final = []	
	if op:
		k = op[0]
		for i in k:
			false_var = 0
			temp = []
			if i[-1] == 1:
				start_piece = min(move_interpreter.move_conv(i[0]),move_interpreter.move_conv(i[1]))
				rnge = abs(move_interpreter.move_conv(i[0])[0] - move_interpreter.move_conv(i[1])[0])
				for x in range(1,rnge):
					if (game_board.gb()[start_piece[0] + x][start_piece[1] + x]) == 0 or (game_board.gb()[start_piece[0] + x][start_piece[1] + x]) == op[-2]:
						false_var+=1
					else:
						temp.append((start_piece[0] + x, start_piece[1] + x))

			if i[-1] == 2:
				start_piece = min(move_interpreter.move_conv(i[0]),move_interpreter.move_conv(i[1]))
				rnge = abs(move_interpreter.move_conv(i[0])[0] - move_interpreter.move_conv(i[1])[0])
				#print(start_piece, rnge)
				for x in range(1,rnge):
					if (game_board.gb()[start_piece[0] + x][start_piece[1] - x]) == 0 or (game_board.gb()[start_piece[0] + x][start_piece[1] - x]) == op[-2]:
						false_var+=1
					else:
						temp.append((start_piece[0] + x,start_piece[1] - x))

			if i[-1] == 3:
				start_piece = min(move_interpreter.move_conv(i[0]),move_interpreter.move_conv(i[1]))
				rnge = abs(move_interpreter.move_conv(i[0])[1] - move_interpreter.move_conv(i[1])[1])
				for x in range(1,rnge):
					if (game_board.gb()[start_piece[0]][start_piece[1] + x]) == 0 or (game_board.gb()[start_piece[0]][start_piece[1] + x]) == op[-2]:
						false_var+=1
					else:
						temp.append((start_piece[0], start_piece[1] + x))	

			if i[-1] == 4:
				start_piece = min(move_interpreter.move_conv(i[0]),move_interpreter.move_conv(i[1]))
				rnge = abs(move_interpreter.move_conv(i[0])[0] - move_interpreter.move_conv(i[1])[0])
				for x in range(1,rnge):
					if (game_board.gb()[start_piece[0] + x][start_piece[1]]) == 0 or (game_board.gb()[start_piece[0] + x][start_piece[1]]) == op[-2]:
						false_var+=1
					else:
						temp.append((start_piece[0] + x, start_piece[1]))
			if bool(false_var) == False:
				temp = list(dict.fromkeys(temp))
				final.append(temp)
		if final:
			return final

	else:
		return False

def r_val(player, move):
	return in_bw_pieces(valid_move.r_val(player, move))