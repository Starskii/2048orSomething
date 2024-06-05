import pygame
from views.splash_view import SplashScreen


class Controller:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.splash_screen = SplashScreen(self.screen)
        self.clock = pygame.time.Clock()
        self.active_screen = self.splash_screen
        self.FRAME_CAP = 1
    def run(self):
        running = True
        while running:
            self.active_screen.render()
            if not running:
                break
            running = self.active_screen.handle_events()
            self.clock.tick(1000/self.FRAME_CAP)
