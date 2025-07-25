import tkinter

window = tkinter.Tk()#creating a window 
window.title("My first GUI program")#tittle name
window.minsize(width=500,height=300)#sets the minimum size of the window

my_label = tkinter.Label(text="I love you",font=("Arial",24,"bold"))
my_label.pack(side="left")#place the label in the sccreen

import turtle


window.mainloop()