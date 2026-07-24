import pygame
from typing import TYPE_CHECKING
from settings import Settings
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship:
    def __init__(self, game: "AlienInvasion"):
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
        self.rect.midleft = self.boundaries.midleft
        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)

    def update(self):
        # Updating the position of ship
        temp_speed = self.settings.ship_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)