import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width = 400
height = 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define the snake's starting position and size
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Define the food's starting position
food_pos = [random.randrange(1, width//10)*10, random.randrange(1, height//10)*10]

# Define the game variables
direction = "RIGHT"
change_to = direction
score = 0

# Define the font
font_style = pygame.font.SysFont(None, 30)

def display_score(score):
    score_font = font_style.render("Score: " + str(score), True, black)
    display.blit(score_font, [0, 0])

def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(display, white, pygame.Rect(pos[0], pos[1], 10, 10))

def draw_food(food_pos):
    pygame.draw.rect(display, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

# Define the game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            elif event.key == pygame.K_DOWN:
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT:
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Update the direction of the snake
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    elif change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    elif change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    elif change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Move the snake
    if direction == "UP":
        snake_pos[1] -= 10
    elif direction == "DOWN":
        snake_pos[1] += 10
    elif direction == "LEFT":
        snake_pos[0] -= 10
    elif direction == "RIGHT":
        snake_pos[0] += 10

    # Check for collision with the food
    if snake_pos == food_pos:
        food_pos = [random.randrange(1, width//10)*10, random.randrange(1, height//10)*10]
        score += 10
        snake_body.append(snake_pos)

    # Move the snake's body
    snake_body.insert(0, list(snake_pos))
    if len(snake_body) > score/10 + 1:
        snake_body.pop()

    # Check for collision with the wall
    if snake_pos[0] < 0 or snake_pos[0] > width-10 or snake_pos[1] < 0 or snake_pos[1] > height-10:
        game_over = True

    # Check for collision with
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over = True

    # Clear the display
    display.fill(black)

    # Draw the snake and the food
    draw_snake(snake_body)
    draw_food(food_pos)

    # Display the score
    display_score(score)

    # Update the display
    pygame.display.update()

    # Set the game's FPS
    clock.tick(60)