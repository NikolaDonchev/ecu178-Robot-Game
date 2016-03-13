#Mario Kostadinov's Individual Feature
import sys
from engine.engine import *
from engine.Core import *

musicOn = False

class Engine():


    def __init__(self):
        pygame.init()
        self.view = None
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.event = None
        self.selectedItems = []
        if musicOn:
            self.music = pygame.mixer.music.load('music.mp3')
            self.play_music = pygame.mixer.music.play(0, 0.0)
            self.music_volume = pygame.mixer.music_set_volume(0.5)

    def main_loop(self, objects): #The Main game loop, everything here takes place into the game
        while 1:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for object in objects:
                object.update(event, self.selectedItems)
                self.handler = object.update(event, self.selectedItems)


                if self.handler == "OnOff":
                    print("MUSIC")
                    global musicOn
                    musicOn = True
                elif self.handler == "+":
                    self.music_volume = pygame.mixer.music_set_volume(1.0)
                elif self.handler == "-":
                    self.music_volume = pygame.mixer.music_set_volume(0.1)
                elif self.handler == "option":
                    OptionsScreen()

class MusicLoop():

    def __init__(self):
        self.display = Gui().display
        self.objects = [
            Background(self.display, menuBackground),
            Button(self.display, "Music ON/OFF", 220, 280, 163, 48, green, green_bright, "OnOff"),
            Button(self.display, "Volume +", 220, 340, 80, 48, green, green_bright, "+"),
            Button(self.display, "Valume -", 303, 340, 80, 48, green, green_bright, "-"),
            Button(self.display, "BACK", 220, 400, 163, 48, green, green_bright, "option")
        ]

        Engine().main_loop(self.objects)
