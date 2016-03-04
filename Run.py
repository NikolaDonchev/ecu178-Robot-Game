import pygame
from engine.Engine import GameEngine
from views.Views import StartScreen

# this will be moved to components soon
mainBackground2 = pygame.image.load('assets/main_menu_background.png')
blankImage = pygame.image.load('selection_screen.png')
engine = GameEngine()
engine.change_view(StartScreen())
engine.main_loop()

pygame.quit()
