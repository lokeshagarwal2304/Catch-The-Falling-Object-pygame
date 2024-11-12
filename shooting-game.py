import pygame
import random
import sys

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
BASKET_WIDTH = 100
BASKET_HEIGHT = 20
OBJECT_WIDTH = 30
OBJECT_HEIGHT = 30
OBJECT_FALL_SPEED = 4

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Basket class
class Basket:
    def __init__(self):
        self.rect = pygame.Rect(WINDOW_WIDTH // 2 - BASKET_WIDTH // 2, WINDOW_HEIGHT - BASKET_HEIGHT - 10, BASKET_WIDTH, BASKET_HEIGHT)

    def move(self, dx):
        self.rect.x += dx
        # Keep the basket within the window bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WINDOW_WIDTH - BASKET_WIDTH:
            self.rect.x = WINDOW_WIDTH - BASKET_WIDTH

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

# Falling object class
class FallingObject:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WINDOW_WIDTH - OBJECT_WIDTH), 0, OBJECT_WIDTH, OBJECT_HEIGHT)

    def fall(self):
        self.rect.y += OBJECT_FALL_SPEED

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

# Main function
def main():
    clock = pygame.time.Clock()
    basket = Basket()
    falling_objects = []
    score = 0
    font = pygame.font.Font(None, 36)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket.move(-10)
        if keys[pygame.K_RIGHT]:
            basket.move(10)

        # Create a new falling object randomly
        if random.randint(1, 30) == 1:  # Adjust the frequency of falling objects
            falling_objects.append(FallingObject())

        # Update falling objects
        for obj in falling_objects[:]:
            obj.fall()
            if obj.rect.y > WINDOW_HEIGHT:  # Remove object if it goes off screen
                falling_objects.remove(obj)
            if obj.rect.colliderect(basket.rect):  # Check for collision
                falling_objects.remove(obj)
                score += 1  # Increment score on catch

        # Drawing
        screen.fill(BLACK)
        basket.draw(screen)
        for obj in falling_objects:
            obj.draw(screen)

        # Display score
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
