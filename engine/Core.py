import pygame, sys
from random import randint as r

droneImage = pygame.image.load('assets/drone.png')
backgroundImage = pygame.image.load('assets/main_background.png')

class Core():
    def drone(self, x, y):
        self.display.blit(droneImage, (x, y))

    def __init__(self):
        self.display = pygame.display.set_mode((600,500))
        # self.display.set_caption
        self.clock = pygame.time.Clock()
        # self.fps = 120
        self.drone_x = 150
        self.drone_y = 150
        self.drone_x_update = 0
        self.drone_y_update = 0
        self.delivery_object_x = 150
        self.delivery_object_y = 300

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.drone_x_update = -5
                    elif event.key == pygame.K_RIGHT:
                        self.drone_x_update = 5
                    elif event.key == pygame.K_UP:
                        self.drone_y_update = -5
                    elif event.key == pygame.K_DOWN:
                        self.drone_y_update = 5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.drone_x_update = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.drone_y_update = 0

            # print(event)

            self.drone_x += self.drone_x_update
            self.drone_y += self.drone_y_update

            self.display.blit(backgroundImage, (0, 0))
            self.drone(self.drone_x, self.drone_y)
            self.drone(self.delivery_object_x, self.delivery_object_y)

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

            pygame.display.update()
            self.clock.tick(80)
