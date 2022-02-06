import pygame
x = pygame.init()

#creating window
mygameWindow=pygame.display.set_mode((1200,500))

#game window title
pygame.display.set_caption("MY FIRST PYTHON GAME")

#game specific variable
exit_game = False
game_over = False

#creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed Right arrow key")

pygame.quit()
quit()