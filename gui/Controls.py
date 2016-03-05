import pygame, sys

black = (107, 107, 107)
white = (250, 250, 250)

deliveryItem = pygame.image.load('assets/delivery_item.png')
deliveryItemSelected = pygame.image.load('assets/delivery_item_selected.png')
selectionTick = pygame.image.load('assets/selection_with_tick.png')
selectionNoTick = pygame.image.load('assets/selection_without_tick.png')

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
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

        smallText = pygame.font.Font("assets/Roboto-Regular.ttf", 20)
        textSurf, textRect = text_objects(self.msg, smallText, white)
        textRect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2) - 1))
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

class CreateTitle():
    def __init__(self):
        pass

class CheckBox(pygame.Surface):
    def __init__(self, display, x_pos, y_pos, clicked=None):
        pygame.Surface.__init__(self, size = (100,50))
        self.display = display
        self.width = 205 # Default width for checkbox
        self.height = 78 # Default height for checkbox
        self.x_pos = x_pos # Where to place one (x)
        self.y_pos = y_pos # Where to place one (y)
        self.msg = "Opa"
        self.titleText = "Title"
        self.subtitleText = "Subtitle"
        self.clicked = clicked

    def draw(self, state=False):
        if state:
            pygame.draw.rect(self.display, white,(self.x_pos, self.y_pos, self.width, self.height))
        else:
            pygame.draw.rect(self.display, white,(self.x_pos, self.y_pos, self.width, self.height))
            self.pos_ = (self.x_pos + 100)
            self.display.blit(selectionNoTick, (self.x_pos + 180, self.y_pos + 55))

        titleFontSize = pygame.font.Font("assets/Roboto-Regular.ttf", 18)
        subtitleFontSize = pygame.font.Font("assets/Roboto-Regular.ttf", 14)
        self.title, titlePosition = text_objects(self.titleText, titleFontSize, black)
        self.subtitle, subtitlePosition = text_objects(self.subtitleText, subtitleFontSize, black)
        titlePosition = ((self.x_pos + 80, self.y_pos + 10))
        subtitlePosition = ((self.x_pos + 80, self.y_pos + 30))
        self.display.blit(self.title, titlePosition)
        self.display.blit(self.subtitle, subtitlePosition)

    def update(self, event):
        self.draw()
        if event.type == pygame.MOUSEMOTION:
            if self.x_pos + self.width > event.pos[0] > self.x_pos and self.y_pos + self.height > event.pos[1] > self.y_pos:
                self.draw(True)
        else:
            self.draw(False)

