import sys, pygame
# from gui.Controls import Button, Background


white = (255, 255, 255)
black = (0, 0, 0)
green = (156, 219, 151)
green_bright = (0,150,0)

class Gui():
    def __init__(self):
        self.display = pygame.display.set_mode((600,500))

class GameEngine():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Automated Delivery Service')
        self.view = None
        self.clock = pygame.time.Clock()
        self.fps = 5
        self.event = None
        self.objects = None
        self.display = Gui().display
        self.pressed = None

    def main_loop(self, objects):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for object in objects:
                object.update(event)

            self.clock.tick(self.fps)
            pygame.display.flip()


    def change_view(self, view):
        self.view = view

    def add_object(self, obj):
        self.objects.append(obj)

    def send_event(self):
        print(self.event)

class StartScreen(Gui):
    def __init__(self):
        self.display = Gui().display
        self.pressed = None
        self.objects = [
            Background(self.display),
            Button(self.display, "START", 220, 280, 163, 48, green, green_bright, "play"),
            Button(self.display, "OPTIONS", 220, 340, 163, 48, green, green_bright, "option"),
            Button(self.display, "EXIT", 220, 400, 163, 48, green, green_bright, "exit")
        ]


        # print(Button().pressed)
        # print(.pressed)

        GameEngine().main_loop(self.objects)


class SelectionScreen(Gui):
    def __init__(self):
        self.display = Gui().display
        self.objects = [
            Button(self.display, "START", 220, 280, 163, 48, green, green_bright, "play")
        ]

        GameEngine().main_loop(self.objects)