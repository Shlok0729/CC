def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens(row, n, board, found):
    if row == n:
        print("One solution:")
        for i in range(n):
            line = ['.'] * n
            line[board[i]] = 'Q'
            print(" ".join(line))
        print()
        found[0] = True  # Mark that at least one solution was found
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(row + 1, n, board, found)
            board[row] = -1  # Backtrack

# --- MAIN CODE ---
n = int(input("Enter the size of the board (n): "))
board = [-1] * n
found = [False]  # Using a mutable list to track if any solution was found
solve_n_queens(0, n, board, found)

if not found[0]:
    print("No solution exists.")
