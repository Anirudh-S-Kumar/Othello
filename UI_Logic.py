import pygame
import game_board
import move_interpreter
import move
import valid_move_2
import valid_move
import os

black = (0,0,0)
white = (255, 255, 255)
board_colour = (34, 34, 34)
button_bright = (50,50,50)
display_length = 1000
display_breadth = 700

const_x = (display_length * 0.2)//1
const_y = (display_breadth * 0.075)//1
gameDisplay = pygame.display.set_mode((display_length, display_breadth))
board_display = pygame.image.load(os.path.join("pictures", "Board_Image.png"))
white_piece = pygame.image.load(os.path.join("pictures", "White_Piece.png"))  
black_piece = pygame.image.load(os.path.join("pictures", "Black_Piece.png"))
valid_piece = pygame.image.load(os.path.join("pictures", "Valid_Move.png"))
last_piece = pygame.image.load(os.path.join("pictures", "Last_Move_2.png"))
black_score_ = pygame.image.load(os.path.join("pictures", "Black_display.png"))
white_score_ = pygame.image.load(os.path.join("pictures", "White_display.png"))

def valid_place(x,y):
	gameDisplay.blit(valid_piece, (x,y))
def boardImg(x,y):
	gameDisplay.blit(board_display, (x,y))
def place_white(x,y):
	gameDisplay.blit(white_piece, (x,y))
def place_black(x,y):
	gameDisplay.blit(black_piece, (x,y))
def last_move(x,y):
	gameDisplay.blit(last_piece, (x,y))
def black_score(x,y):
	gameDisplay.blit(black_score_, (x,y))
def white_score(x,y):
	gameDisplay.blit(white_score_, (x,y))

def box(colour, dimensions):
	pygame.draw.rect(gameDisplay, colour, dimensions)
	pygame.draw.rect(gameDisplay, white, (dimensions[0]-1, dimensions[1]-1, dimensions[2], dimensions[3]), 3)

def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

def message_display(text, x, y, size, color):
	largeText = pygame.font.Font('BebasNeue-Regular.ttf',size)
	TextSurf, TextRect = text_objects(text, largeText, color)
	TextRect.center = (x,y)
	gameDisplay.blit(TextSurf,TextRect)

def button(message, x, y, length, breadth, size, a_c, action):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()[0]
	if x+length > mouse[0] > x and y+breadth > mouse[1] > y:
		box(button_bright, (x, y, length, breadth))
		message_display(message, x+length//2, y+breadth//2+1, size, a_c)
		if click and action != False:
			action()
	else:
		box(board_colour, (x, y, length, breadth))
		message_display(message, x+length//2, y+breadth//2+1, size, white)

def Logic():
	for i in range(8):
		for j in range(8):
			if game_board.gb()[i][j] == 1:
				place_white(const_x + 75*j, const_y + 75*i )
			elif game_board.gb()[i][j] == 2:
				place_black(const_x + 75*j, const_y + 75*i )
			else:
				continue
def valid_moves_rval(turns):
	r_val = []
	for i in range(8):
		for j in range(8):
			if turns%2 == 0:
				if bool(valid_move_2.r_val(2,move_interpreter.rev_move_conv((i,j)))) is True:
					r_val.append((j,i))
			else:
				if bool(valid_move_2.r_val(1,move_interpreter.rev_move_conv((i,j)))) is True:
					r_val.append((j,i))
	return r_val

def valid_moves_display(r_val):
	for i in r_val:
		x,y = i
		valid_place(const_x + 75 * x,const_y + 75 * y)

def move_display(co_ord, turns):
	x,y = co_ord
	x,y = (x - const_x)//75, (y-const_y)//75
	temp = (x,y)
	if temp in valid_moves_rval(turns):
		if turns%2 == 0:
			move.play_move(2, move_interpreter.rev_move_conv(temp))
		else:
			move.play_move(1, move_interpreter.rev_move_conv(temp))

def win_logic():
	d_white = 0
	d_black = 0
	for i in game_board.gb():
		for j in i:
			if j == 1:
				d_white+=1
			elif j == 2:
				d_black+=1
	
	if d_white+d_black == 64:
		return d_black, d_white
	else:
		return d_black, d_white

def score_display():
	if win_logic():
		a,b = win_logic()
		message_display(str(a), 95, 150, 30, white)
		message_display(str(b), 895,150, 30, white)

def win_display():
	pygame.draw.rect(gameDisplay, board_colour, [276, 259, 450, 200])
	pygame.draw.rect(gameDisplay, white, [274, 257, 450, 200],5)
	x,y = win_logic()
	if x > y:
		message_display('Black Won!!', display_length/2, display_breadth/2-20, 75, white)
	elif x < y:
		message_display('White Won!!', display_length/2, display_breadth/2-20, 75, white)
	elif x == y:
		message_display('Draw', display_length/2, display_breadth/2-20, 75, white)

def turn_display(turns):
	if turns%2 == 0:
		message_display("Black's Turn" , display_length/2, 30, 30, white)
	else:
		message_display("White's Turn" , display_length/2, 30, 30, white)