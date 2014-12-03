"""Represents a board to place queens on."""

class Board:
	"""Represents a chess board with the dimensions width x width.
	
	The board is represented as a multi-dimensional array with Falses as empty spaces and Trues as queens."""
	def __init__(self, width):
		"""Initializes board with dimensions width x width."""
		self.spots = [[False for x in xrange(width)] for x in xrange(width)] 
	def __str__(self):
		return '\n'.join([' '.join(['T' if s else 'F' for s in li]) for li in self.spots])
	def __eq__(self, board2):
		return self.spots == board2.spots
	def clear(self):
		for i in xrange(len(self.spots)):
			for j in xrange(len(self.spots[0])):
				self.spots[i][j] = 0
