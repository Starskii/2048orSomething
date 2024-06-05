
class SplashViewModel:
    def __init__(self):
        self.title = "Capitalist Maximust"
        self.colors = {
            "background_color": (0, 0, 0),
            "text_color": (255, 255, 255),
            "highlight_color": (255, 0, 0)
        }
        self.dialogue_options = [
            {"text": "Start Game", "isSelected": True},
            {"text": "Options", "isSelected": False},
            {"text": "Quit", "isSelected": False}
        ]
        self.current_selection = 0

    def increment_selection(self):
        self.dialogue_options[self.current_selection]["isSelected"] = False
        self.current_selection = (self.current_selection + 1) % len(self.dialogue_options)
        self.dialogue_options[self.current_selection]["isSelected"] = True

    def decrement_selection(self):
        self.dialogue_options[self.current_selection]["isSelected"] = False
        self.current_selection = (self.current_selection - 1) % len(self.dialogue_options)
        self.dialogue_options[self.current_selection]["isSelected"] = True
