"""
alien_invasion.py
Johan D. Ramirez Maldonado
This file will create the ships arsenal, storing bullets and firing if able
Starter Code forked from: RedBeard41/alien_invasion_starter
7/24/26
"""
import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    """Stores what is needed for the ships arsenal"""
    def __init__(self, game: "AlienInvasion"):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Updates the arsenal, including _remove_bullets_offscreen"""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Removes any bullets that flied off screen"""
        for bullet in self.arsenal.copy():
            if bullet.rect.right >= 1200:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draws the bullets for the arsenal"""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """
        Fires bullets, but will not fire more bullets until prior bullets are removed from the screen
            Returns True if a bullet can be fired, False otherwise
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
