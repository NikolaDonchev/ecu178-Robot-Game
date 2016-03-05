import pygame, sys

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

            pygame.display.update()
            self.clock.tick(80)
