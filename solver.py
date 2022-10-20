"""Sudoku solver using the backtracking algorithm.

"""

from random import sample

# def print_board(board):
#     for i in range(len(board)):
#         if i % 3 == 0 and i != 0:
#             print("- - - - - - - - - - - -")
#         for j in range(len(board[0])):
#             if j % 3 == 0 and j != 0:
#                 print(" | ", end="")
#             if j == 8:
#                 print(board[i][j])
#             else:
#                 print(str(board[i][j]) + " ", end="")

# checks to see if cell is empty
def isEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                return (i,j) #row, col
    return None

# checks to see if number placement is valid
def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_i = pos[0] // 3
    box_j = pos[1] // 3
    for i in range(box_i*3, box_i*3 + 3):
        for j in range(box_j*3, box_j*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

# uses backtracking to solve puzzle
# def solve(board):
#     find = isEmpty(board)
#     if not find:
#         return True
#     else:
#         row, col = find
    
#     for i in range(1,10):
#         if valid(board, i, (row,col)):
#             board[row][col] = i
#             if solve(board):
#                 return True
#             board[row][col] = 0
#     return False

# uses backtracking to place numbers inside an empty board
def solve(board):
    find = isEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        # 1st element of a list of 1 randomly generated number between 1 and 10
        i = sample(range(1,10),1)[0]
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = ' '
    return False
        

# def main():
    # board = [
    #     [7,8,0,4,0,0,1,2,0],
    #     [6,0,0,0,7,5,0,0,9],
    #     [0,0,0,6,0,1,0,7,8],
    #     [0,0,7,0,4,0,2,6,0],
    #     [0,0,1,0,5,0,9,3,0],
    #     [9,0,4,0,6,0,0,0,5],
    #     [0,7,0,3,0,0,0,1,2],
    #     [1,2,0,0,0,7,4,0,0],
    #     [0,4,9,2,0,6,0,0,7]
    # ]
    # board = [['' for n in range(9)] for m in range(9)]
    # print_board(board)
    # print(board)
    # solve(board)
#     print("--------------------")
    # print_board(board)
    # print(board)

# if __name__ == "__main__":
#     main()