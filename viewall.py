def create():
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    def add():
        global names, standard, hindi, english, maths, science, SSt, submit
        names.close()
        standard.close()
        hindi.close()
        english.close()
        maths.close()
        science.close()
        SSt.close()
        Stu_data = open("Stu_Data_Files\\Names", "a")
        standard = open("Stu_Data_Files\\standard", "a")
        hindi = open("Stu_Data_Files\\hindi", "a")
        english = open("Stu_Data_Files\\english", 'a')
        maths = open('Stu_Data_Files\\maths', 'a')
        science = open('Stu_Data_Files\\science', 'a')
        SSt = open('Stu_Data_Files\\SSt', 'a')
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

    Label(tk, text="Name :", font=('arial', 14)).place(x=0, y=0)
    Label(tk, text="Class :", font=('arial', 14)).place(x=0, y=45)
    Label(tk, text="Phone :", font=('arial', 14)).place(x=0, y=90)
    Label(tk, text="Hindi :", font=('arial', 14)).place(x=0, y=135)
    Label(tk, text="English :", font=('arial', 14)).place(x=0, y=180)
    Label(tk, text="Maths :", font=('arial', 14)).place(x=0, y=225)
    Label(tk, text="SSt :", font=('arial', 14)).place(x=0, y=270)
    Label(tk, text="Science :", font=('arial', 14)).place(x=0, y=315)
    lab9 = Label(tk, text="Gender:", font=('arial', 15))
    lab9.grid(column=0, row=9)
    e1 = Entry(tk, font=('arial', 13), bd=1).place(x=82, y=0, height=30)
    e2 = Entry(tk, font=('arial', 13), bd=1).place(x=82, y=45, height=30)
    e3 = Entry(tk, font=('arial', 13), bd=1).place(x=82, y=90, height=30)
    e4 = Entry(tk, font=('arial', 13), bd=1).place(x=82, y=135, height=30)
    e5 = Entry(tk, font=('arial', 13), bd=1).place(x=82, y=180, height=30)
    e6 = Entry(tk, font=('arial', 13), bd=1).place(x=82, y=225, height=30)
    e7 = Entry(tk, font=('arial', 13), bd=1).place(x=82, y=270, height=30)
    e8 = Entry(tk, font=('arial', 13), bd=1).place(x=82, y=315, height=30)
    submit = PhotoImage(file="Buttons\\Submit4.png")
    sub = Button(tk, image=submit, command=add, bd=0)
    sub.place(x=200, y=200)
    e9 = Radiobutton(tk)
    e9.grid(column=1, row=9)
    e10 = Checkbutton(tk, borderwidth=5)
    e10.grid(column=2, row=9)
    tk.mainloop()

