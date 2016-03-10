import pygame
from engine.engine import Engine, StartScreen

engine = Engine() # calling the engine
engine.change_view(StartScreen()) # calling the class for the menu screen


pygame.quit()