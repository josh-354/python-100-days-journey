import tkinter

window = tkinter.Tk()#creating a window 
window.title("My first GUI program")#tittle name
window.minsize(width=500,height=300)#sets the minimum size of the window


my_label = tkinter.Label(text="I am label")
my_label.pack()#place the label in the sccreen



window.mainloop()