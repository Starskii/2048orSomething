import pygame
from src.views.SplashView import SplashView


class View:
    def __init__(self, presenter):
        pygame.init()
        self.presenter = presenter
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.active_screen = None
        self.FRAME_CAP = 60  # Updated to a more standard frame cap

    def run(self):
        running = True
        while running:
            self.render_active_screen()
            running = self.presenter.handle_events()
            self.clock.tick(1000/self.FRAME_CAP)

    def get_events(self):
        return pygame.event.get()

    def render_active_screen(self):
        self.active_screen.render()
        self.clock.tick(self.FRAME_CAP)

    def set_active_screen(self, screen):
        self.active_screen = screen