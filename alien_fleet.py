import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet():
    def __init__(self, game:"AlienInvasion"):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_Fleet()

    def create_Fleet(self):
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)

        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space)//2)
        y_offset = int((half_screen - fleet_vertical_space)//2)
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h / 2)//alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)

    def _create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def draw(self):
        alien: "Alien"
        for alien in self.fleet:
            alien.draw_alien()