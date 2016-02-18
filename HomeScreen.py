import Tkinter

window = Tkinter.Tk()

def motion(event):
    """Functio which gets coordinates
    of current mouse position"""
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

window.title("Game")
window.geometry("400x400")

label = Tkinter.Label(window, text="Home")
label.pack()

window.bind('<Motion>', motion)

window.mainloop()
