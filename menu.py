import pygame
import sys
import subprocess
import level1

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Holy Molly World")
clock = pygame.time.Clock()

# Загрузка изображений
background = pygame.image.load('Assets/menu.jpg')

# Шрифт для текста
font = pygame.font.Font('Assets/fonts/pix_font.ttf', 100)

# Тексты для кнопок
exit_text = font.render("Выход", True, BLACK)
levels_text = font.render("Уровни", True, BLACK)
about_text = font.render("Об игре", True, BLACK)

# Тексты уровней
level_1_text = font.render("1", True, BLACK)

# Координаты кнопок меню
exit_rect = exit_text.get_rect(center=(400, 300))
levels_rect = levels_text.get_rect(center=(400, 450))
about_rect = about_text.get_rect(center=(400, 600))

# координаты кнопок уровней
level_1_rect = level_1_text.get_rect(center=(400, 200))



# Переменные для уровня
fortress_health = 100
wave_number = 1
mob_speed = 5
mob_pos = 0

run = True
in_menu = True
in_levels = False
levels = [False]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(background, (0, 0))

    if in_menu:
        screen.blit(exit_text, exit_rect)
        screen.blit(levels_text, levels_rect)
        screen.blit(about_text, about_rect)

        mouse_pos = pygame.mouse.get_pos()
        if exit_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                run = False
        elif levels_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                in_menu = False
                in_levels = True

        elif about_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                in_menu = False
                # Здесь вы можете добавить код для отображения информации об игре
    if in_levels:
        screen.blit(level_1_text, level_1_rect)
        mouse_pos = pygame.mouse.get_pos()
        if level_1_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                levels[0] = True
                in_levels = False
    if levels[0]:
        subprocess.call(['python', 'level1.py'])




    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()