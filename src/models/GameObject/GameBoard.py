from src.models.GameObject.Block import Block
import random


class GameBoard:
    def __init__(self, width, height, spawn_count):
        self.width = width
        self.height = height
        self.spawn_count = spawn_count
        self.board = [[Block() for _ in range(self.width)] for _ in range(self.height)]
        self.score = 0
        self.spawn_variants = {
            2: 9,
            4: 1
        }
        self.spawn_block()
        self.spawn_block()
        self.block_colors = {
            2: (233, 86, 86),
            4: (233, 86, 174),
            8: (159, 86, 232),
            16: (86, 110, 233),
            32: (86, 204, 233),
            64: (86, 233, 184),
            128: (86, 233, 120),
            256: (120, 233, 86),
            512: (194, 233, 86),
            1024: (233, 204, 86),
            2048: (233, 154, 86),
            4096: (142, 115, 92),
            8192: (123, 139, 57),
            16384: (57, 139, 82),
            32768: (57, 76, 139),
            65536: (123, 57, 139),
            131072: (71, 21, 58),
        }

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
        probability_total = sum(self.spawn_variants.values())
        rand_value = random.randint(1, probability_total)
        current_value = 0
        block_value = 2
        for k in self.spawn_variants.keys():
            current_value += self.spawn_variants[k]
            if current_value <= rand_value:
                block_value = k
        spawned = 0

        while spawned < self.spawn_count:
            rand_x = random.randint(0, self.width - 1)
            rand_y = random.randint(0, self.height - 1)
            if self.get(rand_x, rand_y).value == 0:
                self.get(rand_x, rand_y).value = block_value
                print(block_value)
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
                    elif target_block.value != current_block.value and current_block.value != 0:
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
                    elif target_block.value != current_block.value and current_block.value != 0:
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
                    elif target_block.value != current_block.value and current_block.value != 0:
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
                    elif target_block.value != current_block.value and current_block.value != 0:
                        break
        if moved:
            self.spawn_block()
