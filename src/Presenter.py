import pygame
from src.handlers.SplashScreenHandler import SplashScreenHandler
from src.views.SplashView import SplashView
from src.View import View
from src.models.SplashViewModel import SplashViewModel
from src.models.GameObject.GameBoard import GameBoard
from src.views.GameView import GameView
from src.handlers.GameScreenHandler import GameScreenHandler

class Presenter:
    def __init__(self):
        self.view = View(self)
        splashViewModel = SplashViewModel()
        gameBoard = GameBoard()
        self.view_handler_lookup = {
            "SplashView": [SplashView(self.view.screen, splashViewModel), SplashScreenHandler(self, splashViewModel), splashViewModel],
            "GameView": [GameView(self.view.screen, gameBoard), GameScreenHandler(self, gameBoard), gameBoard]
        }
        self.current_handler = None
        self.transition_view("SplashView")

    def start(self):
        self.view.run()

    def handle_events(self):
        events = self.view.get_events()
        for event in events:
            if event.type == pygame.QUIT:
                return False
            return self.current_handler.handle_event(event)
        return True

    def update_view(self):
        self.view.render_active_screen()

    def transition_view(self, title):
        view = self.view_handler_lookup[title][0]
        handler = self.view_handler_lookup[title][1]
        self.set_current_handler(handler)
        self.view.set_active_screen(view)

    def set_current_handler(self, handler):
        self.current_handler = handler
