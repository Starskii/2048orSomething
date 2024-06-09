import pygame
from views.AbstractView import AbstractView


class GameView(AbstractView):
    def __init__(self, screen, model):
        self.game_board = model
        self.score_font = pygame.font.SysFont(None, 36)
        self.screen = screen
        pygame.display.set_caption("2048 Game")
        self.margin_top = 100  # Space at the top for the score
        self.calculate_block_size()

    def calculate_block_size(self):
        self.block_size = min(self.screen.get_width() // self.game_board.width, (self.screen.get_height() - self.margin_top) // self.game_board.height)
        self.board_width = self.block_size * self.game_board.width
        self.board_height = self.block_size * self.game_board.height
        self.board_x = (self.screen.get_width() - self.board_width) // 2
        self.board_y = self.margin_top

    def draw_board(self):
        self.screen.fill((255, 255, 255))  # Fill screen with white color

        # Draw blocks
        for x in range(self.game_board.width):
            for y in range(self.game_board.height):
                block = self.game_board.get(x, y)
                if block.value != 0:
                    color = self.game_board.block_colors[block.value]  # Adjust color based on block value
                    rect = pygame.Rect(
                        self.board_x + x * self.block_size,
                        self.board_y + y * self.block_size,
                        self.block_size,
                        self.block_size
                    )
                    pygame.draw.rect(self.screen, color, rect)
                    text_surface = self.score_font.render(str(block.value), True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=rect.center)
                    self.screen.blit(text_surface, text_rect)

        # Draw grid lines
        for x in range(self.game_board.width):
            for y in range(self.game_board.height):
                rect = pygame.Rect(
                    self.board_x + x * self.block_size,
                    self.board_y + y * self.block_size,
                    self.block_size,
                    self.block_size
                )
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 3)  # Draw black grid lines

    def draw_score(self):
        score_text = self.score_font.render("Score: " + str(self.game_board.score), True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))  # Adjust position as needed

    def render(self):
        self.calculate_block_size()
        self.draw_board()
        self.draw_score()
        pygame.display.flip()


