from ast import Lambda
from doctest import master
import tkinter as tk
import boxdb
from template2 import grab
from templayte1 import grab_music

global box
global musicbox
global root
root = tk.Tk()
box=grab(root)
class Canvas:
    def __init__(self,master):
        super().__init__()
        # box=[]  
        for i in box:
            i.pack()
        musicbox=[]  
        musicbox=grab_music(master)
        for i in musicbox:
            i.pack()
        bull=tk.Button(master,text="delete music",command=lambda arg=musicbox : delete(arg))
        bull.pack()
        ren=tk.Button(master,text="render",command=lambda arg=musicbox : render(arg))
        ren.pack()



def delete(elements):
    for i in elements:
        i.destroy()
def render(elements):
    for i in elements:
        i.pack()

app = Canvas(root)
root.mainloop()




