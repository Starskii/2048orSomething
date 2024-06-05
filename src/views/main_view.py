from abc import ABC, abstractmethod
import pygame


class AbstractView(ABC):
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def handle_events(self):
        pass
