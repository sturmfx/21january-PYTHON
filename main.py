import numpy as np
import pygame

dimensions = (10, 10)
dot_size = 50
board = np.random.randint(2, size=dimensions)
pygame.init()
screen = pygame.display.set_mode((dimensions[0] * dot_size, dimensions[1] * dot_size))

def update_board(board):
    new_board = board.copy()
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            neighboars = np.sum(board[i - 1:i + 2, j - 1:j + 2]) - board[i, j]
            if board[i, j] == 1:
                if neighboars < 2 or neighboars > 3:
                    new_board[i, j] = 0
            else:
                if neighboars == 3:
                    new_board[i, j] = 1
    return new_board

running = True
paused = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not paused:
        board = update_board(board)

    screen.fill((255,255,255))
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if board[i,j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (i * dot_size, j * dot_size, dot_size, dot_size))

    keyboard = pygame.key.get_pressed()
    if keyboard[pygame.K_SPACE]:
        paused = not paused
    if keyboard[pygame.K_r]:
        board = np.random.randint(2, size=dimensions)
    pygame.display.update()
    pygame.time.wait(150)
pygame.quit()
