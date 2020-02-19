import move_interpreter
import game_board
import math

'''
We are considering the aplhabetical part to be the x - coordinate and 
The numerical part of move to be the y - coordinate

Also considering diagonal where (0,0) and (1,1) are in the diagonal to be diag_1 and 
diagonal where (0,1) and (1,0) to be diag_2

P.S. Due to a slight mistake in my move_convertor module, the co-ordinates got flipped. This is not a small mistake but a 
HUGE mistake.Instead of doing it again with the correct order of coordinates, I modified my logic to this fact that 
co-ordinates are flipped

'''

def line_bw_pieces(player,move):  # determines in what direction will the pieces be flipped
	black_index = game_board.black_index
	white_index = game_board.white_index

	if game_board.gb()[move_interpreter.move_conv(move)[0]][move_interpreter.move_conv(move)[1]] != 0:
		return False
	k = {1 : black_index,2 : white_index}
	multiple = 0  # variable to handle case when there are multiple ways to connect the given move 
	r_value = []  # list which will contain all the possible ways the given move is connected to the other pieces
	move_abscissa = move_interpreter.move_conv(move)[0]  # assigning value of abscissas and ordinate of the two 
	move_ordinate = move_interpreter.move_conv(move)[1]  # coordinates to individual variables for easier manipulation later

	for i in k[player]:
		temp_abscissa = move_interpreter.move_conv(i)[0] 
		temp_ordinate = move_interpreter.move_conv(i)[1]		
		#print(i)
		# Checking whether the pieces are adjacent to each other or not. If they are, the move cannot be valid as there will be no piece in the middle to flip over
		if (move_abscissa == temp_abscissa + 1 or move_abscissa == temp_abscissa - 1 ) or (move_ordinate == temp_ordinate + 1 or move_ordinate == temp_ordinate - 1 ):
			continue
		if math.fabs(move_abscissa - temp_abscissa) == math.fabs(move_ordinate - temp_ordinate): 
			temp = move_interpreter.move_conv(i)
			k = move_interpreter.move_conv(move)
			if (temp[0]>k[0] and temp[1]>k[1]) or (temp[0]<k[0] and temp[1]<k[1]):
				r_value.append((move, i, 1))  # appending 1 for diag_1
				multiple+=1
			else:
				r_value.append((move, i, 2))  
				multiple+=1
		if move_abscissa + move_ordinate == temp_abscissa + temp_ordinate:
			r_value.append((move, i, 2))  # appending 2 for diag_2
			multiple+=1  
		if move_abscissa == temp_abscissa:
			r_value.append((move, i, 3))  # appending 3 for Horizontal
			multiple+=1  
		if move_ordinate == temp_ordinate:
			r_value.append((move, i, 4))  # appending 4 for Vertical
			multiple+=1  
	if r_value:
		r_value = list(dict.fromkeys(r_value))
		return r_value, player, multiple
	else:
		return False	

def r_val(player, move):
	return line_bw_pieces(player,move)


