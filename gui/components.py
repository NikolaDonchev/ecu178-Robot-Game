import pygame

# Images
droneImage = pygame.image.load('assets/drone-512.png')
mainBackground = pygame.image.load('assets/main_menu_background.png')
gameImage = pygame.image.load('Delivering_objects.png')
blankImage = pygame.image.load('selection_screen.png')

x = 0
y = 0


def load_image(game, image):
    game.blit(image, (0, 0))


def load_drone(game, image, x, y):
    game.blit(image, (x, y))