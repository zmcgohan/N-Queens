"""Represents a board to place queens on."""

class Board:
	"""Represents a chess board with the dimensions width x width.
	
	The board is represented as a multi-dimensional array with Falses as empty spaces and Trues as queens."""
	def __init__(self, width):
		"""Initializes board with dimensions width x width."""
		self.spots = [[False for x in xrange(width)] for x in xrange(width)] 
		self.queens_placed = 0
	def __str__(self):
		return '\n'.join([' '.join(['T' if s else 'F' for s in li]) for li in self.spots])
	def __eq__(self, board2):
		return self.spots == board2.spots
	def clear(self):
		for i in xrange(len(self.spots)):
			for j in xrange(len(self.spots[0])):
				self.spots[i][j] = False
		self.queens_placed = 0
	def place_queen(self, row, col):
		"""Places a queen on the board and increments self.queens_placed."""
		self.spots[row][col] = True
		self.queens_placed += 1
	def hashcode(self):
		hashcode = ""
		blanks_since_queen = 0
		for row in self.spots:
			for spot in row:
				if not spot:
					blanks_since_queen += 1
				else:
					hashcode += '{}-'.format(blanks_since_queen)
					blanks_since_queen = 0
		hashcode += '{}'.format(blanks_since_queen)
		return hashcode
