import sys, pygame
from gui.Controls import Button

white = (255, 255, 255)
black = (0, 0, 0)

class GameEngine():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Automated Delivery Service')
        self.view = None
        self.clock = pygame.time.Clock()
        self.fps = 10
        self.display = pygame.display.set_mode((600,500))

    def main_loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

    def change_view(self, view):
        self.view = view