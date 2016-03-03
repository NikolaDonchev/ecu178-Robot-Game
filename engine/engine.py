import sys, pygame
from gui.Controls import Button

white = (255, 255, 255)
black = (0, 0, 0)

class GameEngine():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Amazon Delivery Service')
        self.view = None
        self.clock = pygame.time.Clock()
        self.fps = 10
        # self.clock = self.clock.tick(self.fps)
        self.display = pygame.display.set_mode((600, 500))

    def main_loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Button("START", 220, 280, 163, 48, white, black, "play")

            pygame.display.flip()


    def change_view(self, view, image):
        self.display.blit(image, (0, 0))
        self.view = view