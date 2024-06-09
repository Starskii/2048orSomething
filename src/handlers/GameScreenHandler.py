import pygame
from src.handlers.AbstractHandler import AbstractHandler


class GameScreenHandler(AbstractHandler):
    def __init__(self, presenter, model):
        self.presenter = presenter
        self.model = model

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.model.down_press()
            elif event.key == pygame.K_UP:
                self.model.up_press()
            elif event.key == pygame.K_RIGHT:
                self.model.right_press()
            elif event.key == pygame.K_LEFT:
                self.model.left_press()
        if self.model.has_lost:
            self.presenter.transition_view("Lost")
        return True
