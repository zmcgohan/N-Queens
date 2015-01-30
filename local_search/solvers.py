from random import randint, choice

class HillClimbingRandomRestartSolver:
	MAX_SIDE_STEPS = 30
	def __init__(self, num_queens):
		self.num_queens = num_queens
		self.set_new_board()
	def set_new_board(self):
		self.board = [randint(0,self.num_queens-1) for i in xrange(self.num_queens)]
		self.side_steps = 0 # number of cycles the least heuristic value hasn't changed
		self.last_heuristic_value = self.get_num_attacks(self.board)
	def print_board(self, board):
		for i in xrange(len(board)):
			for j in xrange(len(board)):
				if (len(board)-i) - 1 - board[j] == 0:
					print "Q",
				else:
					print ".",
			print
		print "Heuristic value: {}".format(self.get_num_attacks(board))
	def print_solution(self):
		for i in xrange(len(self.board)):
			for j in xrange(len(self.board)):
				if (len(self.board)-i) - 1 - self.board[j] == 0:
					print "Q",
				else:
					print ".",
			print
	def get_num_attacks(self, board):
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
		if move[1] == self.board[move[0]]: 
			return self.last_heuristic_value
		move_heuristic = self.last_heuristic_value
		cur_queen_row = self.board[move[0]]
		for i in xrange(self.num_queens):
			if self.board[i] == cur_queen_row and i != move[0]:
				move_heuristic -= 1
			elif self.board[i] == (i-move[0])+cur_queen_row and i != move[0]:
				move_heuristic -= 1
			elif self.board[i] == -(i-move[0])+cur_queen_row and i != move[0]:
				move_heuristic -= 1
			if self.board[i] == move[1] and i != move[0]:
				move_heuristic += 1
			elif self.board[i] == (i-move[0])+move[1] and i != move[0]:
				move_heuristic += 1
			elif self.board[i] == -(i-move[0])+move[1] and i != move[0]:
				move_heuristic += 1
		return move_heuristic
	def make_next_move(self):
		# get heuristic values of all possible movement places
		best_heuristic_value = self.last_heuristic_value
		best_moves = [ (0, self.board[0]) ]
		for i in xrange(len(self.board)):
			#orig_position = self.board[i]
			for j in xrange(len(self.board)):
				if j != self.board[i]:
				#if j != orig_position:
					#self.board[i] = j
					#cur_heuristic = self.get_num_attacks(self.board)
					cur_heuristic = self.get_move_heuristic((i, j))
					if cur_heuristic < best_heuristic_value:
						best_heuristic_value = cur_heuristic
						best_moves = [(i, j)]
					elif cur_heuristic == best_heuristic_value:
						best_moves.append((i, j))
			#self.board[i] = orig_position
		if best_heuristic_value == self.last_heuristic_value:
			self.side_steps += 1
		selected_move = choice(best_moves)
		self.board[selected_move[0]] = selected_move[1]
		self.last_heuristic_value = best_heuristic_value
	def solve(self):
		"""Call make_next_move() until a solution is found or self.side_steps >= MAX_SIDE_STEPS."""
		while self.last_heuristic_value > 0:
			if self.side_steps >= HillClimbingRandomRestartSolver.MAX_SIDE_STEPS:
				print "Failed to find solution. Trying new board..."
				self.set_new_board()
			self.make_next_move()
