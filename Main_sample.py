import tkinter as tk
from time import sleep
#Variable stored in memory even after changing data inside???

str_about = "\nDeveloped by: Dev Balyan\n\nVersion1.0.0\nRelease Date:\n\n"

class application:
    def menu_bar():
        #global menubar
        destroy_everything()
        menubar = tk.Menu(app)
        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label="New")
        filemenu.add_command(label = "Open")
        filemenu.add_command(label = "Save")
        filemenu.add_command(label = "Save as...")
        filemenu.add_command(label = "Close")
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = app.quit)
        menubar.add_cascade(label = "File", menu = filemenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label = "Help Index")
        helpmenu.add_command(label = "About...", command=about_info)
        menubar.add_cascade(label = "Help", menu = helpmenu)
        app.config(menu = menubar)
    def main_menu():
        b1 = tk.Button(app, text="create", bd=0, cursor='hand2', activebackground='#566573',
                    font=('arial', 15), bg='#566573', activeforeground='#6665FF', command=run.create)
        b1.place(x=5, y=5)
        #, command=update
        b2 = tk.Button(app, text="update", bd=0, cursor='hand2',
                    font=('arial', 15), bg='#566573', activebackground='#566573', activeforeground='#6665FF')
        b2.place(x=5, y=60)
        #, command=view
        b3 = tk.Button(app, text='view', cursor='hand2', bd=0,
                    font=('arial', 15), bg='#566573', activebackground='#566573', activeforeground='#6665FF')
        b3.place(x=5, y=115)
        #, command=viewall
        b4 = tk.Button(app, text='viewall', cursor='hand2',
                    bd=0, font=('arial', 15), bg='#566573', activebackground='#566573', activeforeground='#6665FF')
        b4.place(x=5, y=170)
    def create():
        tk.Label(app, text="Name :", font=('arial', 14), bg='#566573').place(x=0, y=20)
        tk.Label(app, text="Section :", font=('arial', 14), bg='#566573').place(x=0, y=65)
        tk.Label(app, text="Roll no :", font=('arial', 14), bg='#566573').place(x=0, y=110)
        tk.Label(app, text="DOB :", font=('arial', 14), bg='#566573').place(x=0, y=155)
        tk.Label(app, text="Phone :", font=('arial', 14), bg='#566573').place(x=0, y=200)
        tk.Label(app, text=" :", font=('arial', 14), bg='#566573').place(x=0, y=245)
        tk.Label(app, text=" :", font=('arial', 14), bg='#566573').place(x=0, y=290)
        tk.Label(app, text=" :", font=('arial', 14), bg='#566573').place(x=0, y=335)
        e1 = tk.Entry(app, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=20, height=30)
        e2 = tk.Entry(app, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=65, height=30)
        e3 = tk.Entry(app, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=110, height=30)
        e4 = tk.Entry(app, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=155, height=30)
        e5 = tk.Entry(app, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=200, height=30)
        e6 = tk.Entry(app, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=245, height=30)
        e7 = tk.Entry(app, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=290, height=30)
        e8 = tk.Entry(app, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=335, height=30)
        #, command=add
        sub = tk.Button(app, image=sbmt_btn_img, bd=0, bg='#566573')
        sub.place(x=330, y=400)

    def Update():
        pass
    def View():
        pass


class run:
    def main_page():
        application.menu_bar()
        application.main_menu()
    def create():
        destroy_everything()
        application.menu_bar()
        application.create()


def about_info():
    #tk.Label(text="Developed by: Dev Balyan", bg='#566573')
    destroy_everything(label_main)
    tk.Label(app, text=str_about, font=('arial', 15),
                bg='#566573', fg='powder blue').pack()
    

def destroy_everything(*exception):
    for child in app.winfo_children():
        if child in exception:
            continue
        else:
            print(child)
            child.destroy()

    
def welcome_page_2():
    name = text_box.get()
    app.title("Database")
    label_main.configure(text="\n\nHello! " + name + "\n\nWelcome To Students Database", bg='#566573')
    destroy_everything(label_main)
    tk.Button(app, image=next_btn_img, command=run.main_page, bg='#566573',
              activebackground='#566573', bd=0).place(x=250, y=250)
    tk.Label(app, text='click next to continue to database', font=('arial', 13), bg='#566573').place(x=170, y=200)


# app- Application Attributes
app = tk.Tk()
app.title('Greetings')
app.minsize(height=450, width=600)
app.maxsize(height=500, width=600)
app.configure(background='#566573')
app.iconbitmap('2906206.ico')


#images
sbmt_btn_img = tk.PhotoImage(file="Buttons\\submit4.png")
next_btn_img = tk.PhotoImage(file="Buttons\\next2.png")


# Main-Label
label_main = tk.Label(app, text='\nEnter Your Name', font=('arial', 15),
                bg='#566573', fg='powder blue')
label_main.pack()

text_box = tk.Entry(app, bd=3, font=('italic', 15), bg='#66CCFF')
text_box.place(height=40, width=250, x=170, y=130)

tk.Button(app, image=sbmt_btn_img, bg='#566573', bd=0,activebackground='#566573',
          command=welcome_page_2).place(x=250, y=250)




app.mainloop()
