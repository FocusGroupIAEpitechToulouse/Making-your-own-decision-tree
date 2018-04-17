#!/usr/bin/python3

import pygame
import random
import time

from config import NB_SQUARES

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
