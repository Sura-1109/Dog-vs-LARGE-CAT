import pygame
import sys
import os

# --- Always load assets relative to this file ---
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# --- Constants ---
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 5
JUMP_FORCE = 15
GRAVITY = 0.8
GROUND_HEIGHT = 100

# --- Pygame setup ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pegasus on the Run Phase 1")
clock = pygame.time.Clock()

# --- Player ---
player = pygame.Rect(WIDTH // 2, HEIGHT - 150, 50, 50)
vel_y = 0.0
on_ground = False
facing_right = True

# --- Camera ---
camera_x = 0

# --- Load horse sprite (robust path) ---
horse_path = os.path.join(BASE_PATH, "horse.png")
try:
    horse_img = pygame.image.load(horse_path).convert_alpha()
except pygame.error as e:
    print(f"Could not load horse.png at: {horse_path}")
    raise
horse_img = pygame.transform.scale(horse_img, (80, 80))  # <-- use the variable, not a string!

def draw():
    screen.fill((135, 206, 235))  # sky

    # ground (very wide)
    pygame.draw.rect(
        screen, (50, 205, 50),
        (0 - camera_x, HEIGHT - GROUND_HEIGHT, 999999, GROUND_HEIGHT)
    )

    # player horse
    if facing_right:
        screen.blit(horse_img, (player.x - camera_x, player.y))
    else:
        screen.blit(pygame.transform.flip(horse_img, True, False),
                    (player.x - camera_x, player.y))

    pygame.display.flip()

def update(jump_pressed: bool):
    global vel_y, on_ground, camera_x, facing_right

    keys = pygame.key.get_pressed()

    # horizontal movement
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= PLAYER_SPEED
        facing_right = False
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += PLAYER_SPEED
        facing_right = True

    # jump (use KEYDOWN edge so holding space doesn't auto-jump forever)
    if jump_pressed and on_ground:
        vel_y = -JUMP_FORCE
        on_ground = False

    # gravity
    vel_y += GRAVITY
    player.y += vel_y

    # ground collision
    ground_top = HEIGHT - GROUND_HEIGHT
    if player.bottom >= ground_top:
        player.bottom = ground_top
        vel_y = 0
        on_ground = True

    # camera follows player
    camera_x = player.x - WIDTH // 2

# --- Game loop ---
while True:
    jump_pressed = False  # capture KEYDOWN once per frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP):
            jump_pressed = True

    update(jump_pressed)
    draw()
    clock.tick(FPS)


#Phase 2

import pygame
import sys
import os
import random

#---Asset path setup---
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

#---Constants---
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 5
JUMP_FORCE = 15
GRAVITY = 0.8
GROUND_HEIGHT = 100

#---Pygame init---
pygame.init()
screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Pegasus on the Run, Phase 2")
clock = pygame.time.Clock()

#---Player setup---
player = pygame.Rect(WIDTH //2,  HEIGHT - 150, 50, 50)
vel_y  = 0
on_ground = False
facing_right = True

#---Camera---
camera_x = 0

#---Load images---
def load_img(filename, size=None):
    path = os.path.join(BASE_PATH, filename)
    img = pygame.image.load(path).convert_alpha()
    if size:
        img = pygame.transform.scale(img, size)
    return horse_img

horse_img = load_img("horse.png", (80, 80))

cloud_img = load_img("cloud.png", (120,60)) if os.path.exists(os.path.join(BASE_PATH, "cloud.png")) else None
cloud1_img = load_img("cloud1.png", (120,60)) if os.path.exists(os.path.join(BASE_PATH, "cloud1.png")) else None
cloud2_img = load_img("cloud2.png", (120, 60)) if os.path.esits(os.path.join(BASE_PATH, "cloud2.png")) else None
cloud3_img = load_img("cloud3.png", (120, 60)) if os.path.exists(os.path.join(BASE_PATH, "cloud3.png")) else None
cloud4_img = load_img("cloud4.png", (120, 60)) if os.path.exists(os.path.join(BASE_PATH, "cloud4.png")) else None
cloud5_img = load_img("clouds5.png", (120,60)) if os.path.exists(os.path.join(BASE_PATH, "cloud5.png")) else None
cloud6_img = load_img("cloud6.png", (120,60)) if os.path.exists(os.path.join(BASE_PATH, "cloud6.png")) else None
cloud7_img = load_img("cloud7.png", (120, 60)) if os.path.exists(os.path.join(BASE_PATH, "cloud7.png")) else None
cloud8_img = load_img("cloud8.png", (120, 60)) if os.path.exists(os.path.join(BASE_PATH, "cloud8.png")) else None            
background1_img = load_img("background1.png") if os.path.exists(os.path.join(BASE_PATH, "background1.png")) else None
background2_img = load_img("background2.png") if os.path.exists(os.path.join(BASE_PATH, "background2.png")) else None
background3_img = load_img("background3.png") if os.path.exists(os.path.join(BASE_PATH, "background3.png")) else None
hill1_img = load_img("hill1.png") if os.path.exists(os.path.join(BASE_PATH, "hill1.png")) else None
hill2_img = load_img("hill2.png") if os.path.exists(os.path.join(BASE_PATH, "hill2.png")) else None
hill3_img = load_img("hill3.png") if os.path.exists(os.path.join(BASE_PATH, "hill3.png")) else None

#---Clouds---
clouds = [{"x": random.randint(0, 2000), "y": random.randint(50, 200), "speed": random.uniform(0.2, 0.5)} for _ in range(5)]

#---Backgrounds---
backgrounds = []




