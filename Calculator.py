import tkinter
import tkinter as tk
from tkinter import  *

root = tk.Tk()

lable3 = Label(root,font=("bold",20),text="enter the integers below ")
lable3.pack()
entry = Entry(root,bd=15,bg="green",fg="black",font=("italic",24))
entry.pack()
entry2 = Entry(root,bd=15,bg="green",fg="black",font=("italic",24))
entry2.pack()

def add():
    entryget = entry.get()
    entrybuy = entry2.get()
    lable7 = Label(root,text=int(entryget)+int(entrybuy),font=("italic",24))
    lable7.pack()


def sub():
    entryget = entry.get()
    entrybuy = entry2.get()
    lable7 = Label(root, text=int(entryget) - int(entrybuy),font=("italic",24))
    lable7.pack()

def mul():
    entryget = entry.get()
    entrybuy = entry2.get()
    lable7 = Label(root, text=int(entryget) * int(entrybuy),font=("italic",24))
    lable7.pack()

def div():
    entryget = entry.get()
    entrybuy = entry2.get()
    lable7 = Label(root,text=int(entryget)/int(entrybuy),font=("italic",24))
    lable7.pack()

#class first word should be captal!!i
root.geometry("400x500+250+120")


buttonplus = Button(root,text="+",command=add,bd=15,padx=20,pady=20,font=("italic",24))
buttonplus.pack(side=tkinter.LEFT)


buttonminuse = Button(root,text="-",command=sub,bd=15,padx=20,pady=20,font=("italic",24))
buttonminuse.pack(side=tkinter.RIGHT)

buttonmul = Button(root,text="*",command=mul,bd=15,padx=20,pady=20,font=("italic",24))
buttonmul.pack(side=tkinter.TOP)

buttondiv = Button(root,text="/",command=div,bd=15,padx=20,pady=20,font=("italic",24))
buttondiv.pack(side=tkinter.BOTTOM)

root.title("calculator box")

root.mainloop()
