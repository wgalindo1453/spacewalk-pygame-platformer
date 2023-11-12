import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Endless Runner")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)


# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.gravity = 1
        self.velocity = 0

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        # Prevent the player from going off the screen
        if self.rect.bottom > height:
            self.rect.bottom = height

    def jump(self):
        self.velocity = -20


# Define the obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = random.randint(0, height - self.rect.height)

    def update(self):
        self.rect.x -= 5


# Define the power-up class
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = random.randint(0, height - self.rect.height)

    def update(self):
        self.rect.x -= 5


# Create groups for sprites
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
power_ups = pygame.sprite.Group()

# Create the player
player = Player()
all_sprites.add(player)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Create new obstacles and power-ups
    if random.randrange(100) < 3:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    if random.randrange(100) < 1:
        power_up = PowerUp()
        all_sprites.add(power_up)
        power_ups.add(power_up)

    # Update sprites
    all_sprites.update()

    # Check for collisions
    if pygame.sprite.spritecollide(player, obstacles, False):
        running = False

    # Draw the game
    window.fill(BLUE)
    all_sprites.draw(window)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
