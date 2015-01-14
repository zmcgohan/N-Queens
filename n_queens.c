#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define EMPTY 0
#define ATTACKED 1
#define QUEEN 2

/* Prints the board to standard output. */
void print_board(int** board, int board_size) {
	char spot_repr[] = { '.', '+', '8' };
	int i;
	for(i = 0; i < board_size; ++i) {
		int j;
		for(j = 0; j < board_size; ++j) {
			printf("%c ", spot_repr[board[i][j]]);
		}
		printf("\n");
	}
}

/* Checks if a queen placed in a spot will collide with another placed queen's path. */
int spot_has_collision(int** board, int board_size, int row, int col) {
	return !(board[row][col] == EMPTY);
}

/* Places a queen at board[row][col] and marks all collision spots. */
void place_queen(int** board, int board_size, int row, int col) {
	int i;
	board[row][col] = QUEEN;
	for(i = 0; i < board_size; ++i) {
		if(row != i)
			board[i][col] = ATTACKED;
		if(col != i)
			board[row][i] = ATTACKED;
	}
	// check top-left->bottom->right
	for(i = 1; row + i < board_size && col + i < board_size; ++i) {
		board[row+i][col+i] = ATTACKED;
	}
	for(i = 1; row - i >= 0 && col - i >= 0; ++i) {
		board[row-i][col-i] = ATTACKED;
	}
	// check bottom-left->top-right
	for(i = 1; row+i < board_size && col-i >= 0; ++i) {
		board[row+i][col-i] = ATTACKED;
	}
	for(i = 1; row-i >= 0 && col+i < board_size; ++i) {
		board[row-i][col+i] = ATTACKED;
	}
}

/* Removes a queen from board and revises the attacked spots on board. */
void remove_queen(int** board, int board_size, int row, int col) {
	int placed_queens[board_size];
	int i;
	for(i = 0; i < board_size; ++i) placed_queens[i] = -1;
	int cur_col, cur_row;
	for(cur_col = 0; cur_col < board_size; ++cur_col) {
		for(cur_row = 0; cur_row < board_size; ++cur_row) {
			// get each placed queen's pos
			if(board[cur_row][cur_col] == QUEEN)
				placed_queens[cur_col] = cur_row;
			// reset board
			board[cur_row][cur_col] = EMPTY;
		}
	}
	// replace queens
	for(cur_col = 0; cur_col < board_size; ++cur_col) {
		if(cur_col != col && placed_queens[cur_col] != -1)
			place_queen(board, board_size, placed_queens[cur_col], cur_col);
	}
}

void set_board(int** board, int board_size) {
	int board_positions[board_size];
	int i;
	for(i = 0; i < board_size; ++i) board_positions[i] = 0;
	int cur_col = 0;
	while(cur_col < board_size && cur_col >= 0) {
		if(board_positions[cur_col] < board_size && !spot_has_collision(board, board_size, board_positions[cur_col], cur_col)) {
			place_queen(board, board_size, board_positions[cur_col], cur_col);
			cur_col++;
		} else if(board_positions[cur_col] < board_size - 1) {
			board_positions[cur_col]++;
		} else {
			board_positions[cur_col] = 0;
			cur_col--;
			remove_queen(board, board_size, board_positions[cur_col], cur_col);
			board_positions[cur_col]++;
		}
	}
}

int main(int argc, char** argv) {
	if(argc < 2) {
		printf("Invalid number of arguments.");
		return 1;
	}

	int num_queens = atoi(argv[1]);

	int** board = malloc(sizeof(int*) * num_queens);
	int i;
	for(i = 0; i < num_queens; ++i) {
		board[i] = malloc(sizeof(int) * num_queens);
	}

	clock_t start_clocks = clock();
	set_board(board, num_queens);
	printf("Total time elapsed: %fs\n", ((double) clock() - start_clocks) / CLOCKS_PER_SEC);
	print_board(board, num_queens);

	return 0;
}
