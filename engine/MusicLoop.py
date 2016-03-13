#Mario Kostadinov's Individual Feature
class MusicLoop():
    def __init__(self):
        self.display = Gui().display
        self.objects = [
            Background(self.display, menuBackground),
            Button(self.display, "Music ON/OFF", 220, 280, 163, 48, green, green_bright, "OnOff"),
            Button(self.display, "Volume +", 220, 340, 80, 48, green, green_bright, "+"),
            Button(self.display, "Valume -", 303, 340, 80, 48, green, green_bright, "-"),
            Button(self.display, "BACK", 220, 400, 163, 48, green, green_bright, "option")
        ]

        Engine().main_loop(self.objects)
