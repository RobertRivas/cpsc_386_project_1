
import pygame


class Settings:

    """A class to store all settings for alien invasion."""

    def __init__(self):
        """initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        pygame.mixer.music.load('audio/spaceinvaders1 3.mpeg')
        self.shoot = pygame.mixer.Sound('audio/shoot.wav')
        self.explosion = pygame.mixer.Sound('audio/explosion.wav')

        # Ship settings
        self.ship_limit = 3
        # Bullet Settings

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Alien settings

        self.fleet_drop_speed = 10
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        # fleet_direction of 1 represents right; -1 left.
        self.fleet_direction = 1

        self.bunkers = 3

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 8
        self.alien_speed_factor = 1

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
