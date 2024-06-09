from views.AbstractView import AbstractView
import pygame
import random
from models.SplashViewModel import SplashViewModel

class SplashView(AbstractView):
    def __init__(self, screen, model):
        super().__init__(screen, model)
        self.font = pygame.font.Font(None, 36)
        self.model = model

    def render(self):
        self.screen.fill((255, 255, 255))  # White background
        for dialogue_option in self.model.dialogue_options:
            self.screen.fill(self.model.colors["background_color"])
            total_options = len(self.model.dialogue_options)
            for i, option in enumerate(self.model.dialogue_options):
                color = self.model.colors["highlight_color"] if option["isSelected"] else self.model.colors["text_color"]
                text_surface = self.font.render(option["text"], True, color)
                text_rect = text_surface.get_rect(center=((self.screen.get_width() // 2), (self.screen.get_height() // 2) - (total_options // 2 - i) * 40))
                self.screen.blit(text_surface, text_rect)
        pygame.display.flip()

