"""
alien_fleet.py
Johan D. Ramirez Maldonado
This file will create an alien fleet
Starter Code forked from: RedBeard41/alien_invasion_starter
8/6/26
"""

import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet():
    """Stores everything needed for an alien fleet."""
    def __init__(self, game:"AlienInvasion"):
        """Initial setup for the alien fleet."""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_Fleet()

    def create_Fleet(self):
        """Creates a fleet of aliens by calling methods."""
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)

        x_offset, y_offset = self.calculate_offset(alien_w, alien_h, screen_h, fleet_w, fleet_h)

        self._create_rectangle_fleet(alien_w, alien_h, fleet_h, fleet_w, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Creates the rectangle shape of the fleet."""
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offset(self, alien_w, alien_h, screen_h, fleet_w, fleet_h):
        """Calculates the offset (gaps) for the fleet."""
        half_screen = self.settings.screen_w//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        y_offset = int((screen_h + fleet_horizontal_space)//2)
        x_offset = int((half_screen - fleet_vertical_space)//2)
        return y_offset,x_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """Calculates the size of the fleet."""
        fleet_w = ((screen_w / 2)//alien_w)
        fleet_h = (screen_h//alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_h), int(fleet_w)

    def _create_alien(self, current_x: int, current_y: int):
        """Uses the alien file to create an alien for the fleet."""
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """Checks if the fleet has hit a boundary. If so, changes direction and moves down."""
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self.drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def drop_alien_fleet(self):
        """Moves the fleet a level."""
        for alien in self.fleet:
            alien.x -= self.fleet_drop_speed

    def update_fleet(self):
        """Updates the fleet. after first checking the edges."""
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """Draws the alien."""
        alien: "Alien"
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisons(self, other_group):
        """Checks collisons for the fleet and other group, like the ship or bullet."""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_left(self):
        """Checks if the fleet has hit the left boundary. If true, level resets."""
        alien: Alien
        for alien in self.fleet:
            if alien.rect.left <= 0:
                return True
        return False
    
    def check_destroyed_status(self):
        """Checks if the fleet is fully destroyed."""
        return not self.fleet