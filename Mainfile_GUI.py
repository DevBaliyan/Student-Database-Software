from tkinter import *
import greet


greet.entry()


names = open("Stu_Data_Files\\Names.txt", 'r')
standard = open("Stu_Data_Files\\standard.txt", "r")
hindi = open("Stu_Data_Files\\hindi.txt", 'r')
english = open('Stu_Data_Files\\english.txt', 'r')
maths = open('Stu_Data_Files\\maths.txt', 'r')
science = open('Stu_Data_Files\\science.txt', 'r')
SSt = open('Stu_Data_Files\\SSt.txt', 'r')
name_l, std_l, hin_l, eng_l, mat_l, sci_l, sst_l = [], [], [], [], [], [], []
recipients = 0
for i in names:
    recipients += 1
    name_l.append(i)
for i in standard:
    std_l.append(i)
for i in hindi:
    hin_l.append(i)
for i in english:
    eng_l.append(i)
for i in maths:
    mat_l.append(i)
for i in science:
    sci_l.append(i)
for i in SSt:
    sst_l.append(i)
r = 1


def create():
    def add():
        global names, standard, hindi, english, maths, science, SSt, submit
        names.close()
        standard.close()
        hindi.close()
        english.close()
        maths.close()
        science.close()
        SSt.close()
        Stu_data = open("Stu_Data_Files\\Names.txt", "a")
        standard = open("Stu_Data_Files\\standard.txt", "a")
        hindi = open("Stu_Data_Files\\hindi.txt", "a")
        english = open("Stu_Data_Files\\english.txt", 'a')
        maths = open('Stu_Data_Files\\maths.txt', 'a')
        science = open('Stu_Data_Files\\science.txt', 'a')
        SSt = open('Stu_Data_Files\\SSt.txt', 'a')
        name = e1.get()
        std = e2.get()
        hin, eng, mat, sst, sci = e4.get(), e5.get(), e6.get(), e7.get(), e8.get()
        Stu_data.write("\n" + name)
        standard.write("\n" + std)
        hindi.write("\n" + hin)
        english.write("\n" + eng)
        maths.write("\n" + mat)
        SSt.write("\n" + sst)
        science.write("\n" + sci)
        tk.destroy()
    b1.destroy(), b2.destroy(), b3.destroy(), b4.destroy()
    Label(tk, text="Name :", font=('arial', 14), bg='#566573').place(x=0, y=20)
    Label(tk, text="Class :", font=('arial', 14), bg='#566573').place(x=0, y=65)
    Label(tk, text="Phone :", font=('arial', 14), bg='#566573').place(x=0, y=110)
    Label(tk, text="Hindi :", font=('arial', 14), bg='#566573').place(x=0, y=155)
    Label(tk, text="English :", font=('arial', 14), bg='#566573').place(x=0, y=200)
    Label(tk, text="Maths :", font=('arial', 14), bg='#566573').place(x=0, y=245)
    Label(tk, text="SSt :", font=('arial', 14), bg='#566573').place(x=0, y=290)
    Label(tk, text="Science :", font=('arial', 14), bg='#566573').place(x=0, y=335)
    e1 = Entry(tk, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=20, height=30)
    e2 = Entry(tk, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=65, height=30)
    e3 = Entry(tk, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=110, height=30)
    e4 = Entry(tk, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=155, height=30)
    e5 = Entry(tk, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=200, height=30)
    e6 = Entry(tk, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=245, height=30)
    e7 = Entry(tk, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=290, height=30)
    e8 = Entry(tk, font=('arial', 13), bd=1, bg='#566573').place(x=82, y=335, height=30)
    submit = PhotoImage(file="Buttons\\Submit4.png")
    sub = Button(tk, image=submit, command=add, bd=0, bg='#566573')
    sub.place(x=330, y=450)
    tk.mainloop()


