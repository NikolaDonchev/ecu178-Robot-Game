import pygame, sys

black = (107, 107, 107)
white = (250, 250, 250)
grey = (151, 151, 151)

deliveryItem = pygame.image.load('assets/delivery_item.png')
deliveryItemSelected = pygame.image.load('assets/delivery_item_selected.png')
selectionTick = pygame.image.load('assets/selection_with_tick.png')
selectionNoTick = pygame.image.load('assets/selection_without_tick.png')

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

class Background():
    """
    Class for generating the background on each screen
    """
    def __init__(self, display, background):
        self.display = display
        self.background = background

    def draw(self):
        self.display.blit(self.background, (0, 0))

    def update(self, event, callback=None):
        self.draw()

class CreateRect():
    """
    Creating rectangles of different screens
    Currently used in the selection screen for the order list and footer
    """
    def __init__(self, display, color, width, height, x_pos, y_pos):
        """
        display = the set_mode method from the Gui class
        color = Background color of the rectangle
        width = width of the rectangle
        height = height of it
        x_pos = Position by X axis
        y_pos = Position by Y axis
        """
        self.display = display
        self.color = color
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self):
        pygame.draw.rect(self.display, self.color, (self.x_pos, self.y_pos, self.width, self.height))

    def update(self, event, callback):
        self.draw()

class CreateTitle():
    def __init__(self, display, text, x_pos, y_pos):
        self.display = display
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self):
        smallText = pygame.font.Font("assets/Roboto-Regular.ttf", 28)
        textSurf, textRect = text_objects(self.text, smallText, white)
        textRect = (self.x_pos, self.y_pos)
        self.display.blit(textSurf, textRect)

    def update(self, event, callback):
        self.draw()

class Button(pygame.Surface):
    """
    Generating button
    """
    def __init__(self, display, msg, x, y, w, h, ic, ac, action=None):
        """
        display = the set_mode method from the Gui class
        msg = the text for the button
        x = Position by X axis
        y = Position by Y axis
        W = Width of the button
        H = Height of the button
        ic = Colour of the button
        ac = Colour of the button when its hovered
        action = string with action which is used in Engine to switch to other screen or do other events
        """
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

    def update(self, event, callback=None):
        self.draw()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.x+self.w > event.pos[0] > self.x and self.y+self.h > event.pos[1] > self.y:
                return self.action
        if event.type == pygame.MOUSEMOTION:
            if self.x+self.w > event.pos[0] > self.x and self.y+self.h > event.pos[1] > self.y:
                self.draw(True)
            else:
                self.draw(False)

class CheckBox(pygame.Surface):
    """
    Checbox class. Here's everything related with the checkboxes
    """
    def __init__(self, display, title, price, weight, x_pos, y_pos, clicked=None, selectedItems=None):
        """
        display = the set_mode method from the Gui class
        title = name of the product
        price = price of the product
        weight = weight of the product
        x_pos = Position by X axis
        y_pos = Position by Y axis
        clicked = determing whether the checkbox is clicked or not
        selectedItems = an array of the active checkboxes on the screen (for additional checks)
        """
        pygame.Surface.__init__(self, size = (100,50))
        self.display = display
        self.width = 205 # Default width for checkbox
        self.height = 78 # Default height for checkbox
        self.x_pos = x_pos # Where to place one (x)
        self.y_pos = y_pos # Where to place one (y)
        self.msg = "Opa"
        self.titleText = title
        self.priceText = "Price: £" + str(price)
        self.weightText = "Weight: " + str(weight) + "kg"
        self.clicked = clicked
        self.selectedItems = selectedItems

    def clicked(self):
        self.draw(True)

    def draw(self, state=False):
        if state:
            pygame.draw.rect(self.display, white,(self.x_pos, self.y_pos, self.width, self.height))
            # self.pos_ = (self.x_pos + 100)
            self.display.blit(selectionTick, (self.x_pos + 180, self.y_pos + 55))
        else:
            pygame.draw.rect(self.display, white,(self.x_pos, self.y_pos, self.width, self.height))
            # self.pos_ = (self.x_pos + 100)
            # pygame.draw.rect(self.display, black,(self.x_pos + 180, self.y_pos + 55, 2, 2))
            self.display.blit(selectionNoTick, (self.x_pos + 180, self.y_pos + 55))

        pygame.draw.rect(self.display, grey, (self.x_pos + 6, self.y_pos + 12, 54, 54)) # product image placeholder

        titleFontSize = pygame.font.Font("assets/Roboto-Regular.ttf", 14)
        self.title, titlePosition = text_objects(self.titleText, titleFontSize, black)
        titlePosition = ((self.x_pos + 70, self.y_pos + 10))
        self.display.blit(self.title, titlePosition)
        # Rendering the title of each checkbox

        secondaryFontSize = pygame.font.Font("assets/Roboto-Regular.ttf", 12)
        self.price, pricePosition = text_objects(self.priceText, secondaryFontSize, black)
        pricePosition = ((self.x_pos + 70, self.y_pos + 32))
        self.display.blit(self.price, pricePosition)
        # Rendering the price of each checkbox

        self.weight, weightPosition = text_objects(self.weightText, secondaryFontSize, black)
        weightPosition = ((self.x_pos + 70, self.y_pos + 48))
        self.display.blit(self.weight, weightPosition)
        # Rendering the weight of each checkbox

    def update(self, event, callback):
        self.draw()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.x_pos+self.width > event.pos[0] > self.x_pos and self.y_pos+self.height > event.pos[1] > self.y_pos:
                return self.clicked