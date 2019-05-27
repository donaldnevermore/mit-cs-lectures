import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """单个外星人"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置rect属性
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # 在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向右移动"""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x
