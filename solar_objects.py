# coding: utf-8
# license: GPLv3

import pygame


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, screen):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = 50
        self.y = 50
        self.R = 10
        self.vx = 0
        self.vy = 0
        self.color = "red"
        self.type = "planet"
        self.image = None
    
        
        

class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """
    def __init__(self, screen):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = 0
        self.y = 0
        self.R = 10
        self.vx = 0
        self.vy = 0
        self.color = "green"
        self.type = "planet"
        self.image = None
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.R
        )

        