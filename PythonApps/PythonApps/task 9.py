from random import randint
from tkinter import *

clicks=0
colors=["red","blue","green"]
def click_button():
    global clicks
    clicks +=1
    root.title("clicks{}".format(clicks))
    btn.configure(bg =colors[clicks%3] )
    

    

root=Tk()
root.title("кнопка")
root.geometry("400x300")

btn=Button(text="что то написано", command=click_button)
btn.pack(expand=True,fill=BOTH)
background="#123"
foreground="#ccc"

root.mainloop()
