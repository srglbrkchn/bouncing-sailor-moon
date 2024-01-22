from tkinter import *
import time
WIDTH = 700
HEIGHT = 400
xSpeed = 4
ySpeed = 5

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

backgroundimg = PhotoImage(file="sailor-moon-bg.png")
lilbackground = backgroundimg.subsample(2, 2)
background = canvas.create_image(0, 0, image=lilbackground, anchor=NW)

myimage = PhotoImage(file="sailor-moon.png")
lilimage = myimage.subsample(4, 4)
moonimage = canvas.create_image(0, 0, image=lilimage, anchor=NW)
rotation_angle = 0


while True:
    coordinates = canvas.coords(moonimage)
    print(coordinates)
    if(coordinates[0]>=(WIDTH - lilimage.width()) or coordinates[0]<0):
        xSpeed = xSpeed * -1


    if (coordinates[1] >= (HEIGHT - lilimage.height())or coordinates[1]<0):
        ySpeed = ySpeed * -1
    canvas.move(moonimage, xSpeed, ySpeed)
    window.update()
    time.sleep(0.01)
window.mainloop()