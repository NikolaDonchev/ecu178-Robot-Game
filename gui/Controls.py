import pygame, sys
# from engine.Engine import GameEngine

black = (0, 0, 0)
white = (255, 255, 255)
mainBackground2 = pygame.image.load('assets/main_menu_background.png')

class testtt():
    def __init__(self):
        print("okay..")

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

class Background():

    def __init__(self, display):
        self.display = display

    def draw(self):
        self.display.blit(mainBackground2, (0, 0))

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

        print( self.x, self.y, self.w, self.h )

    def draw(self, state=False):
        if state:
            pygame.draw.rect(self.display,self.ac,(self.x, self.y, self.w, self.h))
        else:
            pygame.draw.rect(self.display,self.ic,(self.x, self.y, self.w, self.h))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects(self.msg, smallText)
        textRect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        self.display.blit(textSurf, textRect)

    # def mouse_clicked(self, pressed=False):
    #     if pressed:
    #         self.pressed = True
    #         return True
    #     else:
    #         # print("FASLEEE")
    #         return False

    def mouse_hovered(self):
        self.hovered = True

    # def mouse_unclicked(self):
    #     if self.pressed and mousenoclickedatthemoment()
    #         self.pressed = False
    #         dostuff()

    def update(self, event):
        self.draw()

        if event.type == pygame.MOUSEMOTION:
            if self.x+self.w > event.pos[0] > self.x and self.y+self.h > event.pos[1] > self.y:
                self.draw(True)

                # self.mouse_clicked(True)
                # ChangeV("select")
            else:
                self.draw(False)