import sys, pygame
from gui.Controls import Button, Background
from engine.Core import Core

menuBackground = pygame.image.load('assets/main_menu_background.png')
selectionScreenBackground = pygame.image.load('assets/selection_screen_background.png')
white = (255, 255, 255)
black = (0, 0, 0)
green = (156, 219, 151)
green_bright = (0,150,0)

class Gui():
    def __init__(self):
        self.display = pygame.display.set_mode((600,500))

class Engine():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Automated Delivery Service')
        self.view = None
        self.clock = pygame.time.Clock()
        self.fps = 120
        self.event = None
        self.objects = None
        self.display = None
        self.pressed = None
        self.handler = None

    def main_loop(self, objects):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for object in objects:
                object.update(event)
                self.handler = object.update(event)


                if self.handler == "play":
                    SelectionScreen()
                elif self.handler == "option":
                    OptionsScreen()
                elif self.handler == "core":
                    Core()
                elif self.handler == "home":
                    StartScreen()

            self.clock.tick(self.fps)
            pygame.display.flip()


    def change_view(self, view):
        self.display = pygame.display.set_mode((600,500))
        self.view = view

    def add_object(self, obj):
        self.objects.append(obj)

    def send_event(self):
        print(self.event)

class StartScreen():
    def __init__(self):
        self.display = Gui().display
        self.objects = [
            Background(self.display, menuBackground),
            Button(self.display, "START", 220, 280, 163, 48, green, green_bright, "play"),
            Button(self.display, "OPTIONS", 220, 340, 163, 48, green, green_bright, "option"),
            Button(self.display, "EXIT", 220, 400, 163, 48, green, green_bright, "exit")
        ]

        Engine().main_loop(self.objects)


class SelectionScreen():
    def __init__(self):
        self.display = Gui().display
        self.objects = [
            Background(self.display, selectionScreenBackground),
            Button(self.display, "GO", 220, 280, 163, 48, green, green_bright, "core")
        ]

        Engine().main_loop(self.objects)

class OptionsScreen():
    def __init__(self):
        self.display = Gui().display
        self.objects = [
            Button(self.display, "BACK", 220, 320, 163, 48, green, green_bright, "home")
        ]

        Engine().main_loop(self.objects)