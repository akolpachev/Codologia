from tkinter import *


def dml ():
    entr.delete(0,END)
    entr.insert(0,"я все стераьаьаоалалалппппппппппппппппппппппппппппппп")

def dml2 ():
    v = entr.get()
    entr.delete(0, END)
    entr2.insert(0, v)


def dml3 ():
    v= entr.get()
    lst.insert(0,v)
    entr.delete(0,END)

def dml4 ():
    lst.delete(0,END)


def chn(event):
    labl["text"]="thvjbjfhvjhb"

def dml5(event):
    lst["text"]="sddvsdf"
    lst.insert(0,)

def dml6(event):
    lst["text"]="fgfg"


def dml7(event):
    lst["text"]="gdfgdfrgrwgeg"



root = Tk()
root.title("IIPOG")
root.geometry("400x800")

labl=Label(text="fafad\nfadf",fg="red",font=400)
labl.place(x=200,y=100)

btn=Button(text="стереть",command=dml)
btn.place(x=300)

btn2=Button(text="перенести",command=dml3)
btn2.place(x=300,y=30)

entr=Entry(bd=10,width=30)
entr.pack()

btn4=Button(text="изменить",)
btn4.place(x=250,y=150)


lst.bind("<f>",dml5)
lst.bind("Return",dml5)




entr2=Entry(bd=10,width=30)
entr2.place(y=500,x=100)

lst=Listbox()
lst.place(x=200,y=300)

btn3=Button(text="cтереть",command=dml4)
btn3.place(x=250,y=100)

bt5=Button(text="изменить",command=chn)
bt5.place(x=250,y=350)

ssf_lang =IntVar()
ssf_checkbutton=Checkbutton(text="ssf",variable=ssf_lang)
ssf_checkbutton.place(x=150,y=546)

mainloop()
