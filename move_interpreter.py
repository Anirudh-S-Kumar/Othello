'''
Simple function to convert the input by the user to x,y coordinates of the array
'''
move_key   =   {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
move_key_rev = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G', 7 : 'H'}

def move_conv(co_ord):  # converting co-ordinated given by the user to x,y indices for array
	if len(co_ord) > 2 or type(co_ord) != type('a'):
		return False
	co_ord = co_ord.upper()
	return int(co_ord[1])-1,move_key[co_ord[0]]

def rev_move_conv(co_ord):
	x,y = co_ord
	return str(move_key_rev[y]) + str(x+1)