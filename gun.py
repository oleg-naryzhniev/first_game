import pygame
from pygame.sprite import Sprite


class Gun(Sprite):

    def __init__(self, screen):
        """инициализация пушки"""

        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/plane.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.bot = float(self.rect.bottom)
        self.mright = False
        self.mleft = False
        self.m_up = False
        self.mdown = False



    def output(self):
        """рисование пушки"""

        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 3
        if self.mleft and self.rect.left > 0:
            self.center -= 3
        if self.m_up and self.rect.top > 0:
            self.bot -= 1
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.bot += 2

        self.rect.centerx = self.center
        self.rect.bottom = self.bot

    def create_gun(self):
        """размещает пушку по центру внизу"""
        self.center = self.screen_rect.centerx