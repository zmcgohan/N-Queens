"""Different methods of finding correct queen placement for n-queen problems."""

import time
import copy

class Placer(object):
	"""Parent abstract class of all Placer classes."""
	def __init__(self, board, num_queens):
		"""Creates Placer with board given."""
		self.board = board
		self.num_queens = num_queens
	def start_timer(self):
		"""Starts a timer to time execution of Placers."""
		print "Placing {0} queens on a {1}x{1} board with {2}...".format(self.num_queens, len(self.board.spots), self.__class__.__name__)
		self.start_time = time.clock()
	def stop_timer(self):
		"""Ends the timer and returns the elapsed time of execution."""
		self.time_taken = time.clock() - self.start_time
		print "{} took {} seconds.".format(self.__class__.__name__, self.time_taken)
	def spot_has_collision(self, row, col):
		"""Checks if a spot on the board would allow a queen placed there to attack any other queens currently placed.

		Return True if a collision could occur, False if not."""
		# check vertically and horizontally
		for i in xrange(len(self.board.spots)):
			if self.board.spots[i][col]: return True
			if self.board.spots[row][i]: return True
		# check diagonals
		is_in_upper = (row-col) < 0
		num_checks = len(self.board.spots) - abs(row-col)
		r = row-col if not is_in_upper else 0
		c = col-row if is_in_upper else 0
		for i in xrange(num_checks):
			if self.board.spots[r+i][c+i]:
				return True
		for i in xrange(len(self.board.spots)):
			if row+i <= len(self.board.spots)-1 and col-i >= 0 and self.board.spots[row+i][col-i]:
				return True
			if row-i >= 0 and col+i <= len(self.board.spots)-1 and self.board.spots[row-i][col+i]:
				return True
		return False

class IncrementalPlacer(Placer):
	"""Parent abstract class to all incremental queen placer methods."""
	def __init__(self, board, num_queens):
		super(IncrementalPlacer, self).__init__(board, num_queens)
		self.boards_tried = 1
	def place_queens(self):
		self.start_timer()
		while self.board.queens_placed < self.num_queens:
			if not self.place_next_queen():
				self.boards_tried += 1
				self.board.clear()
				if self.boards_tried % 100 == 0:
					print "Boards tried: {}; Time: {} seconds".format(self.boards_tried, time.clock() - self.start_time)
		self.stop_timer()
		print "Total boards created: {}".format(self.boards_tried)
	def place_next_queen(self):
		"""To be implemented by child classes. Returns True if a queen was able to be placed on current board. If False, queen was unable to be placed."""
		pass

class GreedyIncrementalPlacer(IncrementalPlacer):
	"""Goes through ALL options of placing queens to find a correct solution."""
	def __init__(self, board, num_queens):
		"""Creates self with the chess board given."""
		super(GreedyIncrementalPlacer, self).__init__(board, num_queens)
		self.past_boards = []
	def place_next_queen(self):
		for i in xrange(len(self.board.spots)):
			for j in xrange(len(self.board.spots)):
				if not self.would_create_past_board(i, j) and not self.spot_has_collision(i, j):
					self.board.place_queen(i, j)
					return True
		self.past_boards.append(self.board.hashcode())
		return False
	def would_create_past_board(self, row, col):
		"""Checks if a queen placed at row, col would make a board already created."""
		if not self.board.spots[row][col]:
			self.board.spots[row][col] = True
			new_board_hashcode = self.board.hashcode()
			self.board.spots[row][col] = False
		else:
			new_board_hashcode = self.board.hashcode()
		for board in self.past_boards:
			if new_board_hashcode == board: return True
		return False

class LeftmostIncrementalPlacer(Placer):
	"""Places 1 queen in each column, starting with the leftmost column. It starts at the top of each column and goes down through all of the possible states."""
	def __init__(self, board, num_queens):
		super(LeftmostIncrementalPlacer, self).__init__(board, num_queens)
		self.cycles = 1
	def place_queens(self):
		queens_placed = 0
		self.start_timer()
		while queens_placed < self.num_queens:
			pass
		self.stop_timer()
		print "Total boards created: {}".format(self.cycles)