def update():
    b1.destroy(), b2.destroy(), b3.destroy(), b4.destroy()
    names.close()
    standard.close()
    hindi.close()
    english.close()
    maths.close()
    science.close()
    SSt.close()

    def new():
        def up():
            name, std = e1.get(), e2.get()
            hin, eng, mat, sst, sci = e4.get(), e5.get(), e6.get(), e7.get(), e8.get()
            name, std, hin, eng = name, std, eval(hin), eval(eng)
            mat, sst, sci = eval(mat), eval(sst), eval(sci)
            if r < recipients:
                name_l[r - 1] = name + '\n'
                std_l[r - 1] = std + '\n'
                hin_l[r - 1] = str(hin) + '\n'
                eng_l[r - 1] = str(eng) + '\n'
                sci_l[r - 1] = str(sci) + '\n'
                sst_l[r - 1] = str(sst) + '\n'
                mat_l[r - 1] = str(mat) + '\n'
            elif r == recipients:
                name_l[r - 1] = name
                std_l[r - 1] = std
                hin_l[r - 1] = str(hin)
                eng_l[r - 1] = str(eng)
                sci_l[r - 1] = str(sci)
                sst_l[r - 1] = str(sst)
                mat_l[r - 1] = str(mat)
            a, b, c, d, e, f, g = '', '', '', '', '', '', ''
            for j in name_l:
                if j == r:
                    a += name + '\n'
                else:
                    a += j
            for j in std_l:
                if j == r:
                    b += std + '\n'
                else:
                    b += j
            for j in hin_l:
                if j == r:
                    c += str(hin) + '\n'
                else:
                    c += j
            for j in eng_l:
                if j == r:
                    d += str(eng) + '\n'
                else:
                    d += j
            for j in mat_l:
                if j == r:
                    e += str(mat) + '\n'
                else:
                    e += j
            for j in sci_l:
                if j == r:
                    f += str(sci) + '\n'
                else:
                    f += j
            for j in sst_l:
                if j == r:
                    g += str(sst) + '\n'
                else:
                    g += j
            names = open("Stu_Data_Files\\Names.txt", 'w')
            standard = open("Stu_Data_Files\\standard.txt", "w")
            hindi = open("Stu_Data_Files\\hindi.txt", 'w')
            english = open('Stu_Data_Files\\english.txt', 'w')
            maths = open('Stu_Data_Files\\maths.txt', 'w')
            science = open('Stu_Data_Files\\science.txt', 'w')
            SSt = open('Stu_Data_Files\\SSt.txt', 'w')
            names.write(a)
            standard.write(b)
            hindi.write(c)
            english.write(d)
            maths.write(e)
            science.write(f)
            SSt.write(g)
            names.close()
            standard.close()
            hindi.close()
            english.close()
            maths.close()
            science.close()
            SSt.close()
            tk.destroy()

        r = rol.get()
        r = eval(r)
        roll_no.destroy(), sub.destroy(), rol.destroy()
        Label(tk, text="Name :", font=('arial', 14), bg='#566573').place(x=0, y=20)
        Label(tk, text="Class :", font=('arial', 14), bg='#566573').place(x=0, y=65)
        Label(tk, text="Phone :", font=('arial', 14), bg='#566573').place(x=0, y=110)
        Label(tk, text="Hindi :", font=('arial', 14), bg='#566573').place(x=0, y=155)
        Label(tk, text="English :", font=('arial', 14), bg='#566573').place(x=0, y=200)
        Label(tk, text="Maths :", font=('arial', 14), bg='#566573').place(x=0, y=245)
        Label(tk, text="SSt :", font=('arial', 14), bg='#566573').place(x=0, y=290)
        Label(tk, text="Science :", font=('arial', 14), bg='#566573').place(x=0, y=335)
        e1 = Entry(tk, font=('arial', 13), bd=1, bg='#566573')
        e1.place(x=82, y=20, height=30)
        e2 = Entry(tk, font=('arial', 13), bd=1, bg='#566573')
        e2.place(x=82, y=65, height=30)
        e3 = Entry(tk, font=('arial', 13), bd=1, bg='#566573')
        e3.place(x=82, y=110, height=30)
        e4 = Entry(tk, font=('arial', 13), bd=1, bg='#566573')
        e4.place(x=82, y=155, height=30)
        e5 = Entry(tk, font=('arial', 13), bd=1, bg='#566573')
        e5.place(x=82, y=200, height=30)
        e6 = Entry(tk, font=('arial', 13), bd=1, bg='#566573')
        e6.place(x=82, y=245, height=30)
        e7 = Entry(tk, font=('arial', 13), bd=1, bg='#566573')
        e7.place(x=82, y=290, height=30)
        e8 = Entry(tk, font=('arial', 13), bd=1, bg='#566573')
        e8.place(x=82, y=335, height=30)
        e1.insert(0, name_l[r - 1])
        e2.insert(0, std_l[r - 1])
        e4.insert(0, hin_l[r - 1])
        e5.insert(0, eng_l[r - 1])
        e6.insert(0, mat_l[r - 1])
        e7.insert(0, sci_l[r - 1])
        e8.insert(0, sst_l[r - 1])
        submit = PhotoImage(file="Buttons\\Submit4.png")
        sub1 = Button(tk, image=submit, command=new, bg='#566573', bd=0)
        sub1.place(x=330, y=450)
        tk.mainloop()
    roll_no = Label(tk, text="Roll code", font=('arial', 20), bg='#566573',
                    bd=0, foreground='#6633FF')
    roll_no.place(x=150, y=120)
    rol = Entry(tk, bg='#566573', font=('arial', 16))
    rol.place(x=130, y=200, width=150, height=35)
    submit = PhotoImage(file="Buttons\\next.png")
    sub = Button(tk, image=submit, command=new, bg='#566573', bd=0)
    sub.place(x=330, y=450)
    tk.mainloop()


