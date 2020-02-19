import numpy as np
import pygame
import game_board
import move_interpreter
import move
import valid_move_2
import UI_Logic
import os

pygame.init()

black = (0,0,0)
white = (255, 255, 255)
board_colour = (34, 34, 34)
button_bright = (50,50,50)
display_length = 1000
display_breadth = 700
green = pygame.Color('#00b16c')
red = pygame.Color('#ff001a')
yellow = pygame.Color('#d8d700')

const_x = (display_length * 0.2)//1
const_y = (display_breadth * 0.075)//1

gameDisplay = pygame.display.set_mode((display_length, display_breadth))
pygame.display.set_caption('Othello')
clock = pygame.time.Clock()  # for FPS	
board_display = pygame.image.load(os.path.join("pictures", "Board_Image.png"))
white_piece = pygame.image.load(os.path.join("pictures", "White_Piece.png"))  
black_piece = pygame.image.load(os.path.join("pictures", "Black_Piece.png"))
valid_piece = pygame.image.load(os.path.join("pictures", "Valid_Move.png"))
last_piece = pygame.image.load(os.path.join("pictures", "Last_Move_2.png"))
black_score = pygame.image.load(os.path.join("pictures", "Black_display.png"))
white_score = pygame.image.load(os.path.join("pictures", "White_display.png"))

def quitgame():
	pygame.quit()
	quit()
def restart():
	game_board.board = game_board.game_board(8)	
	game_board.black_index = ['D4', 'E5']
	game_board.white_index = ['D5', 'E4']

def restart_game():
	restart()
	game_loop()

def game_intro():
	restart()
	game_board.game_board(8)
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(board_colour)
		UI_Logic.message_display('Othello', display_length//2, display_breadth//2 - 100, 150, white)
		UI_Logic.message_display('by Anirudh S. Kumar (11D) ', display_length//2, display_breadth//2, 35, white)
		UI_Logic.button('Play', 225, 450, 150, 75, 65, green, game_loop)
		UI_Logic.button('Quit', 625, 450, 150, 75, 65, red, quitgame)

		pygame.display.update()
		clock.tick(60)

def game_loop():
	x = display_length * 0.2
	y = display_breadth * 0.075//1
	turns = 0
	crashed = False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
		gameDisplay.fill(board_colour)
		UI_Logic.boardImg(x,y)
		UI_Logic.Logic()
		UI_Logic.black_score(65,70)
		UI_Logic.white_score(865,70)
		UI_Logic.button('Restart',40, 500, 125, 50, 40, yellow, restart_game)
		UI_Logic.button('Exit', 840, 500, 125, 50, 40, red, game_intro)

		if UI_Logic.valid_moves_rval(turns):
			UI_Logic.valid_moves_display(UI_Logic.valid_moves_rval(turns))
		else:
			if turns < 60:
				turns+=1
		if pygame.mouse.get_pressed()[0]:
			p,q = pygame.mouse.get_pos()
			p = (p-200)//75
			q = (q-52)//75
			if (p,q) in UI_Logic.valid_moves_rval(turns):
				UI_Logic.move_display((p,q),turns)
				print(turns)
				game_board.board_view()
				if turns%2 == 0:
					move.play_move(2,move_interpreter.rev_move_conv((q,p)))
					
				else:
					move.play_move(1,move_interpreter.rev_move_conv((q,p)))
				turns+=1
				game_board.board_view()
				pygame.display.update()
				clock.tick(60)
		UI_Logic.score_display()
		if turns < 60:
			UI_Logic.turn_display(turns)
		elif turns == 60:
			UI_Logic.win_display()
			UI_Logic.button('Play again', display_length//2-135, display_breadth//2+40, 125, 50, 30, green, restart_game)
			UI_Logic.button('Quit', display_length//2+ 10, display_breadth//2+40, 125, 50, 40, red, quitgame)
		pygame.display.update()
		clock.tick(60)
	pygame.quit()
	quit()

game_intro()
pygame.quit()
quit()