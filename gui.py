import pygame
import requests

# setting up width and bg colour of window
width = 550
bgColor = (38, 38, 38)
oriElemColor = (255, 255, 255)
buffer = 5

# adding API
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
board = response.json()["board"]
boardOri = [[board[i][j] for i in range(len(board))] for j in range(len(board[0]))]

# adding functionality of game
def insert(win, pos):
    i, j = pos[0], pos[1]
    myFont = pygame.font.SysFont("Arial", 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if boardOri[i-1][j-1] != 0:
                    return
                if event.key == 48: # checking with 0
                    board[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, bgColor,
                    (pos[0]*50+buffer, pos[1]*50+buffer,
                    50-2*buffer, 50-2*buffer))
                    pygame.display.update()
                    return
                if 0 < event.key - 48 < 10: # checking valid input
                    pygame.draw.rect(win, bgColor,
                    (pos[0]*50+buffer, pos[1]*50+buffer,
                    50-2*buffer, 50-2*buffer))
                    value = myFont.render(str(event.key-48), True
                    (179, 179, 179))
                    win.blit(value, (pos[0]*50+15, pos[1]*50))
                    board[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return

# initialising pygame
def main():
    pygame.init()
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku")
    win.fill(bgColor)
    myFont = pygame.font.SysFont("Arial", 35)

    # creating grid lines
    for i in range(len(board)):
        if i % 3 == 0:
            # vertical block line
            pygame.draw.line(win, (255,255,255), (50+50*i,50), (50+50*i,500),4)
            # horizontal block line
            pygame.draw.line(win, (255,255,255), (50, 50+50*i), (500, 50+50*i), 4)
        # vertical line
        pygame.draw.line(win, (166,166,166), (50+50*i, 50), (50+50*i,500), 2)
        # horizontal line
        pygame.draw.line(win, (166,166,166), (50,50+50*i),(500,50+50*i), 2)
    pygame.display.update()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if 0 < board[i][j] < 10:
                value = myFont.render(str(board[i][j]), True, oriElemColor)
                win.blit(value, ((j+1)*50+15, (i+1)*50))
    pygame.display.update()
    
    # close window when quit key pressed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()