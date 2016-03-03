import pygame, sys

black = (0, 0, 0)
white = (255, 255, 255)
mainBackground2 = pygame.image.load('assets/main_menu_background.png')

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

class Background():

    def __init__(self, display):
        self.display = display

    def draw(self):
        self.display.blit(mainBackground2, (0, 0))

    def update(self):
        print("ok")
        self.draw()

class Button():

    def __init__(self, display, msg, x, y, w, h, ic, ac, action=None):
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

        print( self.x, self.y, self.w, self.h )

    def draw(self):
        pygame.draw.rect(self.display,self.ic,(self.x, self.y, self.w, self.h))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects(self.msg, smallText)
        textRect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        self.display.blit(textSurf, textRect)

    def mouse_clicked(self):
        self.pressed = True

    # def mouse_unclicked(self):
    #     if self.pressed and mousenoclickedatthemoment()
    #         self.pressed = False
    #         dostuff()

    def update(self):
        self.draw()
        self.mouse_clicked()


class CheckBox():

    def __init__(self):
        pass