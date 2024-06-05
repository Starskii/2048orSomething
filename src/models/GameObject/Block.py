
class Block:
    def __init__(self):
        self.value = 0
        self.combined = False

    def can_combine(self, block):
        return self.value == block.value and self.value != 0

    def update_value(self, value):
        self.value = 0
