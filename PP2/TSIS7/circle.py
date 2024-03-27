import pygame
import sys
pygame.init()
screen_widht = 800
screen_height = 600
screen = pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption("Перемещение шарика")

white =(255,255,255)
red = (255,0,0)
ball_radius = 25
ball_x = (screen_widht - ball_radius*2)//2
ball_y = (screen_height - ball_radius*2)//2
speed = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - speed >= 0:
        ball_y -= speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius * 2 + speed <= screen_height:
        ball_y += speed
    if keys[pygame.K_LEFT] and ball_x - speed >= 0:
        ball_x -= speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius * 2 + speed <= screen_widht:
        ball_x += speed
    screen.fill(white)
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(30)