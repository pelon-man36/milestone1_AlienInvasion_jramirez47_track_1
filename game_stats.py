"""
game_stats.py
Johan D. Ramirez Maldonado
This file stores the games stats, like score, max score and hi score.
Starter Code forked from: RedBeard41/alien_invasion_starter
8/6/26
"""
# from pathlib import Path
import json
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """Stores everthing needed for game stats."""

    def __init__(self, game: "AlienInvasion"):
        """Initial setup."""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()

        self.reset_stats()

    def init_saved_scores(self):
        """Saves the score during play"""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get("hi_score", 0)
        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        """Saves the scores, updating hi score if a new hi score was reached"""
        scores = {
            "hi_score": self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")

    def reset_stats(self):
        """Resets score, level, and lives"""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """Updates the scores"""
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()


    def _update_max_score(self):
        """Updates max score"""
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f"Max: {self.max_score}")

    def _update_hi_score(self):
        """Updates hi score"""
        if self.score > self.hi_score:
            self.hi_score = self.score
        # print(f"Hi: {self.hi_score}")

    def _update_score(self, collisions):
        """Updates score"""
        for alien in collisions.values():
            self.score += self.settings.alien_points
        # print(f"Basic: {self.score}")

    def update_level(self):
        """Updates the level"""
        self.level += 1
        # print(f"Level: {self.level}")
