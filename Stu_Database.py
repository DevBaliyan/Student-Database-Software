import Stu_Data_Operations
"""
I want to make Roll number on the basis of Alphabets.
For this i will have to make a list take name input and append it
and then use sort method over the list. Using Loop then Find The Roll No.
Make ID which will never be Deleted and will remain same for particular forever

It is to be thought to implement the order of marks on the basis of roll no.
Also, to implement the new order of name and marks in list
"""
"""*********COMMENT-2***********
I need to change a text file into string and store it in variable and to print
specific no. of lines i need to print (number_of_lines+(number_of_lines-1-1)
it is due to when a line breaks it contains some extra command in the form of '\n'.
For further check the code comment-2
"""
ans = 'Do  You want to continue with same?\n1. yes to continue\n2. q to quit'


def task():
    global Op
    Op = str(input('Enter the task to be done\n1. Add new Data(add)\n2. Update Current Data(update)\n'
                   '3. Look for current data(view)\n4. Viewall(all)\n5. Quit(q)\n->'))


def create():
    Stu_Data_Operations.create()
    choice = str(input(ans))
    if choice == 'yes' or choice == '1':
        create()
    else:
        recall()


def update():
    Stu_Data_Operations.update()
    choice = str(input(ans))
    if choice == 'yes' or choice == '1':
        update()
    else:
        recall()


def view():
    Stu_Data_Operations.view()
    choice = str(input(ans))
    if choice == 'yes' or choice == '1':
        view()
    else:
        recall()


def viewall():
    Stu_Data_Operations.viewall()
    recall()


def recall():
    task()
    if Op == 'add' or Op == '1':
        create()
    elif Op == "update" or Op == '2':
        update()
    elif Op == 'view' or Op == '3':
        view()
    elif Op == 'viewall' or Op == '4':
        viewall()
    elif Op == "q" or Op == "5":
        exit(code=None)


recall()
