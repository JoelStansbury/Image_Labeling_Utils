import tkinter as tk
from PIL import Image, ImageTk

def multipoint(img):
    root = tk.Tk()
    if isinstance(img, str):
        img = Image.open(img)
    W,H = img.size
    w,h = (500,500*H//W)
    img = img.resize(size = (w,h), resample = 1)
    
    photo = ImageTk.PhotoImage(img)
    
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



class bbox:
    def __init__(self,img, scale=1):
        self.root = tk.Tk()
        if isinstance(img, str):
            img = Image.open(img)
        self.scale = scale

        W,H = img.size
        w,h = (int(scale*W),int(scale*H))

        img = img.resize(size = (w,h), resample = 1)
        
        photo = ImageTk.PhotoImage(img)
        
        self.c = tk.Canvas(width=w, height=h)
        self.c.pack()
        self.c.create_image(0,0,image=photo,anchor=tk.NW)
        
        self.bbox = [None, None, None, None]
        self.active_rect = None

        self.c.bind('<Button-1>',self.onclick)
        self.c.bind("<B1-Motion>",self.move)
        self.root.bind("<Return>",self.enter)
        self.root.mainloop()


    def get_bbox(self):
        return [int(i/self.scale) for i in self.bbox]
        
    def onclick(self, event):
        if self.active_rect:
            self.c.delete(self.active_rect)
        x,y = (event.x,event.y)
        self.bbox = [x,y,x+1,y+1]
        self.active_rect = self.c.create_rectangle(self.bbox,outline='red')
    
    def move(self, event):
        if self.active_rect != None:
            x2,y2 = (event.x,event.y)
            self.bbox = [self.bbox[0], self.bbox[1],x2,y2]
            self.c.delete(self.active_rect)
            self.active_rect = self.c.create_rectangle(self.bbox,outline='red')
    
    def enter(self, event):
        self.root.destroy()