import pygame
import time
import random

pygame.init()

# Window dimensions
width = 800
height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake block size and speed
block_size = 20
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def snake_game():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()

    def display_score(score):
        text = score_font.render("Score: " + str(score), True, white)
        screen.blit(text, [10, 10])

    def draw_snake(snake_body):
        for block in snake_body:
            pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

    def message(msg, color):
        text = font_style.render(msg, True, color)
        screen.blit(text, [width / 6, height / 3])

    def game_loop():
        game_over = False
        game_exit = False

        # Initial snake position and movement
        x = width / 2
        y = height / 2
        x_change = 0
        y_change = 0

        # Snake body
        snake_body = []
        snake_length = 1

        # Initial food position
        food_x = round(random.randrange(0, width - block_size) / float(block_size)) * block_size
        food_y = round(random.randrange(0, height - block_size) / float(block_size)) * block_size

        while not game_exit:
            while game_over:
                screen.fill(black)
                message("Game Over! Press C to Play Again or Q to Quit", red)
                display_score(snake_length - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_exit = True
                            game_over = False
                        if event.key == pygame.K_c:
                            snake_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -block_size
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = block_size
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        x_change = 0
                        y_change = -block_size
                    elif event.key == pygame.K_DOWN:
                        x_change = 0
                        y_change = block_size

            if x >= width or x < 0 or y >= height or y < 0:
                game_over = True

            x += x_change
            y += y_change
            screen.fill(black)
            pygame.draw.rect(screen, white, [food_x, food_y, block_size, block_size])

            snake_head = []
            snake_head.append(x)
            snake_head.append(y)
            snake_body.append(snake_head)
            if len(snake_body) > snake_length:
                del snake_body[0]

            for block in snake_body[:-1]:
                if block == snake_head:
                    game_over = True

            draw_snake(snake_body)
            display_score(snake_length - 1)

            pygame.display.update()

            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, width - block_size) / float(block_size)) * block_size
                food_y = round(random.randrange(0, height - block_size) / float(block_size)) * block_size
                snake_length += 1

            clock.tick(snake_speed)

    game_loop()

    pygame.quit()
    quit()


snake_game()
