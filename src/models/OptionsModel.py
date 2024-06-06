class OptionsModel:
    def __init__(self):
        self.colors = {
            "background_color": (0, 0, 0),
            "text_color": (255, 255, 255),
            "highlight_color": (255, 0, 0)
        }

        self.width = 4
        self.height = 4
        self.spawn_count = 1

        self.dialogue_options = [
            {"text": "Board Width " + str(self.width), "isSelected": True, "property": "width"},
            {"text": "Board Height " + str(self.height), "isSelected": False, "property": "height"},
            {"text": "Block Spawn Count " + str(self.spawn_count), "isSelected": False, "property": "spawn_count"}
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

    def increment_selected(self):
        for option in self.dialogue_options:
            if option['isSelected']:
                if option["property"] == "width":
                    self.width += 1
                elif option["property"] == "height":
                    self.height += 1
                elif option["property"] == "spawn_count":
                    self.spawn_count += 1
        self.update_dialogues()

    def decrement_selected(self):
        for option in self.dialogue_options:
            if option['isSelected']:
                if option["property"] == "width":
                    self.width -= 1
                elif option["property"] == "height":
                    self.height -= 1
                elif option["property"] == "spawn_count":
                    self.spawn_count -= 1
        self.update_dialogues()

    def update_dialogues(self):
        for option in self.dialogue_options:
            if option["property"] == "width":
                option["text"] = "Board Width " + str(self.width)
            elif option["property"] == "height":
                option["text"] = "Board Height " + str(self.height)
            elif option["property"] == "spawn_count":
                option["text"] = "Block Spawn Count " + str(self.spawn_count)
