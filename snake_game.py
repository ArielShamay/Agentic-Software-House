
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
SCORE_FONT = pygame.font.SysFont('Arial', 24)

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.food = self.generate_food()
        self.score = 0
        self.direction = 'right'

    def generate_food(self):
        while True:
            x = random.randint(0, WIDTH - 20) // 20 * 20
            y = random.randint(0, HEIGHT - 20) // 20 * 20
            food = (x, y)
            if food not in self.snake:
                return food

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != 'down':
                    self.direction = 'up'
                elif event.key == pygame.K_DOWN and self.direction != 'up':
                    self.direction = 'down'
                elif event.key == pygame.K_LEFT and self.direction != 'right':
                    self.direction = 'left'
                elif event.key == pygame.K_RIGHT and self.direction != 'left':
                    self.direction = 'right'

    def update_game_state(self):
        head = self.snake[-1]
        if self.direction == 'up':
            new_head = (head[0], head[1] - 20)
        elif self.direction == 'down':
            new_head = (head[0], head[1] + 20)
        elif self.direction == 'left':
            new_head = (head[0] - 20, head[1])
        elif self.direction == 'right':
            new_head = (head[0] + 20, head[1])

        self.snake.append(new_head)
        if self.food == new_head:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop(0)

        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in self.snake[:-1]):
            pygame.quit()
            sys.exit()

    def draw_game(self):
        self.screen.fill(BACKGROUND_COLOR)
        for pos in self.snake:
            pygame.draw.rect(self.screen, SNAKE_COLOR, (pos[0], pos[1], 20, 20))
        pygame.draw.rect(self.screen, FOOD_COLOR, (self.food[0], self.food[1], 20, 20))
        score_text = SCORE_FONT.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.update()

    def run(self):
        while True:
            self.handle_events()
            self.update_game_state()
            self.draw_game()
            self.clock.tick(10)

if __name__ == '__main__':
    game = SnakeGame()
    game.run()