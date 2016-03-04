<<<<<<< HEAD
=======
import pygame
from gui.Controls import *
from engine.Engine import *

green = (156, 219, 151)
green_bright = (0,150,0)
orange = (0, 255,255)
white = (255, 255, 255)

blankImage = pygame.image.load('Selection_screen.png') 

def game_image(x, y):
    gameDisplay.blit(blankImage, (x, y)

class StartScreen():
    def __init__(self):
        self.objects = [
            Background(GameEngine().display),
            Button(GameEngine().display,"START",220,280,163,48,green,white,"play"),
            Button(GameEngine().display,"OPTIONS",220,340,163,48,green,black,"play"),
            Button(GameEngine().display,"EXIT",220,400,163,48,green,black,"play")
        ]

        for object in self.objects:
            object.update()


    def add_object(self, obj):
        self.objects.append(obj)

global clickedButtons,sumOfCosts,textDisp
clickedButtons=[]
sumOfCosts=[0,0]
textDisp = None

def addCostsAndDisplay(msg,cost,weight):    #Add up the cost and the weight of item
    global sumOfCosts
    sumOfCosts[0]+=cost
    sumOfCosts[1]+=weight

    basicfont = pygame.font.SysFont(None, 27)
    text = basicfont.render('adding '+str(msg)+' adds up to '+str(sumOfCosts[0])+' and weighs '+str(sumOfCosts[1]), True, (255, 0, 0), (255, 255, 255))
    return text
    

def button2(msg,x,y,w,h,ic,ac,cost=1,weight=1, action=None):
    global clickedButtons,textDisp
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #Button Function
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))

        if click[0] == 1 and action != None:
            if not (msg in clickedButtons):
                #Save that this button has been clicked
                clickedButtons.append(msg)
                textDisp=addCostsAndDisplay(msg,cost,weight)
            if action == "START":
                game_loop()
            elif action == "BACK":
                game_intro()
                quit()

            elif action == "Playstation 4":
                print("")
    else:
        #Check if this button has been clicked
        if (msg in clickedButtons):
            pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        else:
            pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

#Text Font and Text Position
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

class SelectionScreen():
    def game_select_items_menu():
        global textDisp
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        gameSelectItems = False
        white not gameSelectItems:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            blank_image(x, y)
            if (not textDisp is None):
                
                screen = pygame.display.get_surface()
                textRect = textDisp.get_rect()
                textRect.center = ((30+500/2)),(150+(350/2))
                screen.blit(textDisp, textRect)
                
            button2("Xbox One", 374, 60, 168, 48, white, orange, 310, 32, "Xbox One")
            
            button2("Playstation 4", 200, 60, 168, 48, white, orange, 290, 29, "Playstation 4")
            
            button2("Kettle", 30, 60, 163, 48, white, orange, 70, 10, "Kettle")
            
            button2("Lewi Jeans", 200, 160, 163, 48, white, orange, 399, 41, "Samsung TV")
            
            button2("MacBook", 200, 160, 168, 48, white, orange, 689, 92, "MacBook")
            
            button2("Samsung TV", 30, 160, 163, 48, white, orange, 399, 41, "Samsung TV")
            
            button2("Nike Air Max", 374, 250, 168, 48, white, orange, 90, 10, "Nike Air Max")
            
            button2("Apple iPad", 200, 250, 168, 48, white, orange, 189, 30, "Apple iPad")
            
            button2("Perfume", 30, 250, 163, 48, white, orange, 45, 65, "Perfume")
            
            #Bottom of GUI Buttons 
            
            button2("START", 374, 370, 163, 48, green, green_bright, 0, 0, "START")
            
            button2("BACK", 374, 430, 163, 48, green, green_bright, 0, 0, "BACK")
            
            pygame.display.update()
            
            clock.tick(80)
            
            
            
        
        
>>>>>>> origin/master
