import pygame, sys
from random import randint as r
from gui.Controls import CreateTitle, Button, Background
from PDFInvoiceExport import InvoiceView
import json

green = (156, 219, 151)
white = (250, 250, 250)

droneImage = pygame.image.load('assets/drone.png')
houseImage = pygame.image.load('assets/house.png')
deliveryBox = pygame.image.load('assets/delivery_box.png')
backgroundImage = pygame.image.load('assets/main_background.png')

class Core():
    """
    Core of the item collection
    The selected items are being collected
    """
    def drone(self, x, y):
        self.display.blit(droneImage, (x, y))

    def box(self, x, y):
        self.display.blit(deliveryBox, (x, y))

    def __init__(self):
        self.display = pygame.display.set_mode((600,510))
        # self.display.set_caption
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Delivering items")
        self.fps = 80
        self.drone_x = 150
        self.drone_y = 150
        self.drone_x_update = 0
        self.drone_y_update = 0
        self.delivery_object_x = 150
        self.delivery_object_y = 300
        self.count = 0
        self.currentNumber = 0
        self.objects = []
        self.handler = None

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for object in self.objects:
                object.update(event)
                self.handler = object.update(event)


            self.drone_x += self.drone_x_update
            self.drone_y += self.drone_y_update
            # self.display.blit(backgroundImage, (0, 0))
            self.drone(self.drone_x, self.drone_y)
            self.box(self.delivery_object_x, self.delivery_object_y)
            if self.count == 1:
                self.currentNumber = "0"
            elif self.count == 2:
                self.currentNumber = "1"
            elif self.count == 3:
                self.currentNumber = "2"
            else:
                self.currentNumber = "3"
            CreateTitle(self.display, "Collected objects: " + self.currentNumber + "/3", 24, 40).draw()

            self.objects = [
                Background(self.display, backgroundImage),
            ]

            if self.drone_x > self.delivery_object_x:
                self.drone_x = self.drone_x - 1
                if self.drone_x == self.delivery_object_x:
                     pass
            else:
                self.drone_x = self.drone_x + 1
                if self.drone_x == self.drone_x:
                    pass
            if self.drone_y < self.delivery_object_y:
                self.drone_y = self.drone_y + 1
                if self.drone_y == self.drone_y:
                    pass
            else:
                self.drone_y = self.drone_y - 1
                if self.drone_y == self.drone_y:
                    pass

            if self.drone_x == self.delivery_object_x and self.drone_y == self.drone_y:
                self.delivery_object_x += r(100, 150)
                self.count += 1
                if self.count == 4:
                    Core2()
                    # If all of the boxes are collected the second
                    # core is called and the drone starts delivering

            pygame.display.update()
            self.clock.tick(self.fps)

    def update_fps(self, fps):
        self.fps = fps

class Core2():
    def drone(self, x, y):
        self.display.blit(droneImage, (x, y))

    def house(self, x, y):
        self.display.blit(houseImage, (x, y))

    def __init__(self):
        self.display = pygame.display.set_mode((600,510))
        # self.display.set_caption
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Delivering items")
        # self.fps = 120
        self.drone_x = 150
        self.drone_y = 150
        self.drone_x_update = 0
        self.drone_y_update = 0
        self.delivery_object_x = 150
        self.delivery_object_y = 300
        self.count = 0
        self.currentNumber = 0
        self.selectedItems = []

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_LEFT:
                #         self.drone_x_update = -5
                #     elif event.key == pygame.K_RIGHT:
                #         self.drone_x_update = 5
                #     elif event.key == pygame.K_UP:
                #         self.drone_y_update = -5
                #     elif event.key == pygame.K_DOWN:
                #         self.drone_y_update = 5
                #
                # if event.type == pygame.KEYUP:
                #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #         self.drone_x_update = 0
                #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #         self.drone_y_update = 0

            # print(event)

            self.drone_x += self.drone_x_update
            self.drone_y += self.drone_y_update
            self.display.blit(backgroundImage, (0, 0))
            self.drone(self.drone_x, self.drone_y)
            self.house(self.delivery_object_x, self.delivery_object_y)
            if self.count == 1:
                self.currentNumber = "0"
            elif self.count == 2:
                self.currentNumber = "1"
            elif self.count == 3:
                self.currentNumber = "2"
            else:
                self.currentNumber = "3"
            CreateTitle(self.display, "Delivered objects: " + self.currentNumber + "/3", 24, 40).draw()

            if self.drone_x > self.delivery_object_x:
                self.drone_x = self.drone_x - 1
                if self.drone_x == self.delivery_object_x:
                     pass
            else:
                self.drone_x = self.drone_x + 1
                if self.drone_x == self.drone_x:
                    pass
            if self.drone_y < self.delivery_object_y:
                self.drone_y = self.drone_y + 1
                if self.drone_y == self.drone_y:
                    pass
            else:
                self.drone_y = self.drone_y - 1
                if self.drone_y == self.drone_y:
                    pass

            with open('products.json') as data_file:
                data = json.load(data_file)

            for singleProduct in data[:3]:
                self.selectedItems.append(singleProduct['productTitle'])

            if self.drone_x == self.delivery_object_x and self.drone_y == self.drone_y:
                self.delivery_object_x += r(100, 150)
                self.count += 1
                if self.count == 4:
                    InvoiceView(self.selectedItems)
                # self.delivery_object_y += r(40, 80)

            pygame.display.update()
            self.clock.tick(80)
