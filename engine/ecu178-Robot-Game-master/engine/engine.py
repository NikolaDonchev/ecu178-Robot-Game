import sys, pygame
from gui.Controls import *
from engine import Core
import json
from pprint import pprint

menuBackground = pygame.image.load('assets/main_menu_background.png')
selectionScreenBackground = pygame.image.load('assets/selection_screen_background.png')
optionsBackground = pygame.image.load('assets/options_background.png')
white = (250, 250, 250)
black = (107, 107, 107)
green = (156, 219, 151)
green_bright = (0,150,0)

class Gui():
    def __init__(self):
        self.display = pygame.display.set_mode((600,510))

class Engine():
    def __init__(self):
        pygame.init()
        self.view = None
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.event = None
        self.selectedItems = []

    def main_loop(self, objects):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for object in objects:
                object.update(event, self.selectedItems)
                self.handler = object.update(event, self.selectedItems)

                if self.handler == "play":
                    SelectionScreen()
                elif self.handler == "option":
                    OptionsScreen()
                elif self.handler == "core":
                    Core()
                elif self.handler == "home":
                    StartScreen()
                elif self.handler == "exit":
                    pygame.QUIT
                    sys.exit()

                if self.handler == "first":
                    self.change_stage("firstCheck")
                elif self.handler == "second":
                        self.change_stage("secondCheck")
                elif self.handler == "third":
                        self.change_stage("thirdCheck")
                elif self.handler == "fourth":
                        self.change_stage("fourthCheck")
                elif self.handler == "fifth":
                        self.change_stage("fifthCheck")
                elif self.handler == "sixth":
                        self.change_stage("sixthCheck")
                elif self.handler == "seventh":
                        self.change_stage("seventhCheck")
                elif self.handler == "eighth":
                        self.change_stage("eigthCheck")
                elif self.handler == "nineth":
                        self.change_stage("ninethCheck")
            print(self.selectedItems)

            self.clock.tick(self.fps)
            pygame.display.flip()
    def bubble_sort(self,unsorted,sorted,selectedItems,tempArray):
        unsorted[selectedItems] == True
        sorted[selectedItems] == False
        tempArray()

    def change_view(self, view):
        self.display = pygame.display.set_mode((600,500))
        self.view = view

    def add_object(self, obj):
        self.objects.append(obj)

    def change_stage(self, obj):
        if len(self.selectedItems) == 0:
            self.selectedItems.append(obj)
        if self.linearSearch(obj, self.selectedItems) != True:
            self.selectedItems.append(obj)

    def linearSearch(self, item, array):
        found = False
        position = 0
        while position < len(array) and not found:
            if array[position] == item:
                found = True
            position = position + 1
        return (found)

    def send_event(self):
        print(self.event)

class StartScreen():
    def __init__(self):
        self.display = Gui().display
        pygame.display.set_caption('Automated Delivery Service')
        self.objects = [
            Background(self.display, menuBackground), # Setting the background
            Button(self.display, "START", 220, 280, 163, 48, green, green_bright, "play"),
            Button(self.display, "OPTIONS", 220, 340, 163, 48, green, green_bright, "option"),
            Button(self.display, "EXIT", 220, 400, 163, 48, green, green_bright, "exit"),
        ]
        # Adding the elements to the "object" array

        Engine().main_loop(self.objects)
        # running the main loop and giving the array as parameter if the mail_loop function from the Engine class


class SelectionScreen():

    def __init__(self):
        self.display = Gui().display
        pygame.display.set_caption("Select items for delivery")
        self.selectedItems = [] # empty array for the selected items
        self.numberOfSelectedItems = 0
        self.checkboxes = []
        self.objects = [
            Background(self.display, selectionScreenBackground),
            CreateTitle(self.display, "Pick three items for delivery", 24, 40), # Title from the header
            CreateRect(self.display, white, 124, 340, 452, 105), # creating rectangle as background for the sorting container
            CreateRect(self.display, white, 552, 41, 24, 454), # creating another container for "Back" and "Go" buttons
            Button(self.display, "GO", 440, 459, 120, 30, green, green_bright, "core"),
            Button(self.display, "BACK", 40, 459, 120, 30, green, green_bright, "home")
        ]

        with open('products.json') as data_file:
            data = json.load(data_file)

        for singleProduct in data:
            self.add_checkbox(CheckBox(self.display, singleProduct['productTitle'], singleProduct['productPrice'], singleProduct['productWeight'], singleProduct['x_pos'], singleProduct['y_pos'], singleProduct['productAction']))

        allObjects = self.objects + self.checkboxes # merging the objects array with the main components and the array full of checkboxes

        Engine().main_loop(allObjects)

    def add_checkbox(self, checkbox):
        self.checkboxes.append(checkbox)

class OptionsScreen():
    def __init__(self):
        self.display = Gui().display
        self.objects = [
            Background(self.display, optionsBackground),
           #Button(self.display, "MUSIC", 220, 280, 163, 48, green, green_bright, ""), # individual feature
            #Button(self.display, "ITEMS", 220, 340, 163, 48, green, green_bright, ""), # individual feature
            #Button(self.display, "BACK", 220, 400, 163, 48, green, green_bright, "home")
        ]

        Engine().main_loop(self.objects)