from src.views.AbstractView import AbstractView
import pygame
from src.models.LostModel import LostModel

class LostView(AbstractView):
    def __init__(self, screen, model: LostModel):
        super().__init__(screen, model)
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 48)
        self.model = model

    def render(self):
        self.screen.fill(self.model.colors["background_color"])  # White background

        # Render title
        title_surface = self.title_font.render(self.model.title, True, self.model.colors["title_color"])
        title_rect = title_surface.get_rect(center=(self.screen.get_width() // 2, 50))
        self.screen.blit(title_surface, title_rect)

        # Render summary of stats
        stats_start_y = 100
        for i, stat in enumerate(self.model.stats):
            stat_surface = self.font.render(stat, True, self.model.colors["text_color"])
            stat_rect = stat_surface.get_rect(center=(self.screen.get_width() // 2, stats_start_y + i * 40))
            self.screen.blit(stat_surface, stat_rect)

        # Render dialogue options
        options_start_y = stats_start_y + len(self.model.stats) * 40 + 20
        total_options = len(self.model.dialogue_options)
        for i, option in enumerate(self.model.dialogue_options):
            color = self.model.colors["highlight_color"] if option["isSelected"] else self.model.colors["text_color"]
            option_surface = self.font.render(option["text"], True, color)
            option_rect = option_surface.get_rect(center=(self.screen.get_width() // 2, options_start_y + i * 40))
            self.screen.blit(option_surface, option_rect)

        pygame.display.flip()
