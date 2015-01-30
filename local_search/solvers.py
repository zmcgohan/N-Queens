from random import randint, choice

class HillClimbingRandomRestartSolver:
	MAX_SIDE_STEPS = 30 # max number of cycles the solver will go through where the heuristic value doesn't go down
	def __init__(self, num_queens):
		self.num_queens = num_queens
		self.set_new_board()
	def set_new_board(self):
		"""Sets up a new board and resets all relevant variables."""
		self.board = [randint(0,self.num_queens-1) for i in xrange(self.num_queens)]
		self.side_steps = 0 # number of cycles the least heuristic value hasn't changed
		self.last_heuristic_value = self.get_num_attacks(self.board)
	def print_board(self, board):
		"""Prints a visual representation for board."""
		for i in xrange(len(board)):
			for j in xrange(len(board)):
				if (len(board)-i) - 1 - board[j] == 0:
					print "Q",
				else:
					print ".",
			print
	def get_num_attacks(self, board):
		"""Returns the total number of pairs of queens that can attack each other in board.
		
		NOTE: As is, VERY inefficient."""
		num_attacks = 0
		# iterate through all queens
		for i in xrange(len(board)):
			queen_row = board[i]
			# compare against other queens
			for j in xrange(len(board)):
				if board[j] == queen_row and i != j:
					num_attacks += 1
				if board[j] == (j-i)+queen_row and i != j:
					num_attacks += 1
				if board[j] == -(j-i)+queen_row and i != j:
					num_attacks += 1
		return num_attacks / 2
	def get_move_heuristic(self, move):
		"""Returns the heuristic value of a modified board, created through move.

		move = tuple with [0] as col to change, [1] as new col value"""
		if move[1] == self.board[move[0]]: # return current heuristic value if move doesn't change anything
			return self.last_heuristic_value
		move_heuristic = self.last_heuristic_value
		cur_queen_row = self.board[move[0]]
		for i in xrange(self.num_queens):
			# remove collisions from current queen position
			if self.board[i] == cur_queen_row and i != move[0]: # horizontal
				move_heuristic -= 1
			elif self.board[i] == (i-move[0])+cur_queen_row and i != move[0]: # diagonal, left-bottom->top-right
				move_heuristic -= 1
			elif self.board[i] == -(i-move[0])+cur_queen_row and i != move[0]: # diagonal, top-left->bottom-right
				move_heuristic -= 1
			# add collisions for new queen position
			if self.board[i] == move[1] and i != move[0]: # horizontal
				move_heuristic += 1
			elif self.board[i] == (i-move[0])+move[1] and i != move[0]: # diagonal, left-bottom->top-right
				move_heuristic += 1
			elif self.board[i] == -(i-move[0])+move[1] and i != move[0]: # diagonal, top-left->bottom-right
				move_heuristic += 1
		return move_heuristic
	def make_next_move(self):
		"""Changes board to new board with lowest heuristic value found in current configuration; if no lower heuristic value found, chooses random board from heuristic values of equal value."""
		# get heuristic values of all possible movement places
		best_heuristic_value = self.last_heuristic_value
		best_moves = [ (0, self.board[0]) ] # holds all next configurations with equal heuristic values
		# iterate through all spots on board to find lowest next heuristic value
		for i in xrange(len(self.board)):
			for j in xrange(len(self.board)):
				if j != self.board[i]:
					cur_heuristic = self.get_move_heuristic((i, j))
					if cur_heuristic < best_heuristic_value:
						best_heuristic_value = cur_heuristic
						best_moves = [(i, j)]
					elif cur_heuristic == best_heuristic_value:
						best_moves.append((i, j))
		if best_heuristic_value == self.last_heuristic_value: # if no lower heuristic found, increment self.side_steps
			self.side_steps += 1
		# select next configuration randomly from equal heuristic values
		selected_move = choice(best_moves)
		self.board[selected_move[0]] = selected_move[1]
		self.last_heuristic_value = best_heuristic_value
	def solve(self):
		"""Call make_next_move() until a solution is found or self.side_steps >= MAX_SIDE_STEPS."""
		while self.last_heuristic_value > 0:
			# if at the limit for side steps, start a new board
			if self.side_steps >= HillClimbingRandomRestartSolver.MAX_SIDE_STEPS:
				print "Failed to find solution. Trying new board..."
				self.set_new_board()
			self.make_next_move()
