import pygame
import sys
import random

# Functions
#bb = 0


def ball_animation():
    # Better to use return statements in more complex code
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time, middle_line
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1  # Border bounce
    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()  # ball reset
    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()  # ball reset

    # ball_speed_x > 0 # ball has to come from left
    if ball.colliderect(player) and ball_speed_x > 0:
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        # when ball hits player from top
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        # when ball hits player from bottom
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            # if statements fix a bug when hitting player from sides
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    #if ball == screen_width/2:
        #bb += 1
    #if ball == screen_width/2 and bb >= 5:
        #ball_speed_x *= -1


def player_animation():
    # player_speed = 0 so we can assign value later to it in player_movement function
    player.y += player_speed
    if player.top <= 0:
        player.top = 0  # Upside border
    if player.bottom >= screen_height:
        player.bottom = screen_height  # Downside border


def opponent_ai():
    if opponent.top < ball.y:  # Copies movement of the ball
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0  # Upside border
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height  # Downside border


def player_movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= 10
    if keys[pygame.K_DOWN]:
        player.y += 10


def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 2100:  # 2100 milliseconds # Countdown till the game starts
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Colors
bg_color = pygame.Color("grey12")
light_grey = (255, 100, 40)  # 200, 200, 200

# Game Variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7
middle_line = pygame.Rect(screen_width/2, 0, 1, screen_height)

# Text Variables
player_score = 0
opponent_score = 0
# Has to be SysFont, not only Font
game_font = pygame.font.SysFont('freesansbold.tff', 50)

# Score Timer
score_time = True  # In the beginning, ball auto resets

run = True
while run:  # Main game loop
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player_movement()
    ball_animation()
    player_animation()
    opponent_ai()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, middle_line)

    # Time
    if score_time:
        ball_restart()

    # Score
    player_text = game_font.render(
        f"{player_score}", False, light_grey)  # False, Antialiasing
    screen.blit(player_text, (screen_width/2 + 20, 0 + 15))
    opponent_text = game_font.render(
        f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (screen_width/2 - 34, 0 + 15))

    # Updating the window
    pygame.display.flip()
    clock.tick(90)
