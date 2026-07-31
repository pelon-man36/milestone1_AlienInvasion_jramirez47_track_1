class GameStats():
    """Stores everthing needed for game stats."""

    def __init__(self, ships_left):
        """Initial setup. Currently only holds lives."""
        self.ships_left = ships_left
