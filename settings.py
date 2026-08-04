"""
settings.py
Johan D. Ramirez Maldonado
This file stores settings that is used in the other files
Starter Code forked from: RedBeard41/alien_invasion_starter
7/31/26
"""

from pathlib import Path
class Settings:
    """Stores the settings for the other files"""

    def __init__(self):
        """
        The stored information for the files, including:
            screen size, images (including sizes), sounds, and game settings like ship and bullet speed
        """
        self.name: str = "Alien Invasion - Track 1"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"
        self.difficulty_scale = 1.1

        self.ship_file = Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        self.ship_w = 60
        self.ship_h = 40

        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast.png"
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.impact = Path.cwd() / "Assets" / "sound" / "impactSound.mp3"

        self.alien_file = Path.cwd() / "Assets" / "images" / "enemy_4.png"
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)

        self.text_color = (255, 255, 255)
        self.button_font_size = 45
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / "Assets" / "Fonts" / "Silkscreen" / "Silkscreen-Bold.ttf"

    def initialize_dynamic_settings(self):
        """Initializes settings that change throughout the game"""
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_speed = 7
        self.bullet_amount = 5
        self.bullet_w = 80
        self.bullet_h = 25

        self.fleet_speed = 2
        self.fleet_drop_speed = 40

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale

        
        