def view():
    def new():
        r = rol.get()
        r = eval(r)
        roll_no.destroy(), rol.destroy(), sub.destroy()
        Label(tk, text="Name").grid(column=0, row=1)
        Label(tk, text="Class").grid(column=0, row=2)
        Label(tk, text="Phone Number").grid(column=0, row=3)
        Label(tk, text="Hindi").grid(column=0, row=4)
        Label(tk, text="English").grid(column=0, row=5)
        Label(tk, text="Maths").grid(column=0, row=6)
        Label(tk, text="SSt").grid(column=0, row=7)
        Label(tk, text="Science").grid(column=0, row=8)
        e1 = Entry(tk)
        e1.insert(0, name_l[r - 1])
        e1.grid(column=1, row=1)
        e2 = Entry(tk)
        e2.insert(0, std_l[r - 1])
        e2.grid(column=1, row=2)
        e3 = Entry(tk)
        e3.grid(column=1, row=3)
        e4 = Entry(tk)
        e4.insert(0, hin_l[r - 1])
        e4.grid(column=1, row=4)
        e5 = Entry(tk)
        e5.insert(0, eng_l[r - 1])
        e5.grid(column=1, row=5)
        e6 = Entry(tk)
        e6.insert(0, mat_l[r - 1])
        e6.grid(column=1, row=6)
        e7 = Entry(tk)
        e7.insert(0, sst_l[r - 1])
        e7.grid(column=1, row=7)
        e8 = Entry(tk)
        e8.insert(0, sci_l[r - 1])
        e8.grid(column=1, row=8)
        sub1 = Button(tk, text='submit', command=tk.destroy)
        sub1.place(x=300, y=300)
        e1.configure(state='disabled'), e2.configure(state='disabled')
        e2.configure(state='disabled'), e4.configure(state='disabled')
        e5.configure(state='disabled'), e6.configure(state='disabled')
        e7.configure(state='disabled'), e8.configure(state='disabled')

    tk = Tk()
    tk.minsize(height=200, width=250)
    roll_no = Label(tk, text="Roll code")
    roll_no.place(x=95, y=10)

    rol = Entry(tk)
    rol.place(x=70, y=50, width=100)
    sub = Button(tk, text='submit', command=new)
    sub.grid()

    tk.mainloop()


