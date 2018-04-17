#!/usr/bin/python3

import pygame
import random
import time

from config import NB_SQUARES, VICTORY_ROW

## GIVEN FUNCTION THAT COULD HELP (NOT MANDATORY TO USE) ##

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
# if return 0 no one wins, if return 100 ai wins, if return -100 player wins
def find_score(grid):
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
				if winner != 0 and winner == 3:
					return (-100)
				elif winner != 0 and winner == 2:
					return (100)
	return (0)

# function that returns the highest score from the score list and its index
def highest_score(score):
	keep = -101
	keep_index = 0
	for i in range(len(score)):
		if score[i] > keep:
			keep = score[i]
			keep_index = i
	return (keep, keep_index)

#main ai function that i call for my solution
#mainly here for structure purposes
def ia_turn_solution(grid):
	score = []
	final_score = 0
	index = 0
	#make a deep copy of the grid so that you can modify it without changing the original one
	sim_grid = copy.deepcopy(grid)
	#function that recursively calls calculates the weight of all the branches, returns a list those weights
	score = get_next_branch(sim_grid, '2')
	#from the score returns the highest weight as well as its index in the score list
	final_score, index = highest_score(score)
	#puts the square of the ai in the original grid
	grid = put_square_on_highest_score(grid, index)
	return (grid)

#----------------------------------#

#chosses first square
def place_first_square(grid):
	for i in range(NB_SQUARES):
		for k in range(NB_SQUARES):
			if (grid[i][k] == '0'):
				grid[i][k] = '2'
				return (grid)

# #	replace this function with your ai	# #
def ia_turn(grid):
	grid = place_first_square(grid)
	return (grid)
