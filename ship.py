"""
alien_invasion.py
Johan D. Ramirez Maldonado
This file will create the ship, which can be moved about on screen
Starter Code forked from: RedBeard41/alien_invasion_starter
7/31/26
"""
import pygame
from typing import TYPE_CHECKING
from settings import Settings
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """Everything to create the ship"""

    def __init__(self, game: "AlienInvasion", arsenal: "Arsenal"):
        """Initial setup for ship"""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h)
            )

        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_up = False
        self.moving_down = False
        self.arsenal = arsenal

    def _center_ship(self):
        """Centers the ship."""
        self.rect.midleft = self.boundaries.midleft
        self.y = float(self.rect.y)

    def update(self):
        """Updates the position of the ship, plus its Arsenal"""
        # Updating the position of ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """The ships movement for up & down"""
        temp_speed = self.settings.ship_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        self.rect.y = self.y

    def draw(self):
        """Draws the ship"""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """The ship fires a bullet, if fire_bullet is True"""
        return self.arsenal.fire_bullet()

    def check_collisons(self, other_group):
        """Checks ship collisons with other sprites, specifically aliens."""
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        else:
            return False