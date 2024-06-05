from abc import ABC, abstractmethod, abstractproperty
import pygame


class AbstractView(ABC):
    def __init__(self, screen, model):
        self.screen = screen
        self.clock = pygame.time.Clock()

    @abstractmethod
    def render(self):
        pass