"""
I think it is not the proper solution for update as it increases the lines
by many lines. So, update function is to be made
self indicating type name, std, etc
change pass new value

string-List-string-text
Firstly fetch all the elements from text file
Second - Store The elements in the lists
Third - Change the particular element in the lists obtained above
Fourth - Stored the value in the form of string by adding all the elements of the
lists with the help of loop
Last - Created a new text file and add the string to it
what is ambiguous variable
"""
names = open("Stu_Data_Files\\Names.txt", 'r')
standard = open("Stu_Data_Files\\standard.txt", "r")
hindi = open("Stu_Data_Files\\hindi.txt", 'r')
english = open('Stu_Data_Files\\english.txt', 'r')
maths = open('Stu_Data_Files\\maths.txt', 'r')
science = open('Stu_Data_Files\\science.txt', 'r')
SSt = open('Stu_Data_Files\\SSt.txt', 'r')
name_l, std_l, hin_l, eng_l, mat_l, sci_l, sst_l = [], [], [], [], [], [], []
ans = "Do You Want To Continue With Same or Not\n1.If continue press enter\n2.Or if not press 'q'"
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


print('Total  :-', recipients)


def create():
    global names, standard, hindi, english, maths, science, SSt
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
    name = str(input('Enter Your Name\n->'))
    std = str(input('In which class do you read\n->'))
    hin = str(input("Enter Your Marks in Hindi\n->"))
    eng = str(input("Enter Your Marks in English\n->"))
    math = str(input("Enter Your Marks in Maths\n->"))
    sci = str(input("Enter Your Marks in Science\n->"))
    sst = str(input("Enter Your Marks in SSt\n->"))
    Stu_data.write("\n" + name)
    standard.write("\n" + std)
    hindi.write("\n" + hin)
    english.write("\n" + eng)
    maths.write("\n" + math)
    SSt.write("\n" + sst)
    science.write("\n" + sci)
    names.close()
    standard.close()
    hindi.close()
    english.close()
    maths.close()
    science.close()
    SSt.close()


def update():
    global a, b, c, d, e, f, g, names, standard, hindi, english, maths, science, SSt
    global name_l, std_l, hin_l, eng_l, mat_l, sci_l, sst_l, l
    a, b, c, d, e, f, g = '', '', '', '', '', '', ''
    roll = int(input('Enter Your Roll Number\n->'))
    nam = str(input('Enter Your Name\n->'))
    cls = str(input("In which class do you read\n->"))
    hin = int(input('Enter Your Marks in Hindi\n->'))
    eng = int(input('Enter Your Marks in English\n->'))
    mat = int(input('Enter Your Marks in Maths\n->'))
    sci = int(input('Enter Your Marks in Science\n->'))
    sst = int(input('Enter Your Marks in S.St\n->'))
    if roll < recipients:
        name_l[roll-1] = nam+'\n'
        std_l[roll-1] = cls+'\n'
        hin_l[roll-1] = str(hin)+'\n'
        eng_l[roll-1] = str(eng)+'\n'
        sci_l[roll-1] = str(sci)+'\n'
        sst_l[roll-1] = str(sst)+'\n'
        mat_l[roll-1] = str(mat)+'\n'
    elif roll == recipients:
        name_l[roll - 1] = nam
        std_l[roll - 1] = cls
        hin_l[roll - 1] = str(hin)
        eng_l[roll - 1] = str(eng)
        sci_l[roll - 1] = str(sci)
        sst_l[roll - 1] = str(sst)
        mat_l[roll - 1] = str(mat)
    # remaining 6 elements
    names.close()
    standard.close()
    hindi.close()
    english.close()
    maths.close()
    science.close()
    SSt.close()
    for j in name_l:
        if j == roll:
            a += nam + '\n'
        else:
            a += j
    for j in std_l:
        if j == roll:
            b += cls + '\n'
        else:
            b += j
    for j in hin_l:
        if j == roll:
            c += str(hin) + '\n'
        else:
            c += j
    for j in eng_l:
        if j == roll:
            d += str(eng) + '\n'
        else:
            d += j
    for j in mat_l:
        if j == roll:
            e += str(mat) + '\n'
        else:
            e += j
    for j in sci_l:
        if j == roll:
            f += str(sci) + '\n'
        else:
            f += j
    for j in sst_l:
        if j == roll:
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


def view():
    roll = int(input('Enter Your Roll Code\n->'))
    print('Name:-', name_l[roll-1], end='')
    print('Class:-', std_l[roll - 1], end='')
    print('Marks in Hindi:-', hin_l[roll - 1], end='')
    print('Marks in English:-', eng_l[roll - 1], end='')
    print('Marks in Maths:-', mat_l[roll - 1], end='')
    print('Marks in Science:-', sci_l[roll - 1], end='')
    print('Marks in S.St:-', sst_l[roll - 1], end='')
    names.close()
    standard.close()
    hindi.close()
    english.close()
    maths.close()
    science.close()
    SSt.close()


def viewall():
    for k in range(recipients):
        print('Name:-', name_l[k - 1], end='')
        print('Class:-', std_l[k - 1], end='')
        print('Marks in Hindi:-', hin_l[k - 1], end='')
        print('Marks in English:-', eng_l[k - 1], end='')
        print('Marks in Maths:-', mat_l[k - 1], end='')
        print('Marks in Science:-', sci_l[k - 1], end='')
        print('Marks in S.St:-', sst_l[k - 1])
    names.close()
    standard.close()
    hindi.close()
    english.close()
    maths.close()
    science.close()
    SSt.close()
