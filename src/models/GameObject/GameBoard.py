from src.models.GameObject.Block import Block
import random


class GameBoard:
    def __init__(self, width, height, spawn_count):
        self.width = width
        self.height = height
        self.spawn_count = spawn_count
        self.board = [[Block() for _ in range(self.width)] for _ in range(self.height)]
        self.score = 0
        self.spawn_block()

    def get(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.board[y][x]
        else:
            raise IndexError("Index out of bounds")

    def set(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.board[y][x].value = value
        else:
            raise IndexError("Index out of bounds")

    def spawn_block(self):
        spawned = 0
        while spawned < self.spawn_count:
            rand_x = random.randint(0, self.width - 1)
            rand_y = random.randint(0, self.height - 1)
            if self.get(rand_x, rand_y).value == 0:
                self.get(rand_x, rand_y).value = 2
                spawned += 1

    def down_press(self):
        width_max = self.width-1
        width_min = 0

        height_max = self.height-1
        height_min = 0

        moved = False
        for y in range(height_max, height_min - 1, -1):
            for x in range(width_min, width_max + 1):
                target_block = self.get(x, y)
                starting_y = y-1
                for yn in range(starting_y, height_min - 1, -1):
                    current_block = self.get(x, yn)
                    if target_block.value == 0 and current_block.value == 0:
                        continue
                    elif target_block.value == 0 and current_block.value > 0:
                        target_block.value = current_block.value
                        current_block.value = 0
                        moved = True
                        continue
                    elif target_block.value == current_block.value:
                        target_block.value += current_block.value
                        self.score += current_block.value
                        current_block.value = 0
                        moved = True
                        break
        if moved:
            self.spawn_block()

    def up_press(self):
        width_max = self.width - 1
        width_min = 0

        height_max = self.height - 1
        height_min = 0

        moved = False
        for y in range(height_min, height_max + 1):
            for x in range(width_min, width_max + 1):
                target_block = self.get(x, y)
                starting_y = y + 1
                for yn in range(starting_y, height_max + 1):
                    current_block = self.get(x, yn)
                    if target_block.value == 0 and current_block.value == 0:
                        continue
                    elif target_block.value == 0 and current_block.value > 0:
                        target_block.value = current_block.value
                        current_block.value = 0
                        moved = True
                        continue
                    elif target_block.value == current_block.value:
                        target_block.value += current_block.value
                        self.score += current_block.value
                        current_block.value = 0
                        moved = True
                        break
        if moved:
            self.spawn_block()

    def right_press(self):
        width_max = self.width - 1
        width_min = 0

        height_max = self.height - 1
        height_min = 0

        moved = False
        for x in range(width_max, width_min - 1, -1):
            for y in range(height_min, height_max + 1):
                target_block = self.get(x, y)
                starting_x = x - 1
                for xn in range(starting_x, width_min - 1, -1):
                    current_block = self.get(xn, y)
                    if target_block.value == 0 and current_block.value == 0:
                        continue
                    elif target_block.value == 0 and current_block.value > 0:
                        target_block.value = current_block.value
                        current_block.value = 0
                        moved = True
                        continue
                    elif target_block.value == current_block.value:
                        target_block.value += current_block.value
                        self.score += current_block.value
                        current_block.value = 0
                        moved = True
                        break
        if moved:
            self.spawn_block()

    def left_press(self):
        width_max = self.width - 1
        width_min = 0

        height_max = self.height - 1
        height_min = 0

        moved = False
        for x in range(width_min, width_max + 1):
            for y in range(height_min, height_max + 1):
                target_block = self.get(x, y)
                starting_x = x + 1
                for xn in range(starting_x, width_max + 1):
                    current_block = self.get(xn, y)
                    if target_block.value == 0 and current_block.value == 0:
                        continue
                    elif target_block.value == 0 and current_block.value > 0:
                        target_block.value = current_block.value
                        current_block.value = 0
                        moved = True
                        continue
                    elif target_block.value == current_block.value:
                        target_block.value += current_block.value
                        self.score += current_block.value
                        current_block.value = 0
                        moved = True
                        break
        if moved:
            self.spawn_block()


