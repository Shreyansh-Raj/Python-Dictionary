from googletrans import Translator
from tkinter import *
import ctypes
from tkinter.messagebox import *

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

root = Tk()
root.iconbitmap("favicon.ico")
root.title("Translator")
root.geometry("550x500")
root.resizable(False,False)

labe = Label(root, text="DICTIONARY BY SHREYANSH",font="Calibri 20 bold")
labe.pack(pady=4)

a=StringVar()
lab = Label(root,text="Enter The Word",font=("Andalus", 13))
lab.pack(pady=10)
e1= Entry(root,textvariable=a)
e1.pack(pady=0)

def translate():
    # import time
    statusbar_var.set("Tanslating...")
    statusbar.update()
    try:
        global label
        try:
            label.destroy()

        except:
            pass

        r = e1.get()
        if r == "":
            showerror("Dictionary","Please enter a word")

        else:
            translator = Translator()
            word1 = translator.translate(f"{r}", dest="hindi",src="en")
            w = word1.text
            label = Label(text=f"The Hindi meaning of {r} is {w}", font='bold')
            label.pack(pady=10)
            statusbar_var.set("Ready")
            statusbar.update()

    except:
        showerror("Dictionary","No Internet")

b1 = Button(root, text="Translate", command=translate, bg='brown', fg='white', font=('Comic Sans MS', 10, 'bold'))
b1.pack(pady=23)

statusbar_var = StringVar()
statusbar_var.set("Ready")
statusbar = Label(root,textvariable=statusbar_var,relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()