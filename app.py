from tkinter import *
import time
WIDTH = 800
HEIGHT = 500
xSpeed = 1
ySpeed = 1

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

myimage = PhotoImage(file="sailor-moon.png")
lilimage = myimage.subsample(8, 8)
moonimage = canvas.create_image(0, 0, image=lilimage, anchor=NW)

while True:
    coordinates = canvas.coords(moonimage)
    print(coordinates)
    if(coordinates[0]>=(WIDTH - lilimage.width()) or coordinates[0]<0):
        xSpeed = xSpeed * -1
    canvas.move(moonimage, xSpeed, 0)
    window.update()
    time.sleep(0.01)
window.mainloop()