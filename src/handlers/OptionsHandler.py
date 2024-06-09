import pygame
from handlers.AbstractHandler import AbstractHandler


class OptionsHandler(AbstractHandler):
    def __init__(self, presenter, model):
        self.presenter = presenter
        self.model = model

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.model.increment_selection()
            elif event.key == pygame.K_UP:
                self.model.decrement_selection()
            elif event.key == pygame.K_RIGHT:
                self.model.increment_selected()
            elif event.key == pygame.K_LEFT:
                self.model.decrement_selected()
        return True