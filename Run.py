import pygame
from engine.Engine import GameEngine
from views.Views import StartScreen

# this will be moved to components soon
mainBackground2 = pygame.image.load('assets/main_menu_background.png')

engine = GameEngine()
engine.change_view(StartScreen(), mainBackground2)
engine.main_loop()

pygame.quit()