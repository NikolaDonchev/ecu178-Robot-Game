import pygame
<<<<<<< HEAD
from engine.Engine import GameEngine, StartScreen
from gui.Controls import *
=======
from engine.Engine import GameEngine
from views.Views import StartScreen

# this will be moved to components soon
mainBackground2 = pygame.image.load('assets/main_menu_background.png')
blankImage = pygame.image.load('selection_screen.png')
>>>>>>> origin/master

engine = GameEngine()
engine.change_view(StartScreen())

pygame.quit()
