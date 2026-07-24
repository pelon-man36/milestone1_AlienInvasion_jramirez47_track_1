"""
settings.py
Johan D. Ramirez Maldonado
This file stores settings that is used in the other files
Starter Code forked from: RedBeard41/alien_invasion_starter
7/24/26
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

        self.ship_file = Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        self.ship_w = 60
        self.ship_h = 40
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast.png"
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.bullet_speed = 7
        self.bullet_w = 80
        self.bullet_h = 25
        self.bullet_amount = 5
        