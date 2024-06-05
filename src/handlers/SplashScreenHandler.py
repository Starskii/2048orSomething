import pygame
from src.handlers.AbstractHandler import AbstractHandler


class SplashScreenHandler(AbstractHandler):
    def __init__(self, presenter, model):
        self.presenter = presenter
        self.model = model

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.model.increment_selection()
            elif event.key == pygame.K_UP:
                self.model.decrement_selection()
            elif event.key == pygame.K_RETURN:
                selected_option = self.model.dialogue_options[self.model.current_selection]
                if selected_option["text"] == "Quit":
                    return False
                elif selected_option["text"] == "Start Game":
                    self.presenter.transition_view("GameView")
                    return True
        return True
