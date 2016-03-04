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
            
            button2(
            
            
            
            
            
        
        
