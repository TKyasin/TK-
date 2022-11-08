import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter import *
danger1 =          "        ||||||||||||||||||||||||||         "
danger2 =          "      ||||||||||||||||||||||||||||||         "
danger3 =          "    |||                            |||       "      
danger4 =          "    ||||        o o   o o         ||||       "
danger5 =          "    |||||        o     o         |||||       "
danger6 =          "    |||||                        |||||       "
danger7 =          "    ||||        TK--______--TK    ||||        "
danger8 =          "    ||||                          ||||       "
danger9 =          "        |||||||||||||||||||||||||||         "
danger10 =          "           |||||||||||||||            "
danger11 =          "               |||||||                 "
root = tk.Tk()
root.configure(bg="Black")
root.iconbitmap("./um.ico")
root.title("Tkinter Hub")
root.attributes("-topmost", 1)
l1=Label(root,text="HACKED",fg="red", font="Times 280 bold", bg='black').pack()
l2=Label(root,text=danger1,fg="red", font="Times 45 bold", bg='black').pack()
l2=Label(root,text=danger2,fg="red", font="Times 45 bold", bg='black').pack()
l2=Label(root,text=danger3,fg="red", font="Times 45 bold", bg='black').pack()
l2=Label(root,text=danger4,fg="red", font="Times 45 bold", bg='black').pack()
l2=Label(root,text=danger5,fg="red", font="Times 45 bold", bg='black').pack()
l2=Label(root,text=danger6,fg="red", font="Times 45 bold", bg='black').pack()
l2=Label(root,text=danger7,fg="red", font="Times 45 bold", bg='black').pack()
l2=Label(root,text=danger8,fg="red", font="Times 45 bold", bg='black').pack()
l2=Label(root,text=danger9,fg="red", font="Times 45 bold", bg='black').pack()
l2=Label(root,text=danger10,fg="red", font="Times 45 bold", bg='black').pack()
l2=Label(root,text=danger11,fg="red", font="Times 45 bold", bg='black').pack()


root.geometry("1920x1000")

def confirm():
    ans = askyesno(title="Exit", message="Do u want to exit")

    if ans:
        root.destroy(False)

root.protocol("WM_DELETE_WINDOW", confirm)
root.mainloop()