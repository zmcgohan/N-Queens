"""Figures out how to fit n queens on a board of a user-input-given board size without any of them being able to attack each other.

The first command-line argument is the board width, and the second is the number of queens to be placed.

Example: python queens.py 5 2

^ For the above, 2 queens will be placed on a 5x5 board in positions where neither can attack the other."""

import sys

from queen_placement import GreedyIncrementalPlacer
from board import Board

if __name__ == '__main__':
	try:
		board_width = int(sys.argv[1])
		num_queens = int(sys.argv[2])
	except ValueError: 
		print "queens.py must be ran with two arguments, the board width and number of queens.\n\nExample:\npython queens.py 5 2\n^ A 5x5 board would be tested for the positions of 2 queens which could not attack each other."
		exit(1)
	board = Board(board_width)
	greedy_placer = GreedyIncrementalPlacer(board, num_queens)
	greedy_placer.place_queens()
	print board
