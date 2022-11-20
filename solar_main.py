# coding: utf-8
# license: GPLv3

import pygame
from solar_vis import *
from solar_model import *
from solar_input import *

FPS = 30

WHITE = 0xFFFFFF
RED = (255,   0,   0)
BLACK = (0, 0, 0)

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

physical_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

displayed_time = None
"""Отображаемое на экране время.
Тип: переменная tkinter"""

dt = None
"""Шаг по времени при моделировании.
Тип: float"""

space_objects = []
"""Список космических объектов."""
clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((window_width, window_height))

space_objects = read_space_objects_data_from_file('double_star.txt', screen)
calculate_scale_factor(1E10)

finished = False



while not finished:
    screen.fill(BLACK)

    dt = clock.tick()

    clock.tick(FPS)
    for obj in space_objects:
        pygame.draw.circle(
            obj.screen,
            obj.color,
            (scale_x(obj.x), scale_y(obj.y)),
            obj.R)

        # print(scale_x(obj.x))
        # print(obj.x)
        # print(obj.Vx)
    # print(space_objects[0].Vy)
    pygame.display.update()
    recalculate_space_objects_positions(space_objects, dt*600)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