def viewall():
    def inc():
        global r
        if r < recipients:
            r += 1
            e1 = Entry(tk)
            e1.insert(0, name_l[r - 1])
            e1.grid(column=1, row=1)
            e2 = Entry(tk)
            e2.insert(0, std_l[r - 1])
            e2.grid(column=1, row=2)
            e3 = Entry(tk)
            e3.grid(column=1, row=3)
            e4 = Entry(tk)
            e4.insert(0, hin_l[r - 1])
            e4.grid(column=1, row=4)
            e5 = Entry(tk)
            e5.insert(0, eng_l[r - 1])
            e5.grid(column=1, row=5)
            e6 = Entry(tk)
            e6.insert(0, mat_l[r - 1])
            e6.grid(column=1, row=6)
            e7 = Entry(tk)
            e7.insert(0, sst_l[r - 1])
            e7.grid(column=1, row=7)
            e8 = Entry(tk)
            e8.insert(0, sci_l[r - 1])
            e8.grid(column=1, row=8)
            e1.configure(state='disabled'), e2.configure(state='disabled')
            e2.configure(state='disabled'), e4.configure(state='disabled')
            e5.configure(state='disabled'), e6.configure(state='disabled')
            e7.configure(state='disabled'), e8.configure(state='disabled')
        if r == recipients:
            sub1.configure(command='bell')

    tk = Tk()
    tk.minsize(height=350, width=400)
    Label(tk, text="Name").grid(column=0, row=1)
    Label(tk, text="Class").grid(column=0, row=2)
    Label(tk, text="Phone Number").grid(column=0, row=3)
    Label(tk, text="Hindi").grid(column=0, row=4)
    Label(tk, text="English").grid(column=0, row=5)
    Label(tk, text="Maths").grid(column=0, row=6)
    Label(tk, text="SSt").grid(column=0, row=7)
    Label(tk, text="Science").grid(column=0, row=8)
    e1 = Entry(tk)
    e1.insert(0, name_l[r - 1])
    e1.grid(column=1, row=1)
    e2 = Entry(tk)
    e2.insert(0, std_l[r - 1])
    e2.grid(column=1, row=2)
    e3 = Entry(tk)
    e3.grid(column=1, row=3)
    e4 = Entry(tk, text=hin_l[r - 1])
    e4.insert(0, hin_l[r - 1])
    e4.grid(column=1, row=4)
    e5 = Entry(tk)
    e5.insert(0, eng_l[r - 1])
    e5.grid(column=1, row=5)
    e6 = Entry(tk)
    e6.insert(0, mat_l[r - 1])
    e6.grid(column=1, row=6)
    e7 = Entry(tk)
    e7.insert(0, sst_l[r - 1])
    e7.grid(column=1, row=7)
    e8 = Entry(tk)
    e8.insert(0, sci_l[r - 1])
    e8.grid(column=1, row=8)
    e1.configure(state='disabled'), e2.configure(state='disabled')
    e2.configure(state='disabled'), e4.configure(state='disabled')
    e5.configure(state='disabled'), e6.configure(state='disabled')
    e7.configure(state='disabled'), e8.configure(state='disabled')
    sub1 = Button(tk, text='submit', command=inc)
    sub1.place(x=300, y=300)

    tk.mainloop()


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


tk = Tk()
tk.geometry('450x500')
tk.resizable(0, 0)
tk.title('Stu_Data')
tk.configure(bg='#566573')
tk.iconbitmap('icon.ico')

la = Label(tk, bg='#566573')
la.grid()
f = Frame(tk, height=449, width=449)
b1 = Button(tk, text="create", command=create, bd=0, cursor='hand2', activebackground='#566573',
            font=('arial', 15), bg='#566573', activeforeground='#6665FF')
b1.place(x=5, y=5)
b2 = Button(tk, text="update", command=update, bd=0, cursor='hand2',
            font=('arial', 15), bg='#566573', activebackground='#566573', activeforeground='#6665FF')
b2.place(x=5, y=60)
b3 = Button(tk, text='view', command=view, cursor='hand2', bd=0,
            font=('arial', 15), bg='#566573', activebackground='#566573', activeforeground='#6665FF')
b3.place(x=5, y=115)
b4 = Button(tk, text='viewall', command=viewall, cursor='hand2',
            bd=0, font=('arial', 15), bg='#566573', activebackground='#566573', activeforeground='#6665FF')
b4.place(x=5, y=170)


tk.mainloop()
