from tkinter import *


def entry():
    def greet():
        a = welcome.get()
        welcome.destroy()
        ok.destroy()
        name.configure(text="\n\nHello! " + a + "\n\nWelcome To Students Database", bg='#566573')
        Label(wel, text='click next to continue to database', font=('arial', 13), bg='#566573').place(x=170, y=200)
        nex = Button(wel, image=n, command=wel.destroy, bg='#566573',
                     activebackground='#566573', bd=0)
        nex.place(x=250, y=250)

    wel = Tk()
    wel.title('Greet')
    wel.minsize(height=350, width=600)
    wel.maxsize(height=350, width=600)
    wel.configure(background='#566573')
    name = Label(wel, text='\nEnter Your Name', font=('arial', 15),
                 bg='#566573', fg='powder blue')
    name.pack()
    submit = PhotoImage(file="Buttons\\submit4.png")
    n = PhotoImage(file="Buttons\\next2.png")
    welcome = Entry(wel, bd=3, font=('italic', 15), bg='#66CCFF')
    welcome.place(height=40, width=250, x=170, y=130)
    ok = Button(wel, image=submit, command=greet, bg='#566573', bd=0,
                activebackground='#566573')

    ok.place(x=250, y=250)
    wel.mainloop()


