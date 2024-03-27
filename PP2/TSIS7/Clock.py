import pygame
import sys
import time
from datetime import datetime

# Инициализация Pygame
pygame.init()

# Установка размера окна
WIDTH, HEIGHT = 400, 400
WINDOW_SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Clock")

# Загрузка изображений для стрелок и фона
clock_bg_img = pygame.image.load("TSIS7/images/backend.jpg")  # Фото часов в качестве фона
minute_hand_img = pygame.image.load("TSIS7/images/minute.png")
second_hand_img = pygame.image.load("TSIS7/images/second.png")

# Функция для отрисовки часов и стрелок
def draw_clock(minute_angle, second_angle):
    window.blit(clock_bg_img, (0, 0))  # Отрисовка фона
    
    # Отрисовка минутной стрелки
    rotated_minute_hand = pygame.transform.rotate(minute_hand_img, minute_angle)
    minute_rect = rotated_minute_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(rotated_minute_hand, minute_rect)
    
    # Отрисовка секундной стрелки
    rotated_second_hand = pygame.transform.rotate(second_hand_img, second_angle)
    second_rect = rotated_second_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(rotated_second_hand, second_rect)
    
    pygame.display.update()

# Основной цикл приложения
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Получение текущего времени
        current_time = datetime.now().time()
        minute = current_time.minute
        second = current_time.second
        
        # Вычисление углов для стрелок
        minute_angle = -(minute / 60.0) * 360.0
        second_angle = -(second / 60.0) * 360.0
        
        # Отрисовка часов с учетом углов
        draw_clock(minute_angle, second_angle)
        
        # Задержка для обновления времени каждую секунду
        time.sleep(1)

if __name__ == "__main__":
    main()
