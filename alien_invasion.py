"""
alien_invasion.py
Johan D. Ramirez Maldonado
This file will run the Alien Invasion, a playable game
Starter Code forked from: RedBeard41/alien_invasion_starter
7/24/26
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
# from alien import Alie
from alien_fleet import AlienFleet

class AlienInvasion:
    """Stores everything Alien Invasion needs to run properly"""
    def __init__(self):
        """Initial setup"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact)
        self.impact_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self, )
        self.alien_fleet.create_Fleet()


    def run_game(self):
        """Runs the game"""
        # Game Loop
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien_fleet.update_fleet()
            self._check_collisons()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisons(self):
        if self.ship.check_collisons(self.alien_fleet.fleet):
            self._reset_level()

            # lose a life

        # check collisons for aliens/bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self._reset_level()

        # check collisons of bullets and aliens
        collisons = self.alien_fleet.check_collisons(self.ship.arsenal.arsenal)
        if collisons:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()


    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_Fleet()

    def _update_screen(self):
        """Updates the screen to create a background and the ship"""
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_events(self):
        """Checks events (inputs) for movement, firing lasers, and to quit game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        """Checks when the key is not being pressed down"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_keydown_events(self, event):
        """Checks when the key is pressed down"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
