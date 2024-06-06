import pygame
from src.handlers.SplashScreenHandler import SplashScreenHandler
from src.views.SplashView import SplashView
from src.View import View
from src.models.SplashViewModel import SplashViewModel
from src.models.GameObject.GameBoard import GameBoard
from src.views.GameView import GameView
from src.handlers.GameScreenHandler import GameScreenHandler
from src.views.OptionsView import OptionsView
from src.handlers.OptionsHandler import OptionsHandler
from src.models.OptionsModel import OptionsModel

class Presenter:
    def __init__(self):
        self.view = View(self)
        splashViewModel = SplashViewModel()
        self.optionsModel = OptionsModel()
        gameBoard = GameBoard(self.optionsModel.width, self.optionsModel.height, self.optionsModel.spawn_count)
        self.view_handler_lookup = {
            "SplashView": [SplashView(self.view.screen, splashViewModel), SplashScreenHandler(self, splashViewModel), splashViewModel],
            "GameView": [GameView(self.view.screen, gameBoard), GameScreenHandler(self, gameBoard), gameBoard],
            "OptionsView": [OptionsView(self.view.screen, self.optionsModel), OptionsHandler(self, self.optionsModel), self.optionsModel]
        }
        self.current_handler = None
        self.transition_view("SplashView")

    def start(self):
        self.view.run()

    def handle_events(self):
        for event in pygame.event.get():
            # Handle Global Events
            if event.type == 32787:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.transition_view("SplashView")
            # Handle screen specific events
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

    def start_new_game(self):
        print("got here")
        gameBoard = GameBoard(self.optionsModel.width, self.optionsModel.height, self.optionsModel.spawn_count)
        self.view_handler_lookup["GameView"] = [GameView(self.view.screen, gameBoard), GameScreenHandler(self, gameBoard), gameBoard]
        self.transition_view("GameView")
