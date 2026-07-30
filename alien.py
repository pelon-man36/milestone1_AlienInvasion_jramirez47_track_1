"""
alien_invasion.py
Johan D. Ramirez Maldonado
This file will create a bullet that the ship uses
Starter Code forked from: RedBeard41/alien_invasion_starter
7/24/26
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """Stores everything needed to create a bullet"""

    def __init__(self, game: "AlienInvasion", x: float, y: float):
        """Initial setup"""
        super().__init__()
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h)
            )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        temp_speed = self.settings.fleet_speed
        self.x += temp_speed
        self.rect.x = self.x

    def draw_alien(self):
        """Draws the bullet onto the screen"""
        self.screen.blit(self.image, self.rect)
