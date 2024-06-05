from src.views.main_view import AbstractView
import pygame


class SplashScreen(AbstractView):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(None, 36)

    def render(self):
        self.screen.fill((255, 255, 255))  # White background
        text = self.font.render("Splash Screen", True, (0, 0, 0))  # Black text
        text_rect = text.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
        return True
