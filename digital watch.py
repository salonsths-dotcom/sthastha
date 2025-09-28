from  tkinter import *
from tkinter. ttk import *


mywindow=Tk()
mywindow.title("digital clock")

def time():
    str=strftime("%H : %M : %S %P")
    lbl.config(text=str)
    lbl.aftre(1000,time)


lbl=Label(mywindow,font=("Arial",25), background="black", foreground="white")
lbl.pack()
time()


mainloop()