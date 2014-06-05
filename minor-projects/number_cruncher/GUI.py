from Tkinter import *
import time

root = Tk()

def callback(event):
    print "clicked at", event.x, event.y 

frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

time.sleep(5)

print "Finished!"
