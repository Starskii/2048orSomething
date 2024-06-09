class LostModel:
    def __init__(self, prev_game_board):
        self.title = "Game Over!"
        self.stats = ["Score: " + str(prev_game_board.score),
                      "Moves: " + str(prev_game_board.turns),
                      "Board Height: " + str(prev_game_board.height),
                      "Board Width: " + str(prev_game_board.width),
                      "Spawn Rate: " + str(prev_game_board.spawn_count)]
        self.dialogue_options = [
            {"text": "New Game", "isSelected": True},
            {"text": "Options", "isSelected": False},
            {"text": "Quit", "isSelected": False}
        ]

        self.colors = {
            "title_color": (255, 255, 255),
            "background_color": (0, 0, 0),
            "text_color": (255, 255, 255),
            "highlight_color": (255, 0, 0)
        }
        self.current_selection = 0

    def increment_selection(self):
        self.dialogue_options[self.current_selection]["isSelected"] = False
        self.current_selection = (self.current_selection + 1) % len(self.dialogue_options)
        self.dialogue_options[self.current_selection]["isSelected"] = True

    def decrement_selection(self):
        self.dialogue_options[self.current_selection]["isSelected"] = False
        self.current_selection = (self.current_selection - 1) % len(self.dialogue_options)
        self.dialogue_options[self.current_selection]["isSelected"] = True