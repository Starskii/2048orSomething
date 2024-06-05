import pygame
from controller import Controller


class Presenter:
    def __init__(self):
        self.controller = Controller()

    def start(self):
        self.controller.run()
