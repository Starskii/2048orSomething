import pygame
from handlers.SplashScreenHandler import SplashScreenHandler
from views.SplashView import SplashView
from View import View
from models.SplashViewModel import SplashViewModel
from models.GameObject.GameBoard import GameBoard
from views.GameView import GameView
from handlers.GameScreenHandler import GameScreenHandler
from views.OptionsView import OptionsView
from handlers.OptionsHandler import OptionsHandler
from models.OptionsModel import OptionsModel
from models.LostModel import LostModel
from views.LostView import LostView
from handlers.LostHandler import LostHandler
class Presenter:
    def __init__(self):
        self.view = View(self)
        splashViewModel = SplashViewModel()
        self.optionsModel = OptionsModel()
        self.gameBoard = GameBoard(self.optionsModel.width, self.optionsModel.height, self.optionsModel.spawn_count)
        self.view_handler_lookup = {
            "SplashView": [SplashView(self.view.screen, splashViewModel), SplashScreenHandler(self, splashViewModel), splashViewModel],
            "GameView": [GameView(self.view.screen, self.gameBoard), GameScreenHandler(self, self.gameBoard), self.gameBoard],
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
        if title == "Lost":
            model = LostModel(self.gameBoard)
            view = LostView(self.view.screen, model)
            handler = LostHandler(self, model)
            self.current_handler = handler
            self.view.set_active_screen(view)
        else:
            view = self.view_handler_lookup[title][0]
            handler = self.view_handler_lookup[title][1]
            self.set_current_handler(handler)
            self.view.set_active_screen(view)

    def set_current_handler(self, handler):
        self.current_handler = handler

    def start_new_game(self):
        self.gameBoard = GameBoard(self.optionsModel.width, self.optionsModel.height, self.optionsModel.spawn_count)
        self.view_handler_lookup["GameView"] = [GameView(self.view.screen, self.gameBoard), GameScreenHandler(self, self.gameBoard), self.gameBoard]
        self.transition_view("GameView")
