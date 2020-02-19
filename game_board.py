import numpy as np

black_index = ['D4', 'E5']
white_index = ['D5', 'E4']

def game_board(k): # creating the board
	board = np.zeros((k,k))
	board[3][3],board[4][4],board[3][4],board[4][3] = 1,1,2,2
	return board

board = game_board(8)  # initialising the board

def board_view():
	print('    A  B  C  D  E  F  G  H')
	for i in range(len(board)):
		print(i+1, end = '  ')
		print(board[i])

def gb():
	return board

