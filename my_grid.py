#!/usr/bin/python3

import pygame
import random
import time

from my_ia import *
from config import *
from my_solution_ia import ia_turn_solution

#init window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("TIC TAC TOE AI")
screen.fill(BLACK)

#sets the whole grid with '0'
#	[['0']['0']['0']
#	 ['0']['0']['0']
#	 ['0']['0']['0']]
def fill_grid(grid):
	for line in range(NB_SQUARES):
		grid.append([])
		for column in range(NB_SQUARES):
			grid[line].append('0')
	return (grid)

grid = []
grid = fill_grid(grid)

#get the coresponding index of the grid from mouse pos
#	returns a number between 0 and (NB_SQUARES - 1) for x and y
def find_coords(pos):
	x = 0
	y = 0
	nbr = WIDTH + MARGIN + 5
	while (nbr < pos[0]):
		nbr += (WIDTH + MARGIN)
		x += 1
	nbr = HEIGHT + MARGIN + 50
	while (nbr < pos[1]):
		nbr += (HEIGHT + MARGIN)
		y += 1
	return (x, y)

# places the square for the human player and then calls the AI
def place_square(human_player, grid):
	pos = pygame.mouse.get_pos()
	if int(pos[1]) < (WINDOW_HEIGHT - 5 - MARGIN) and int(pos[1]) > 55 and int(pos[0]) > 5 and int(pos[0]) < (WINDOW_WIDTH - 5 - MARGIN):
		rect_x, rect_y = find_coords(pos)
		win = 0
		if human_player and grid[rect_y][rect_x] == '0':
			grid[rect_y][rect_x] = '3';
			human_player = False
			win = check_win()
			if win != 0:
				print(win)
				print("One player as made a row of " + str(VICTORY_ROW))
				pygame.quit()
				exit(0)
			# AI CALLED HERE, returns the grid
			grid = ia_turn(grid)
			human_player = True
			win = check_win()
			if win != 0:
				print(win)
				print("One player as made a row of " + str(VICTORY_ROW))
				pygame.quit()
				exit(0)
	return (human_player)

#check if there is any enpty squares left on the grid else exit
def check_if_draw(grid):
	for i in range(NB_SQUARES):
		for k in range(NB_SQUARES):
			if (grid[i][k] == '0'):
				return (1)
	print("Draw")
	pygame.quit()
	exit(0)

#checks for each instances if true, if true then one player wins
#	format it checks [[2, 2, 2], [3,2,0]]
def check_if_equal(res):
	for i in range(len(res)):
		if i != 0 and res[i - 1] != res[i]:
			return (0)
	return (res[0])

#checks four lines, digonal, top, left and bottom
#then calls check_if_equal() to check if one of the four lines is true
#if true one player wins
def check_win():
	for line in range(NB_SQUARES):
		for column in range(NB_SQUARES):
			res = [[], [], [], []]
			for i in range(VICTORY_ROW):
				if i + line < NB_SQUARES and i + column < NB_SQUARES:
					res[0].append(int(grid[line + i][column + i]))
				if i + line < NB_SQUARES:
					res[1].append(int(grid[line + i][column]))
				if i + column < NB_SQUARES:
					res[2].append(int(grid[line][column + i]))
				if line - i >= 0 and i + column < NB_SQUARES:
					res[3].append(int(grid[line - i][column + i]))
			for i in range(4):
				winner = 0
				if len(res[i]) == VICTORY_ROW:
					winner = check_if_equal(res[i])
				if winner != 0:
					return (winner)
	return (0)

#draw the red lines surrounding the tic tac toe game
pygame.draw.rect(screen, DARK_RED, pygame.Rect(0, 50, 5, (WINDOW_HEIGHT - 50)))
pygame.draw.rect(screen, DARK_RED, pygame.Rect((WINDOW_WIDTH - 5), 50, 5, (WINDOW_HEIGHT - 50)))
pygame.draw.rect(screen, DARK_RED, pygame.Rect(0, 50, WINDOW_WIDTH, 5))
pygame.draw.rect(screen, DARK_RED, pygame.Rect(0, (WINDOW_HEIGHT - 5), WINDOW_WIDTH, 5))

#main loop 
human_player = True
running = True
while running:
	#get mouse event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
	if pressed1:
		#place human player square as well as calling ai
		human_player = place_square(human_player, grid)
		check_if_draw(grid)
	#display corresponding colour for each squares
	for column in range(NB_SQUARES):
		for line in range(NB_SQUARES):
			if (grid[line][column] == '0'):
				pygame.draw.rect(screen, LIGHT_GREY, pygame.Rect(5 + (column * (WIDTH + MARGIN)), (5 + 50) + (line * (WIDTH + MARGIN)), WIDTH, HEIGHT))
			elif (grid[line][column] == '2'):
				pygame.draw.rect(screen, LIGHT_YELLOW, pygame.Rect(5 + (column * (WIDTH + MARGIN)), (5 + 50) + (line * (WIDTH + MARGIN)), WIDTH, HEIGHT))
			else:
				pygame.draw.rect(screen, ROYAL_BLUE, pygame.Rect(5 + (column * (WIDTH + MARGIN)), (5 + 50) + (line * (WIDTH + MARGIN)), WIDTH, HEIGHT))
	#limits at 60 frames per seconds
	pygame.time.Clock().tick(60)
	pygame.display.flip()

pygame.quit()