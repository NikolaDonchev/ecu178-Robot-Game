import pygame
from engine.Engine import Engine, StartScreen

engine = Engine()
engine.change_view(StartScreen())


pygame.quit()