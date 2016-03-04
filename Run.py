import pygame
from engine.Engine import GameEngine, StartScreen
from gui.Controls import *

engine = GameEngine()
engine.change_view(StartScreen())


pygame.quit()