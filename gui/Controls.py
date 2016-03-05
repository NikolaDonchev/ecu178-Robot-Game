import pygame, sys

black = (0, 0, 0)
white = (255, 255, 255)



def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

class Background():

    def __init__(self, display, background):
        self.display = display
        self.background = background

    def draw(self):
        self.display.blit(self.background, (0, 0))

    def update(self, event):
        self.draw()

class Button(pygame.Surface):

    def __init__(self, display, msg, x, y, w, h, ic, ac, action=None):
        pygame.Surface.__init__(self, size = (100,50))
        self.mouse = pygame.mouse.get_pos()
        self.clicked = pygame.mouse.get_pressed()
        self.display = display
        self.msg = msg
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ic = ic
        self.ac = ac
        self.action = action
        self.pressed = None

    def draw(self, state=False):
        if state:
            pygame.draw.rect(self.display,self.ac,(self.x, self.y, self.w, self.h))
        else:
            pygame.draw.rect(self.display,self.ic,(self.x, self.y, self.w, self.h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects(self.msg, smallText)
        textRect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        self.display.blit(textSurf, textRect)

    def update(self, event):
        self.draw()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.x+self.w > event.pos[0] > self.x and self.y+self.h > event.pos[1] > self.y:
                return self.action
        if event.type == pygame.MOUSEMOTION:
            if self.x+self.w > event.pos[0] > self.x and self.y+self.h > event.pos[1] > self.y:
                self.draw(True)
            else:
                self.draw(False)