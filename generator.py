"""Generates a 9x9 Sudoku puzzle
"""

from solver import solve
from copy import deepcopy
from random import sample

# generates a solved puzzle
def solution():
    board = [[' ' for i in range(9)] for j in range(9)]
    solve(board)
    return board

# generates a puzzle to be solved
def puzzleMaker():
    sol = solution()
    puzzle = deepcopy(sol)

    # randomly replace cells with 0
    # puzzles must have at least 17 clues to have a valid solution
    # easy: erases 20 to 34 clues
    # medium: erases 35 to 49 clues
    # hard: erases 50 to 64 clues
    # if difficulty == 'easy':
    #     for i in sample(range(81), sample(range(20,34),1)[0]):
    #         puzzle[i//9][i%9] = ' '
    # elif difficulty == 'medium':
    #     for i in sample(range(81), sample(range(35,49),1)[0]):
    #         puzzle[i//9][i%9] = ' '
    # elif difficulty == 'hard':
    #     for i in sample(range(81), sample(range(20,34),1)[0]):
    #         puzzle[i//9][i%9] = ' '
    for i in sample(range(81), sample(range(17,31),1)[0]):
        puzzle[i//9][i%9] = ' '

    return puzzle, sol

# formats puzzle into user-friendly format
def printBoard(puzzle):
    print("-----------------------")

    for i in range(len(puzzle)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(puzzle[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end="")
    
    print("-----------------------")

# def format(puzzle):
#     print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
    
#     for b in range(len(puzzle)):
#         if b % 3 == 0 and b != 0:
#             print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
#         if b in [1, 2, 4, 5, 7, 8]:
#             print('╟───┼───┼───╫───┼───┼───╫───┼───┼───╢')
#         for c in range(len(puzzle[0])):
#             if c % 3 == 0:
#                 print("║ ", end = "")
#             if c in [1, 2, 4, 5, 7, 8] and c != 0:
#                 print('│ ', end = '')
#             if c == 8:
#                 print(str(puzzle[b][c]) + " ║")
#             else:
#                 print(str(puzzle[b][c]) + " ", end = '')
                
    
#     print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")

# if __name__ == "__main__":
#     printBoard(solution())
#     printBoard(puzzleMaker("easy"))