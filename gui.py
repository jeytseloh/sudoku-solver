"""PyGame GUI for Sudoku
"""

import pygame, sys
from pygame.locals import *
from generator import puzzleMaker

pygame.font.init()
puzzle, sol = puzzleMaker()

font = pygame.font.SysFont("arial", 60)

# window size - multiply of 9
width = 540
height = 540

# extension
ex = 100

# grid and numbers
square = width // 3
cell = square // 3

# colors
color = {
    "bl": [0,0,0],
    "wh": [255,255,255],
    "gr": [200,200,200],
    "re": [255,0,0],
    "input": [0,0,255],
    "sol": [0,255,0],
    "hover": [204,255,229]
}

# draws puzzle numbers
def drawNum(puzzle, sol, solOn, display):
    x = cell // 2
    y = cell // 2
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            num = puzzle[i][j]
            if type(num) == str and num != " " and solOn:
                text = font.render(str(sol[i][j]), True, color["input"])
                display.blit(text, (x-12,y-15))
            elif type(num) == str and num != " ":
                text = font.render(str(num), True, color["input"])
                display.blit(text, (x-12,y-15))
            elif type(num) == int and num != " ":
                text = font.render(str(num), True, color["bl"])
                display.blit(text, (x-12,y-15))
            elif num == " " and solOn:
                text = font.render(str(sol[i][j]), True, color["re"])
                display.blit(text, (x-12,y-15))
            
            x += cell
        x = cell // 2
        y += cell

# draws grid
def drawGrid():
    # box lines
    for i in range(0, width, square): # vertical
        if i != 0:
            pygame.draw.line(display, color["bl"], (i,0), (i,height), 4)
    for j in range(0, height, square): # horizontal
        if j != 0:
            pygame.draw.line(display, color["bl"], (0,j), (width,j), 4)
    
    # cell lines
    for i in range(0, width, cell): # vertical
        if i % square != 0:
            pygame.draw.line(display, color["bl"], (i,0), (i,height), 1)
    for j in range(0, height, cell): # horizontal
        if j % square != 0:
            pygame.draw.line(display, color["bl"], (0,j), (width,j), 1)
    
    # bottom border
    pygame.draw.line(display, color["bl"], (0,height), (width,height), 4)

# check solution button
def checkSol():
    xSol = width // 2 - cell
    ySol = (height + ex) - 77

    xNew = width // 6 - cell
    yNew = ySol

    # draw button
    pygame.draw.rect(display, color["bl"], (xSol, ySol, cell*2, cell), 3)
    text = font.render("Solve", True, color["sol"])
    display.blit(text, (xSol+5, ySol+10))

    # new puzzle button
    pygame.draw.rect(display, color["bl"], (xNew, yNew, cell*2, cell), 3)
    text = font.render("New", True, color["sol"])
    display.blit(text, (xNew+15, yNew+10))

    # difficulty level buttons

# returns mouse position
def click(pos):
    if pos[0] < width and pos[1] < height:
        col = pos[0] // cell
        row = pos[1] // cell
        return(int(row), int(col))
    else:
        return None

def hightlight(pos, display):
    # cells highlighted in red when selected
    try:
        x, y = pos
        pygame.draw.rect(display, color["re"], (y*cell, x*cell, cell, cell), 2)
    except TypeError:
        print("Outside grid")

# fills in number inputs
def fillVal(display, val, pos):
    x, y = click(pos)
    text = font.render(str(val), 1, color["bl"])
    display.blit(text, (x, y))

# redraws board whenever cell is highlighted to get rid of old highlights
def redrawer(puzzle, sol, solOn):
    display.fill(color["wh"])
    drawGrid()
    drawNum(puzzle, sol, solOn, display)
    checkSol()

def main():
    global display, pos
    puzzle, sol = puzzleMaker()

    display = pygame.display.set_mode((width, height+ex))

    pygame.display.set_caption("Sudoku")
    key = None
    run = True
    select = False
    solOn = False
    redrawer(puzzle,sol,solOn)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                select = True
                # grid selection
                if pos[0] < width and pos[1] < height:
                    redrawer(puzzle, sol, solOn)
                    hightlight(click(pos), display)
                    key = None
                # solve button selection
                if width // 2 - cell + cell*2 > pos[0] > width // 2 - cell and (height+ex)-77 + cell > pos[1] > (height+ex)-77:
                    solOn = True
                    redrawer(puzzle, sol, solOn)
                # new game button
                if width // 6 - cell + cell*2 > pos[0] > width // 6 - cell and (height+ex) - 77 + cell > pos[1] > (height+ex)-77:
                    puzzle, sol = puzzleMaker()
                    solOn = False
                    redrawer(puzzle, sol, solOn)

        # takes input and updates puzzle with it
        if select == True and key != None and pos[0] < width and pos[1] < height:
            row, col = click(pos)
            # only draws numbers if you click on empty cell
            if puzzle[row][col] == " " or type(puzzle[row][col]) == str:
                puzzle[row][col] = str(key)
                # if correct, solution cell also changes to str
                if sol[row][col] == key:
                    sol[row][col] = str(key)
                redrawer(puzzle, sol, solOn)
                text = font.render(str(key), True, color["input"])
                display.blit(text, (col*cell+18, row*cell+15))
        
        pygame.display.update()

if __name__ == "__main__":
    main()