from src.models.GameObject.Block import Block
import random
class GameBoard:
    def __init__(self):
        self.width = 4
        self.height = 4
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
        while True:
            rand_x = random.randint(0, self.width - 1)
            rand_y = random.randint(0, self.height - 1)
            if self.get(rand_x, rand_y).value == 0:
                self.get(rand_x, rand_y).value = 2
                break

    def down_press(self):
        moved = False
        for x in range(self.width):
            for y in range(self.height-2, -1, -1):
                current_block = self.get(x, y)
                if current_block.value == 0:
                    continue
                for ny in range(y+1, self.height):
                    target_block = self.get(x, ny)
                    if target_block.value == 0:
                        self.set(x, ny, current_block.value)
                        self.set(x, y, 0)
                        moved = True
                    elif target_block.value == current_block.value:
                        self.set(x, ny, current_block.value * 2)
                        self.set(x, y, 0)
                        self.score += current_block.value * 2
                        moved = True
                        break
                    else:
                        break
        if moved:
            self.spawn_block()

    def up_press(self):
        moved = False
        for x in range(self.width):
            for y in range(1, self.height):
                current_block = self.get(x, y)
                if current_block.value == 0:
                    continue
                for ny in range(y-1, -1, -1):
                    target_block = self.get(x, ny)
                    if target_block.value == 0:
                        self.set(x, ny, current_block.value)
                        self.set(x, y, 0)
                        moved = True
                    elif target_block.value == current_block.value:
                        self.set(x, ny, current_block.value * 2)
                        self.set(x, y, 0)
                        self.score += current_block.value * 2
                        moved = True
                        break
                    else:
                        break
        if moved:
            self.spawn_block()

    def right_press(self):
        moved = False
        for y in range(self.height):
            for x in range(self.width-2, -1, -1):
                current_block = self.get(x, y)
                if current_block.value == 0:
                    continue
                for nx in range(x+1, self.width):
                    target_block = self.get(nx, y)
                    if target_block.value == 0:
                        self.set(nx, y, current_block.value)
                        self.set(x, y, 0)
                        moved = True
                    elif target_block.value == current_block.value:
                        self.set(nx, y, current_block.value * 2)
                        self.set(x, y, 0)
                        self.score += current_block.value * 2
                        moved = True
                        break
                    else:
                        break
        if moved:
            self.spawn_block()

    def left_press(self):
        moved = False
        for y in range(self.height):
            for x in range(1, self.width):
                current_block = self.get(x, y)
                if current_block.value == 0:
                    continue
                for nx in range(x-1, -1, -1):
                    target_block = self.get(nx, y)
                    if target_block.value == 0:
                        self.set(nx, y, current_block.value)
                        self.set(x, y, 0)
                        moved = True
                    elif target_block.value == current_block.value:
                        self.set(nx, y, current_block.value * 2)
                        self.set(x, y, 0)
                        self.score += current_block.value * 2
                        moved = True
                        break
                    else:
                        break
        if moved:
            self.spawn_block()

