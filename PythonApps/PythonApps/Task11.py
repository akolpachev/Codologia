from tkinter import *

WIDTH = 800

HEIGHT = 600

SEG_SIZE = 20

IN_GAME = True

root = Tk()
root.title
c = Canvas(root,width=WIDTH,height=HEIGHT, bg="#003300")
c.grid()
c.focus_set()

class Segment(object):
    def __init__(self,x,y):
        self.instance = c.create_restangle(x,y,x+SEG_SIZE,y+SEG_SIZE,fill="white")

class Snake(object):
    def __init__(self,segments):
        self.segments = segments
        self.mapping = {"down":(0,1), "Up":(0,-1), "Letf":(-1,0), "Right":(1,0)}
        self.vector = self.mapping["Right"]

    def move(self):

        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
        x1,y1,x2,y2 = c.coords(self.segments[index+1].instance)

        c.coords(segment,x1,y1,x2,y2)

        x1,y1,x2,y2= c.coords(self.segments[-2].instance)

        c.coords(self.segments[-1].instanse,
                  x1+self.vector[0]*SEG_SIZE,
                     y1 +self.vector[1]*SEG_SIZE,
                     x2 +self.vector[0]*SEG_SIZE,
                     y2 + self.vector[1]*SEG_SIZE)
    def change_direction(self,event):
        if event.keysym in self.mappiing:
            self.vector = self.mappiing[event,keysym]

    def add_segment(self):

        last_seg = c.coords(self.segments[0].instance)

        x= last_seg[2] -SEG_SIZE
        y= last_seg[3] -SEG_SIZE

        self.segments.insert(0,Segment(x,y))


        segments =[Segment(SEG_SIZE,-SEG_SIZE),Segment(SEG_SIZE*2,-SEG_SIZE),Segment(SEG_SIZE*3,-SEG_SIZE)]

        s = Snake(segments)


root.mainloop()

