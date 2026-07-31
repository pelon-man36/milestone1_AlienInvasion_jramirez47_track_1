"""
alien_invasion.py
Johan D. Ramirez Maldonado
This file will create a bullet that the ship uses
Starter Code forked from: RedBeard41/alien_invasion_starter
7/31/26
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Stores everything needed to create a bullet"""

    def __init__(self, game: "AlienInvasion"):
        """Initial setup"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
            )

        self.rect = self.image.get_rect()
        self.rect.midright = game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Updates the bullet as it travels to the right"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draws the bullet onto the screen"""
        self.screen.blit(self.image, self.rect)
