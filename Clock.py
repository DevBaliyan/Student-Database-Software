from tkinter import *
from time import sleep
i= 0
"""It is not working i can use it if i dont use recursion in start
Winsound collection of sounds
dbm, cmd, copy internal
timer can be made with loop or by writing a very varge value stopwatch can also
be made
"""

def start():
    global i
    sleep(1)
    i += 1
    tim = Entry(tk, font=('arial', 18))
    tim.place(x=150, y=150)
    tim.insert(0, i)
    start()

tk = Tk()
tk.geometry('450x450')
tk.resizable(0, 0)
tk.title('Stu_Data')
tk.configure(bg='#566573')

la = Label(tk, bg='#566573')
la.pack()
tim = Entry(tk, font=('arial', 18))
tim.place(x=150, y=150)
tim.insert(0, i)
f = Frame(tk, height=449, width=449)
b1 = Button(tk, text="Start", bd=0, cursor='hand2', activebackground='#566573', command=start,
            font=('arial', 15), bg='#566573', activeforeground='#6665FF')
b1.place(x=5, y=5)

tk.mainloop()