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
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        # Updating the position of ship
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)