"""Represents a board to place queens on."""

class Board:
	"""Represents a chess board with the dimensions width x width.
	
	The board is represented as a multi-dimensional array with 0s as empty spaces, 1s as attacked spaces and 2s as queens."""
	def __init__(self, width):
		"""Initializes board with dimensions width x width."""
		self.spots = [[0 for x in xrange(width)] for x in xrange(width)] 
		self.queens_placed = 0
	def __str__(self):
		return '\n'.join([' '.join(['-' if x<2 else 'Q' for x in li]) for li in self.spots])
	def __eq__(self, board2):
		return self.spots == board2.spots
	def clear(self):
		for i in xrange(len(self.spots)):
			for j in xrange(len(self.spots[0])):
				self.spots[i][j] = 0
		self.queens_placed = 0
	def place_queen(self, row, col):
		"""Places a queen on the board and increments self.queens_placed."""
		self.queens_placed += 1
		for i in xrange(len(self.spots)):
			self.spots[row][i] = 1
			self.spots[i][col] = 1
			if row+i < len(self.spots) and col+i < len(self.spots): 
				self.spots[row+i][col+i] = 1
			if row-i >= 0 and col-i >= 0:
				self.spots[row-i][col-i] = 1
			if row-i >= 0 and col+i < len(self.spots):
				self.spots[row-i][col+i] = 1
			if row+i < len(self.spots) and col-i >= 0:
				self.spots[row+i][col-i] = 1
		self.spots[row][col] = 2
	def spot_is_open(self, row, col):
		"""Returns True if a spot is not in the path of another queen and it is free."""
		return self.spots[row][col] == 0
	def hashcode(self):
		hashcode = ""
		blanks_since_queen = 0
		for row in self.spots:
			for spot in row:
				if spot < 2:
					blanks_since_queen += 1
				else:
					hashcode += '{}-'.format(blanks_since_queen)
					blanks_since_queen = 0
		hashcode += '{}'.format(blanks_since_queen)
		return hashcode
