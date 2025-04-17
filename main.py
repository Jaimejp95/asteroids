import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

print("File is running!")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    running = True

    # New game loop
    while running:
        dt = clock.tick(60) / 1000
    
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # Update game state using group
        updatable.update(dt)
    
        # Draw everything using group
        screen.fill((0, 0, 0))
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
    
if __name__ == "__main__":
    main()