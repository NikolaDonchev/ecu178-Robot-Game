import pygame
from engine.Engine import Engine, StartScreen

engine = Engine() # calling the engine
engine.change_view(StartScreen()) # calling the class for the menu screen


pygame.quit()