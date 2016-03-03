import pygame
from gui.Controls import *
from engine.Engine import *

green = (156, 219, 151)
green_bright = (0,150,0)

class StartScreen():
    def __init__(self):
        self.objects = [
            Background(GameEngine().display),
            Button(GameEngine().display,"START",220,280,163,48,green,white,"play"),
            Button(GameEngine().display,"OPTIONS",220,340,163,48,green,black,"play"),
            Button(GameEngine().display,"EXIT",220,400,163,48,green,black,"play")
        ]

        for object in self.objects:
            object.update()


    def add_object(self, obj):
        self.objects.append(obj)

class SelectionScreen():
    def __init__(self):
        pass