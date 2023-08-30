#importing necessary packages
import tkinter
import random, string

#Root window
root = tkinter.Tk()
root.geometry("400x280")
root.title("Password Generator")

title = tkinter.StringVar()
label = tkinter.Label(root, textvariable=title).pack()
title.set("Password strength:")


def selection():
    global selection
    selection = choice.get()


#password strength
choice = tkinter.IntVar()
R1 = tkinter.Radiobutton(root, text="Poor", variable=choice, value=1, command=selection).pack(anchor=tkinter.CENTER)
R2 = tkinter.Radiobutton(root, text="Average", variable=choice, value=2, command=selection).pack(anchor=tkinter.CENTER)
R3 = tkinter.Radiobutton(root, text="Strong", variable=choice, value=3, command=selection).pack(anchor=tkinter.CENTER)
labelchoice = tkinter.Label(root)
labelchoice.pack()

#password length
lenlabel = tkinter.StringVar()
lenlabel.set("Password length:")
lentitle = tkinter.Label(root, textvariable=lenlabel).pack()


val = tkinter.IntVar()
spinlenght = tkinter.Spinbox(root, from_=4, to_=24, textvariable=val, width=13).pack()




def callback():
    lsum.config(text=passgen())



passgenButton = tkinter.Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3, bg='lightblue')
passgenButton.pack()
password = str(callback)


lsum = tkinter.Label(root, text="")
lsum.pack(side=tkinter.BOTTOM)

poor= string.ascii_uppercase + string.ascii_lowercase
average= string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor+ average + symbols


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))


root.mainloop()
