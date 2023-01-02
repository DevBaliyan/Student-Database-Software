Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class book:
    title = None
    author = None
    publisher = None
    price = None
    ISBN = None
    def getBookDetails(self):
        title = input("Title")
        author = input("Author")
        publisher = input("Publisher")
        price = input("Price")
        ISBN = input("ISBN")
    def display(self):
        print("Title%s"%self.title,self.author, self.publisher, self.price, self.ISBN, sep='\n')

obj = Book()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    obj = Book()
NameError: name 'Book' is not defined. Did you mean: 'book'?
obj = book()
obj.getBookDetails()
TitleTitle
AuthorAuthor
PublisherPub
PriceMoney
ISBN98763287621
obj.display()
TitleNone
None
None
None
None
class book:
    title = None
    author = None
    publisher = None
    price = None
    ISBN = None
    def getBookDetails(self):
        self.title = input("Title")
        self.author = input("Author")
        self.publisher = input("Publisher")
        self.price = input("Price")
        self.ISBN = input("ISBN")
    def display(self):
        print("Title%s"%self.title,self.author, self.publisher, self.price, self.ISBN, sep='\n')

        
obj = book()
obj.getBookDetails()
TitleTitle
AuthorAuthor
PublisherPublisher
PricePrice
ISBNISBN
obj.display()
TitleTitle
Author
Publisher
Price
ISBN
obj.title()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    obj.title()
TypeError: 'str' object is not callable
obj.title
'Title'
def calsum(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return Calsum(n-1)+Calsum(n)

def calsum(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return calsum(n-1)+calsum(n)

print(calsum(10))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(calsum(10))
  File "<pyshell#35>", line 6, in calsum
    return calsum(n-1)+calsum(n)
  File "<pyshell#35>", line 6, in calsum
    return calsum(n-1)+calsum(n)
  File "<pyshell#35>", line 6, in calsum
    return calsum(n-1)+calsum(n)
  [Previous line repeated 1021 more times]
  File "<pyshell#35>", line 2, in calsum
    if n==1:
RecursionError: maximum recursion depth exceeded in comparison
def calsum(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return calsum(n-1)+calsum(n-2)

print(calsum(10))
34
for i in range(1,8):
    print(calsum(i))

    
0
1
1
2
3
5
8
for i in range(1,11):
    print(calsum(i))

    
0
1
1
2
3
5
8
13
21
34
def calsum(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return calsum(n-1)+calsum(n-2)

s = 0
for i in range(1, int(input())+1):
    if i%2==0:
        s+=calsum(i)
    print(calsum(i))

    

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    for i in range(1, int(input())+1):
ValueError: invalid literal for int() with base 10: ''
def calsum(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return calsum(n-1)+calsum(n-2)

for i in range(1, int(input())+1):
    if i%2==0:
        s+=calsum(i)
    print(calsum(i))

    
10
0
1
1
2
3
5
8
13
21
34
def calsum(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return calsum(n-1)+calsum(n-2)

class student:
    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail

    
stu1 = student("Prakhar", 20, 'prakhar@phimale.com')
print("Student 1 details: ", student.name, student.age, student.mail)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print("Student 1 details: ", student.name, student.age, student.mail)
AttributeError: type object 'student' has no attribute 'name'
class student:
    name, age, mail = '', '', ''
    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail

        
print("Student 1 details: ", student.name, student.age, student.mail)
Student 1 details:    
stu1 = student("Prakhar", 20, 'prakhar@phimale.com')
print("Student 1 details: ", stu1.name, stu1.age, stu1.mail)
Student 1 details:  Prakhar 20 prakhar@phimale.com
class student:
    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail

        
print("Student 1 details: ", stu1.name, stu1.age, stu1.mail)
Student 1 details:  Prakhar 20 prakhar@phimale.com
class student:
    def getDetails(self, a, b, c):
        self.name = a
        self.age = b
        self.mail = c
... 
...         
>>> stu1 = student()
>>> stu1 = stu1.getDetails("Prakhar", 20, 'prakhar@phimale.com')
>>> print("Student 1 details: ", stu1.name, stu1.age, stu1.mail)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    print("Student 1 details: ", stu1.name, stu1.age, stu1.mail)
AttributeError: 'NoneType' object has no attribute 'name'
>>> class car:
...     def setName(self, name):
...         self.name = name
...     def getName(self)
...     
SyntaxError: incomplete input
>>> class car:
...     def setName(self, name):
...         self.name = name
...     def getName(self):
...         print(self.name)
... 
...         
>>> obj = car()
>>> car.setName('Honda City')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    car.setName('Honda City')
TypeError: car.setName() missing 1 required positional argument: 'name'
>>> obj.setName('Honda City')
>>> obj.getName()
Honda City
