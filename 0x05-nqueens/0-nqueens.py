#!/usr/bin/python3
import sys


def is_safe(queen_positions, row, col):
    for r, c in queen_positions:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve_nqueens(n, row=0, queen_positions=[]):
    if row == n:
        print(queen_positions)
        return
    for col in range(n):
        if is_safe(queen_positions, row, col):
            solve_nqueens(n, row + 1, queen_positions + [[row, col]])


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
