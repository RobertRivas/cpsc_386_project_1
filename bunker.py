
import pygame


from pygame.sprite import Sprite


class Bunker(Sprite):

    def __init__(self, ai_settings, screen):
        super(Bunker, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/bunker block-1.png(1).png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.rect.left
        self.rect.y = self.rect.bottom + 250

    def blitme(self):
        """Draw the bunker at its current location."""
        self.screen.blit(self.image, self.rect)
