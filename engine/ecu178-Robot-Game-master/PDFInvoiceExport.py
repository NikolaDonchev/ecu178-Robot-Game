import pygame, sys
from weasyprint import HTML, CSS
from gui.Controls import CreateTitle, Background, Button
import time

green = (156, 219, 151)
green_bright = (0,150,0)
emptyBackground = pygame.image.load("assets/empty_background.png")

class InvoiceEngine():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps = 80
        self.event = None

    def items(self):
        self.items

    def mainLoop(self, objects):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for object in objects:
                object.update(event, self.items)
                self.handler = object.update(event, self.selectedItems)

                if self.handler == "downloadInvoice":
                    GenerateInvoice().invoice()

            pygame.display.update()
            self.clock.tick(self.fps)

class InvoiceView():
    def __init__(self, items=None):
        self.display = pygame.display.set_mode((600,510))
        pygame.display.set_caption('Generate Invoice')
        self.items = items
        self.objects = [
            CreateTitle(self.display, "Do you want to download your invoice?", 24, 40),
            Background(self.display, emptyBackground), # Setting the background
            Button(self.display, "Download invoice", 220, 280, 163, 48, green, green_bright, "downloadInvoice")
        ]
        # Adding the elements to the "object" array

        InvoiceEngine().mainLoop(self.objects)
        # running the main loop and giving the array as parameter if the mail_loop function from the Engine class


class GenerateInvoice():
    def __init__(self, items):
        self.items = items
        self.finalPrice = items[0]['productPrice'] + items[1]['productPrice'] + items[2]['productPrice'] # making a sum of all projects

    def invoice(self):
        today = time.strftime("%d/%m/%Y")

        HTML(string='''
        <html>
        <style media="screen">

        </style>
        <body style="width: 100%">
            <div class="header">
                <img style="width: 200px" src="http://donchev.net/blog/ads_drone.png" alt="" />
            </div>
            <div style="padding-top: 60px; float:left; width: 100%;">
                <div style="width: 60%;float:left">
                    <h2>billed to</h2>
                    <p>Nikola Donchev</p>
                    <p>Coventry, UK</p>
                    <p>CV1 5AX</p>
                </div>
                <div style="width: 40%;float:left">
                    <p>Invoice number: 43432</p>
                    <p>Date: ''' + today + '''</p>
                    <p style="background-color: #cacaca">Total amount: ''' + str(self.finalPrice) + '''</p>
                </div>
            </div>
            <div style="clear: both"></div>
            <hr>
        </body>
        </html>
        ''').write_pdf('your-invoice.pdf',
        stylesheets=[CSS(string='body { font-family: Helvetica, Arial } * { margin: 0; padding: 0; } th { text-align: left } p, h2 { padding: 5px; }')])