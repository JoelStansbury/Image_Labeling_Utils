# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from PIL import Image, ImageTk

def multipoint(fname):
    root = tk.Tk()
    im = Image.open(fname)
    W,H = im.size
    w,h = (500,500*H//W)
    im = im.resize(size = (w,h), resample = 0)
    
    photo = ImageTk.PhotoImage(im)
    
    c = tk.Canvas(width=w, height=h)
    c.pack()
    c.create_image(0,0,image=photo,anchor=tk.NW)
    
    coords = []
    markers = []
    def scale_coords(list_of_coords):
        result = []
        for x,y in list_of_coords:
            result.append([x*W//w,y*H//h])
        return result
        
    def onclick(event):
        x,y = (event.x,event.y)
        coords.append((x,y))
        markers.append(c.create_oval((x,y,x+1,y+1),outline='red'))
        
    def rclick(event):
        c.delete(markers[-1])
        del markers[-1]
        del coords[-1]
    
    def enter(event):
        root.destroy()
        
    
    c.bind('<Button-1>',onclick)
    c.bind("<Button-3>",rclick)
    root.bind("<Return>",enter)
    root.mainloop()
    
    return scale_coords(coords)
