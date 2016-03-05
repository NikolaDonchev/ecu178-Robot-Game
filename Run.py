import pygame
from engine.Engine import GameEngine, StartScreen

engine = GameEngine()
engine.change_view(StartScreen())


pygame.quit()