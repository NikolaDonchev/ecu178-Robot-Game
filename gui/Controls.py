import pygame, sys

black = (0, 0, 0)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

class Button():

    def __init__(self, msg, x, y, w, h, ic, ac, action=None):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.mouse = pygame.mouse.get_pos()
            self.clicked = pygame.mouse.get_pressed()
            self.display = pygame.display.set_mode((600, 500))
            self.msg = msg
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.ic = ic
            self.ac = ac
            self.action = action


            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    # if self.event_rect.collidepoint(event.pos):
                    print("mouse moving")

            # if self.x + self.w > self.mouse[0] > self.x and self.y + self.h > self.mouse[1] > self.y:
            #     pygame.draw.rect(self.display, self.ac, (self.x, self.y, self.w, self.h))
            #
            #     print("")
            #
            #     if self.clicked[0] == 1 and self.action != None:
            #         if self.action == "play":
            #             print("start page")
            #             pass
            #         elif self.action == "Exit":
            #             pass
            #
            # else:
            #     pygame.draw.rect(self.display, self.ic, (self.x, self.y, self.w, self.h))

            print(self.action)

            smallText = pygame.font.Font("freesansbold.ttf", 20)
            textSurf, textRect = text_objects(self.msg, smallText)
            textRect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
            self.display.blit(textSurf, textRect)
            pygame.time.Clock().tick(10)


    def update(self):
        pass


class CheckBox():

    def __init__(self):
        pass