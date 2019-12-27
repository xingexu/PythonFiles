from tkinter import *

import random 

def click():
    nummy = random.randint(1,6)
    answer["text"] = nummy

window = Tk()
window.title("Roll a dice")
window.geometry("100x120")

button1 = Button(text = "Roll", command = click)
button1.place(x = 30, y = 30, width = 50, height = 25)

answer = Message(text = "")
button1.place( x= 30, y = 70, width = 30, height = 25)

window.mainloop()
