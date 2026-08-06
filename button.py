"""
button.py
Johan D. Ramirez Maldonado
This file stores the button used to start the game
Starter Code forked from: RedBeard41/alien_invasion_starter
8/6/26
"""
import pygame.font
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal
class Button:
    """Stores everything needed to make a button"""
    def __init__(self, game: "AlienInvasion", msg):
        """Initial setup"""
        self.game = game
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.button_font_size)
        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Prepares the message rect"""
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draws the rect"""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        """Checks if the mouse clicked the button"""
        return self.rect.collidepoint(mouse_pos)

        