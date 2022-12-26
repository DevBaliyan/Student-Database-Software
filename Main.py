import tkinter as tk
from time import sleep


def destroy_everything(*exception):
    for child in app.winfo_children():
        if child in exception:
            continue
        else:
            child.destroy()

    
def welcome_page_2():
    name = text_box.get()
    label_main.configure(text="\n\nHello! " + name + "\n\nWelcome To Students Database", bg='#566573')
    destroy_everything(label_main)
    tk.Button(app, image=next_btn_img, command=destroy_everything, bg='#566573',
              activebackground='#566573', bd=0).place(x=250, y=250)
    tk.Label(app, text='click next to continue to database', font=('arial', 13), bg='#566573').place(x=170, y=200)


def main_application_page():
        pass


# app- Application Attributes
app = tk.Tk()
app.title('Greetings')
app.minsize(height=350, width=600)
app.maxsize(height=350, width=600)
app.configure(background='#566573')


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
