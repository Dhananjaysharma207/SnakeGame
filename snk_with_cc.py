import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating Window
screen_width = 900
screen_height = 600
GameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakeGameByDhananjay")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def screen_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    GameWindow.blit(screen_text, [x, y])


def plot_snake(GameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(GameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        GameWindow.fill((0,255,127))
        screen_score("WELCOME TO SNAKES GAME !", black, 180, 270)
        screen_score("PRESS SPACE  BAR TO PLAY !", red, 180, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()


        pygame.display.update()
        clock.tick(50)


# Game Loop
def game_loop():
    # Game Specific Variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    with open("high_score.txt", "r") as f:
        high_score = f.read()

    Food_x = random.randint(20, screen_width / 2)
    Food_y = random.randint(20, screen_height / 2)
    Score = 0
    init_velocity = 5
    snake_size = 30
    fps = 50

    while not exit_game:
        if game_over:
            with open("high_score.txt", "w") as f:
               f.write(str(high_score))

            GameWindow.fill((127,255,212))
            screen_score("Game Over! Press Enter To Continue", red, 100, 270)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_a:
                        Score += 5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - Food_x) < 18 and abs(snake_y - Food_y) < 18:
                Score += 10

                Food_x = random.randint(20, screen_width / 2)
                Food_y = random.randint(20, screen_height / 2)
                snk_length += 5
                if Score >  int(high_score):
                    high_score = Score

            GameWindow.fill((186,85,211))
            screen_score("Score: " + str(Score) + "   high_score: "+ str(high_score), red, 5, 5)
            pygame.draw.rect(GameWindow, red, [Food_x, Food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # Game over Condition
            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(GameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
