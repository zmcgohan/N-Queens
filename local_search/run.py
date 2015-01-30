import sys
import solvers
from time import clock

SOLVER_KEYS = {
		'r': "HillClimbingRandomRestartSolver",
	}

if __name__ == '__main__':
	# make sure a number of queens to place was passed in
	if len(sys.argv) < 2:
		print "This program requires a number of queens to place as an argument."
		print "Example: python run.py 8 r"
		print "^ Would solve a board for 8 placed queens with random restart hill climbing solver"
		sys.exit(1)
	try:
		num_queens = int(sys.argv[1])
	except ValueError:
		print "Invalid value passed in."
	# make sure all solvers passed in are real, if they are
	solvers_to_use = []
	if len(sys.argv) == 3:
		lowercase_arg = sys.argv[2].lower()
		for c in lowercase_arg:
			if not c in SOLVER_KEYS:
				print "{} is not a valid solver key.".format(c)
				sys.exit(1)
			solvers_to_use.append(getattr(solvers, SOLVER_KEYS[c])(num_queens))
	else:
		for key in SOLVER_KEYS:
			solvers_to_use.append(getattr(solvers, SOLVER_KEYS[key])(num_queens))
	for solver in solvers_to_use:
		print "Finding solution with {}...".format(solver.__class__.__name__)
		start_time = clock()
		solver.solve()
		print "Solution found in {} seconds:".format(clock() - start_time)
		solver.print_solution()
