
from sys import builtin_module_names
import pygame
import os
pygame.font.init()

size = width, height = 700, 600
WIN = pygame.display.set_mode(size)
pygame.display.set_caption("Don't drop the ball")
FPS = 60
VEL = 10  # velocity

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

BORDER = pygame.Rect(0, height//3 + 50, width, 10)  # BILA CARA

CHARACTER_WIDTH, CHARACTER_HEIGHT = 110, 110
BALL_WIDTH, BALL_HEIGHT = 50, 50
TENNISBALL_WIDTH, TENNISBALL_HEIGHT = 25, 25

jumping = False
Y_GRAVITY = 2
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
BALL_VELOCITY = 5
TENNISBALL_VELOCITY = 10
MAX_TENNISBALLS = 3
Ballx_position = 300
Bally_position = 100
Tennisballs_count = MAX_TENNISBALLS
Tennisballs = []

CHARACTER_HEALTH = 3
HEALTH_FONT = pygame.font.SysFont('comicsans', 30)

CHARACTER_IMAGE = pygame.image.load(
    os.path.join("Assets", "frank-a.png"))
# pygame.transform.scale nam zmeni velikost CHARACTER
CHARACTER = pygame.transform.scale(
    CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
CHARACTER_JUMPING_IMAGE = pygame.image.load(
    os.path.join("Assets", "frank-jump.png"))
CHARACTER_JUMP = pygame.transform.scale(
    CHARACTER_JUMPING_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
BALL_IMAGE = pygame.image.load(os.path.join("Assets", "ball.png"))
BALL = pygame.transform.scale(BALL_IMAGE, (BALL_WIDTH, BALL_HEIGHT))
TENNISBALL_IMAGE = pygame.image.load(os.path.join("Assets", "tennisball.png"))
TENNISBALL = pygame.transform.scale(
    TENNISBALL_IMAGE, (TENNISBALL_WIDTH, TENNISBALL_HEIGHT))
BACKGROUND_IMAGE = pygame.image.load(
    os.path.join("Assets", "pixel-background_2.jpg"))
BACKGROUND = pygame.transform.scale(
    BACKGROUND_IMAGE, (width, height))

# novej event #cisla slouzi k identifikaci eventu (musi byt jina)
Ball_hit = pygame.USEREVENT + 1
Character_hit = pygame.USEREVENT + 2
Character_catch = pygame.USEREVENT + 3
Ball_fell = pygame.USEREVENT + 4

Character = pygame.Rect(290, 400, CHARACTER_WIDTH, CHARACTER_HEIGHT)
Ball = pygame.Rect(Ballx_position, Bally_position, BALL_WIDTH, BALL_HEIGHT)

def CHARACTER_MOVEMENT():
    # kazdych 60FPS zjisti jake keys jsou stlaceny a podle toho pridava nebo ubira hodnotu Characteru(Rectanglu) na X axis
    keys_pressed = pygame.key.get_pressed()
    # LEFT # and Character.x... nam rika ze nam dovoli udelat krok pokud neprekrocime border mapy neboli 0
    if keys_pressed[pygame.K_a] and Character.x - VEL > 0:
        Character.x -= VEL
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_d] and Character.x + VEL + Character.width < width:  # RIGHT
        Character.x += VEL

def draw_window():
    WIN.blit(BACKGROUND, (0, 0))
    # WIN.fill(BLUE) #pokud cheme mit background modrej
    pygame.draw.rect(WIN, WHITE, BORDER)  # Bila Cara
    CHARACTER_HEALTH_TEXT = HEALTH_FONT.render(
        "Health: " + str(CHARACTER_HEALTH), 1, RED)
    TENNISBALLS_COUNT = HEALTH_FONT.render(
        "Balls: " + str(MAX_TENNISBALLS), 1, BLACK)
    WIN.blit(CHARACTER_HEALTH_TEXT,
             (width - CHARACTER_HEALTH_TEXT.get_width() - 10, 10))
    WIN.blit(TENNISBALLS_COUNT,
             (width - CHARACTER_HEALTH_TEXT.get_width() - 10, 50))
    # WIN.blit musi byt za WIN.fill jinak se character neobjevi kvuli tomu ze barva se fillne po tom co character a prekresli nam ho
    # character.x a .y je variable a postava se lockne na misto rectanglu
    WIN.blit(CHARACTER, (Character.x, Character.y))
    WIN.blit(BALL, (Ball.x, Ball.y))
    # updatne nam display, jinak by barva nezustala

    for Tennisball in Tennisballs:
        # pygame.draw.rect(WIN, GREEN, Tennisball) #pokud bych nemel image Tennisballu
        WIN.blit(TENNISBALL, (Tennisball.x, Tennisball.y))

    pygame.display.update()


def hlavni_funkce(jumping, Y_VELOCITY):

    global CHARACTER_HEALTH

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and len(Tennisballs) < MAX_TENNISBALLS:
                    Tennisballs()
            if event.type == Ball_hit:
                Ball.y -= VEL * 5
            if event.type == Ball_fell:
                CHARACTER_HEALTH -= 1
                
        if CHARACTER_HEALTH <= 0:
            END_text = "You've lost!"

        keys_pressed = pygame.key.get_pressed()
        # JUMP #SPACE mi nesel ve funkci CHARACTER_MOVEMENT tak musi byt tu
        if keys_pressed[pygame.K_SPACE]:
            jumping = True
        if jumping:
            Character.y -= Y_VELOCITY
            Y_VELOCITY -= Y_GRAVITY
            if Y_VELOCITY < -JUMP_HEIGHT:
                jumping = False
                Y_VELOCITY = JUMP_HEIGHT

        CHARACTER_MOVEMENT()
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    # funkce hlavni_funkce se zapne pouze, pokud zapneme tento soubor
    hlavni_funkce(jumping, Y_VELOCITY)
