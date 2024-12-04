import tkinter
from tkinter import *
from datetime import date
root = Tk()
root.title("Hello world")
root.geometry("500x400")
label1 = Label(text = "Hey there", fg = "white", bg = "blue", height = 1, width = 400)
label2 = Label(text = "Full name", bg = "white")
name_entry = Entry()
def display():
    name = name_entry.get()
    greet = f"Hello {name}, How are you?\n"
    message = f"Today's date is {date.today()}\n"
    text_box.delete(1.0, END)
    text_box.insert(END, greet)
    text_box.insert(END, message)
text_box = Text(height = 5)
button1 = Button(text = "Begin", fg = "white", bg = "blue", height = 1, command = display)
#Packing
label1.pack()
label2.pack()
name_entry.pack()
text_box.pack()
button1.pack()
root.mainloop()