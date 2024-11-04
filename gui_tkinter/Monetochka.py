from tkinter import *
import random

def event(a):
    if a == 1:
        cat.config(text="Орел")
    elif a == 2:
        cat.config(text="Решка")

choice = random.randint(1, 2)

window = Tk()
window.title("Віконечко")
window.config(width=500, height=400, bg="#f5cc7f")

cat = Label(window)
cat.config(text="Підкинь монету", font="Arial 24", bg="#9370db", fg="#88bf8d")
cat.pack(padx=30, pady=30)


knopka = Button(window, command=event(choice))
knopka.config(text="Спробувати!", font="Times 16", bg="#8b0a50", fg="black", bd=15)
knopka.pack(padx=30, pady=30)

window.mainloop()