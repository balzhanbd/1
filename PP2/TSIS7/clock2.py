import pygame
import datetime

pygame.init()
screen_width, screen_height = 800,800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(center=originPos)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=image_rect.center)
    rotated_image_rect.center = pos
    surf.blit(rotated_image, rotated_image_rect)


mainclock = pygame.image.load("TSIS7/images/backend.jpg")
seconds = pygame.image.load("TSIS7/images/second.png")  
minute = pygame.image.load("TSIS7/images/minute.png")

mainclockw, mainclockh = mainclock.get_size()

clockcenter = (screen_width // 2, screen_height // 2)

coordinate_center = (400, 400)

done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = datetime.datetime.now()
    
    curr_seconds = current_time.second + current_time.microsecond / 1000000 
    angle_seconds = -(curr_seconds / 60) * 360  

    curr_min = current_time.minute + curr_seconds / 60  
    angle_minutes = -(curr_min / 60) * 360 

    screen.blit(mainclock, (0, 0))  

    blitRotate(screen, seconds, coordinate_center, coordinate_center, angle_seconds)  
    blitRotate(screen, minute, coordinate_center, coordinate_center, angle_minutes)
    
    pygame.display.flip()

pygame.quit()