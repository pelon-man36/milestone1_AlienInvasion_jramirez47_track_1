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
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h)
            )

        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

    def draw(self):
        self.screen.blit(self.image, self.rect)