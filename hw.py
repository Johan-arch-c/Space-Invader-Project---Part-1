import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader - Part 1")

player_img = pygame.Surface((40, 40))
player_img.fill((0, 255, 0))
player_x = 370
player_y = 500
player_speed = 5

enemy_img = pygame.Surface((40, 40))
enemy_img.fill((255, 0, 0))

enemy_x = []
enemy_y = []

for i in range(7):
    enemy_x.append(random.randint(0, 760))
    enemy_y.append(random.randint(0, 300))

score = 0
font = pygame.font.Font(None, 36)

def show_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def detect_collision(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance < 40

running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 760:
        player_x += player_speed

    screen.blit(player_img, (player_x, player_y))

    for i in range(7):

        if detect_collision(player_x, player_y, enemy_x[i], enemy_y[i]):
            score += 1
            enemy_x[i] = random.randint(0, 760)
            enemy_y[i] = random.randint(0, 300)

        screen.blit(enemy_img, (enemy_x[i], enemy_y[i]))

    show_score()

    pygame.display.update()

pygame.quit()
