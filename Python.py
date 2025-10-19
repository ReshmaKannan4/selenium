# age=33
# name="tuttu"
#
# print("hi my name is " ,name, " and my age is " ,age)
#
# list1= ["tuttu", "chittu", "mom", "dad",6]
# list1[4]="resh"
# print(list1)
#
# tup1=("new jersey", "chennai", "varkala")
# print(tup1)
#
# dict1={"curd rice": "vendakka", "upma": "curd"}
# print(dict1["upma"])
#
# x=False
# print(x)
from gettext import dpgettext
from tkinter.font import names


# multi_line="""hi I am Reshma
# I am tuttu's friend
# ok"""
# print(multi_line[1])

# for x in multi_line:
#     print(x)

# if "resh" in multi_line:
#     print("yes")


# test=multi_line[5:10]
# print(test)

#
# a="apple"
# b="apple"
#
# if a is b:
#     print("same")
# else:
#     print("not same")

#
# list1=[1,2,3]
# list2=[4,5,6]
# for i in range(len(list1)):
#     print(i)

# dict1={"Mom":"59","Dad":"64", "Chittu":"10", "tuttu":"33"}
# # print(dict1["tuttu"])
# # print(dict1.keys())
# print(dict1)

# def tuttu(resh):
#     print("my name is",resh)
#
#
# tuttu("prasenna")
# tuttu("reshma")

# class Human:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def body(self):
#         print("test")
#
# tuttu=Human("Reshma",30)
# chittu=Human("Kshe", 10)
# list1=[tuttu,chittu]
# for i in list1:
#     print("my name is" ,i.name, "and age is",i.age)
# b=Human("Prasenna",34)
# b.body()

# def tuttu(a,b):
#     c=a+b
#     return c
#
# d=tuttu(50,60)
# print("sum of a and b",d)


# Create a class Car with attributes brand and year.#
# Add a method display_info() that prints "Brand: <brand>, Year: <year>".#
# Create two objects (Car("Toyota", 2020), Car("Honda", 2018)) and call the method.

# class Car():
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
#     def display_info(self):
#         print("Brand is", self.brand, "year is ", self.year)
#
#
# t1 = Car("Toyota", 2020)
# t1.display_info()
# t2 = Car("Honda", 2018)
# t2.display_info()


# Create a class BankAccount:
# # Attributes: owner, balance.
# Methods:
#deposit(amount) → adds money to balance.
# withdraw(amount) → subtracts if enough balance, else print "Insufficient funds".
# display_balance() → shows the current balance.
# Create an account for "Alice" with balance 1000 and test deposits/withdrawals.

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#
#         self.balance+=amount
#         print("Updated balance is", self.balance)
#
#     def withdraw(self, amount):
#
#         if amount<self.balance:
#             self.balance = self.balance - amount
#             print("withdraw amount is", amount)
#
#         else:
#             print("insufficient balance")
#
#     def display_balance(self):
#         print("current balance is", self.balance)
#
# a = BankAccount("Alice", 1000)
# a.deposit(500)
# a.withdraw(700)
# a.display_balance()


# Write a program to:
# Ask the user for their name and age.
# Print "Hello <name>, you will be <age+5> years old in 5 years!"

# name=input("Enter your name")
# age=int(input("enter your age"))
# age+=5
# print("Hello" ,name, ",you will be" ,age, "years old in 5 years")

# Write a function is_even(n) that returns True if a number is even, and False otherwise.
# Test it with numbers 3, 10, and 25.

# def is_even(n):
#     return n%2==0
#
# print(is_even(3))
# print(is_even(10))
# print(is_even(25))

#Given a list of numbers, print the sum, maximum, and minimum
# without using Python’s built-in sum(), max(), or min().
# list1=[1,2,7,4,5,6]
# def sum(list2):
#     n=0
#     for i in list2:
#         n=n+i
#     return n
# print(sum(list1))
# # #
# # #
# # # #Max
# def Maxi(list2):
#     max1=0
#     for i in list2:
#         if max1<i:
#             max1=i
#     return max1
# print(Maxi(list1))
# #
# # #Min
# def Min(list3):
#     a=list3[0]
#     for i in list3:
#         if a>i:
#             a=i
#     return a
#
# print(Min(list1))

#Print all the numbers from 1 to 50:
# Replace numbers divisible by 3 with "Fizz".
# Replace numbers divisible by 5 with "Buzz".
# Replace numbers divisible by both with "FizzBuzz"

# for i in range(1,51):
#     if (i%3==0) and (i%5==0):
#         i="FizzBuzz"
#         print(i)
#     elif i%5==0:
#         i="Buzz"
#         print(i)
#     elif i%3==0:
#         i="Fizz"
#         print(i)
#     else:
#         print(i)

#Write a program that takes a string and counts how many vowels (a, e, i, o, u) it has.

# def name(str1):
#     count=0
#     vow = "aeiou"
#     for i in str1:
#         if i in vow:
#             count+=1
#     print("Number of vowels in your string is", count)
# name("chittu")

#Write a function reverse_string(s) that returns the reversed version of s.
#Example: "python" → "nohtyp"

# def reverse(str1):
#     list1=list(str1)
#     list1.reverse()
#     #print(list1)
#     str1="".join(list1)
#     return str1
#
# print(reverse("tuttu"))

#Write a function is_palindrome(word) that returns True if the word reads the same
# # backward and forward.
# def palindrome(word):
#
#     list1 = list(word)
#     list2=list((list1))
#     list2.reverse()
#
#
#     if list1==list2:
#         print("String is a palindrome")
#     else:
#         print("not a palindrome")
#
# palindrome("malayalam")

#Create a class Rectangle:
# Attributes: width, height.
# Methods:
# area() → returns area.
# perimeter() → returns perimeter.
# Create a rectangle 5x10 and print area and perimeter.

# class Rectangle:
#     def __init__(self,width, height):
#         self.width=width
#         self.height=height
#
#     def area(self):
#         return self.width*self.height
#
#     def perimeter(self):
#         return 2*(self.width+self.height)
#
# a=Rectangle(15,10)
# print(a.area())
# print(a.perimeter())

#Create a class Student with:
# Attributes: name, grades (a list).
# Methods:
# add_grade(grade) → adds a grade.
# average() → returns average grade.
# Create a student, add 3–4 grades, and print average

# class Student:
#     def __init__(self,name,grades):
#         self.name=name
#         self.grades=grades
#
#     def add_grade(self):
#
#          self.total= sum(self.grades)
#
#
#     def average(self):
#         self.add_grade()
#         return self.total/len(self.grades)
#
    #
# a=Student("Kshethra",[99,98,97,96])
# print(a.name)
# print(a.add_grade())
# print(a.average())

#Create a simple class Book with attributes: title, author, year.
# Make a list of Book objects (like a mini library).
# Write a function that prints all books published after 2010.

# class Book:
#     def __init__(self, title, author, year):
#         self.title=title
#         self.author=author
#         self.year=year
#
# book=[Book("OneGoldenSummer","Carley Fortune",2020),
#       Book("BlueSisters","Coco mellors",2009),
#       Book("Donotdisturb","Frieda mcfadden",2011),
#       Book("Tenant","Frieda mcfadden",2001)]
# def print_books():
#     list2 = []
#     for i in book:
#         if i.year > 2010:
#             list2.append(i.title)
# print("Books published after 2010 are", list2)
# print_books()


# Word Frequency Counter
# Take a string input and print how many times each word appears.
# Example:
# "the cat and the dog" → {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}

# def counter(str1):
#     str2=str1.split()
#     dict1={}
#     for i in str2:
#         dict1.update({i: str2.count(i)})
#     print(dict1)
#
# counter("the cat and the dog")

# Unique Elements
# Write a function unique_elements(lst)
# that returns a new list with only unique values from the given list.

# def unique1(list1):
#     list2=[]
#
#     for i in list1:
#         if i not in list2:
#             list2.append(i)
#     print(list2)
#
# unique1([1,4,6,2,1,3,2,2,1,6,10,11,90])

# Library System (Basic)
# Create a class Book with attributes: title, author, year.
# Then create a class Library that stores books in a list and has methods:
# add_book(book)
# display_books()
# Test by adding 3 books and displaying them.

# class Book:
#     def __init__(self,title,author,year):
#         self.title=title
#         self.author=author
#         self.year=year
#
# class Library:
#
#     def __init__(self):
#         self.book_list=[]
#
#     def add_book(self,book):
#         self.book_list.append(book.title)
#         self.book_list.append(book.author)
#         self.book_list.append(book.year)
#
#     def display_books(self):
#         print("Books are", self.book_list)
#
# books=[Book("book1","author1", 2023),
#       Book("book2","author2", 2024),
#       Book("book3","author3", 2025)]
# a=Library()
# a.add_book(books[0])
# a.add_book(books[1])
# a.add_book(books[2])
# a.display_books()


#Employee Management
# Create a class Employee with attributes name, salary.
# Add a method give_raise(amount) that increases salary.
# Create 2–3 employees and give them raises.

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
#     def give_raise(self,amount):
#         self.amount=amount
#         raise_for_employee=self.salary+self.amount
#         print("Raise for employee",self.name, "is" ,raise_for_employee)
#
# employee1=Employee("Reshma",15000)
# employee2=Employee("Prasenna",12000)
# employee1.give_raise(50000)
# employee2.give_raise(100)

#Shopping Cart
# Create classes:
# Item(name, price)
# Cart() with methods:
# add_item(item)
# total() → returns total price.
# Add 3 items and print the total cost.
#
# class Item:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#
# class Cart:
#     def __init__(self):
#         self.item_list=[]
#         self.total_price=0
#
#     def add_item(self,item):
#         self.item_list.append(item.price)
#         self.total_price=sum(self.item_list)
#
#     def total(self):
#         print("The total price of all items are",self.total_price )
#
# item1=Item("box",40)
# item2=Item("apple", 90)
# item3=Item("airpods",12000)
#
# c=Cart()
# c.add_item(item1)
# c.add_item(item2)
# c.add_item(item3)
# c.total()

# Prime Numbers
# Write a function is_prime(n) that returns True if n is a prime number.
# Then print all prime numbers between 1 and 100.

# def prime():
#     for i in range(2,101): #prime numbers
#         for j in range(2,i+1): #divisors
#             if i!=j and i%j==0:
#                 break
#             if i==j:
#                 print(i)
# prime()

# Student Grading
# Create a class Student with attributes: name, marks (a dictionary with subject → score).
# Methods:
# add_mark(subject, score)
# average()
# display_report() → prints "Math: 90, Science: 85 ... Average: 87.5".

# class Student:
#     def __init__(self, name):
#         self.name=name
#         self.marks={}
#
#     def add_mark(self,subject,score):
#         marks[subject]=score
#
#     def average(self):
#         total=sum(marks.values())
#         self.avg=total/len(marks.values())
#
#
#     def display_report(self):
#         marks["Average"]=self.avg
#         print(marks)
#
# marks={}
# student=Student("Chittu")
# student.add_mark("Social",99)
# student.add_mark("English",95)
# student.add_mark("Math",100)
# student.add_mark("Science",98)
# student.average()
# student.display_report()

# Bank with Multiple Accounts
# Extend the earlier BankAccount class:
# Add a Bank class that stores multiple accounts in a dictionary (owner → account).
# Methods: add_account(account), transfer(from_owner, to_owner, amount).

# class BankAccount:
#
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance+=amount
#         print("Updated balance is", self.balance)
#
#     def withdraw(self, amount):
#         if amount<self.balance:
#             self.balance = self.balance - amount
#             print("withdraw amount is", amount)
#         else:
#             print("insufficient balance")
#
#     def display_balance(self):
#         print("current balance is", self.balance)
#
# class Bank:
#     def __init__(self):
#         self.dict1 = {}
#
#     def add_account(self,account):
#         self.dict1[account.owner]=account
#
#     def transfer(self, from_owner, to_owner, amount):
#         name=self.dict1[from_owner]
#         name2=self.dict1[to_owner]
#         name.balance-=amount
#         name2.balance+=amount
#
# a = BankAccount("Alice", 1000)
# b= BankAccount("Chittu",5000)
# a.deposit(500)
# a.withdraw(700)
# a.display_balance()
# b.display_balance()
# bank=Bank()
# bank.add_account(a)
# bank.add_account(b)
# bank.transfer("Alice","Chittu",500)
# a.display_balance()
# b.display_balance()

# Create a class Circle with:
# Attribute: radius.
# Methods:
# area() → returns area (π * r^2).
# circumference() → returns circumference (2 * π * r).
# scale(factor) → multiplies radius by factor.
# Create two circles, print their area and circumference, then scale one and check results again.
# Practice Goal: Using math inside methods + changing object state.

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#
#     def area(self):
#         area_of_a_circle=3.14*self.radius*self.radius
#         print("Area is",area_of_a_circle)
#
#     def circumference(self):
#         circum_of_a_circle=2*3.14*self.radius
#         print("Circumference is", circum_of_a_circle)
#
#     def scale(self, factor):
#         self.radius*=factor
#         print("Radius of the circle is resized to", self.radius)
#
# circle1=Circle(5)
# circle2=Circle(10)
# circle1.area()
# circle2.area()
# circle1.circumference()
# circle2.circumference()
# circle1.scale(2)
# circle1.area()
# circle1.circumference()

# Create a class Task with:
# Attributes: title, completed (default = False).
# Methods:
# mark_done() → marks the task as completed.
# __str__() → returns "Task: <title> [Done]" or "Task: <title> [Not Done]".
# Create a class TodoList with:
# Attribute: a list of tasks.
# Methods:
# add_task(title) → creates a new Task and adds it.
# show_tasks() → prints all tasks.

# class Task:
#     def __init__(self, title):
#         self.title=title
#         self.completed=False
#
#     def mark_done(self):
#         self.completed=True
#
#     def __str__(self):
#         if(self.completed==True):
#             print(self.title,"Done")
#         else:
#             print(self.title,"Not Done")
#
# class TodoList:
#     def __init__(self):
#         self.list_of_tasks=[]
#
#     def add_task(self,title):
#         task = Task(title)
#         self.list_of_tasks.append(task)
#
#     def show_tasks(self):
#         for i in self.list_of_tasks:
#             print(i.title)
#
# todolist1=TodoList()
# todolist1.add_task("Get Milk")
# todolist1.show_tasks()

# Create a class Temperature with:
# Attribute: celsius.
# Methods:
# to_fahrenheit()
# to_kelvin()
# Test with a few values

# class Temperature:
#     def __init__(self,celsius):
#         self.celsius=celsius
#
#     def to_fahrenheit(self):
#         farenheit=(self.celsius*1.8)+32
#         print(farenheit)
#
#     def to_kelvin(self):
#         kelvin=self.celsius+273.15
#         print(kelvin)
#
# c=Temperature(50)
# c.to_fahrenheit()
# c.to_kelvin()

# Create a class Board with:
# A 3x3 list to represent the grid.
# display() → prints the board in a nice format.
# place_mark(row, col, mark) → puts 'X' or 'O'

# class Board:
#     def __init__(self):
#         self.list1=[["","",""],
#                     ["","",""],
#                     ["","",""]]
#
#     def place_mark(self,row,col,mark):
#         self.list1[row][col]=mark
#
#     def display(self):
#         print("The Board is",self.list1)
#
# b=Board()
# b.place_mark(0,0,"X")
# b.place_mark(0,1,"0")
# b.place_mark(0,2,"0")
# b.place_mark(1,0,"0")
# b.place_mark(1,1,"X")
# b.place_mark(1,2,"0")
# b.place_mark(2,0,"0")
# b.place_mark(2,1,"0")
# b.place_mark(2,2,"X")
# b.display()

# Create a class Teacher with attributes:name
# department
# Method __str__() → "Teacher: <name> (<department>)"
# Create a class Course with attributes:
# title
# teacher (this should be a Teacher object)
# students (an initially empty list).
# Methods:
# add_student(name) → adds a student to the list.
# course_info() → prints:"Course: <title> | Teacher: <teacher.name> | Students: <students list>".
# Create one teacher and two courses for that teacher.
# Add some students to each course and display the course info.

# class Teacher:
#     def __init__(self,name, department):
#         self.name=name
#         self.department=department
#
#     def __str__(self):
#         return "Teacher: "+self.name+" dept is "+self.department
#
# class Course:
#     def __init__(self,title):
#         self.title=title
#         self.student=[]
#
#
#     def add_student(self,name):
#         self.student.append(name)
#
#
#     def course_info(self):
#
#         teacher = Teacher("Uma Maheshwari", "Math")
#         print(str(teacher))
#         print("Course info",self.title,"Teacher",teacher.name,"Student list",self.student)
#
# c=Course("Algebra and Geometry")
# c.add_student("Chittu")
# c.add_student("Tuttu")
# c.course_info()

# Create a class Review with attributes:
# reviewer
# rating (0–10)
# comment
# Method __str__() → "Reviewer: <reviewer>, Rating: <rating>/10, Comment: <comment>".
# Create a class Movie with attributes:
# title
# year
# reviews (an empty list initially).
# Methods:
# add_review(review_obj) → adds a Review object to the list.
# average_rating() → returns the average of all ratings.
# show_reviews() → prints all reviews.
# Create one movie and add 2–3 reviews using Review objects, then print the average rating and all reviews.

# class Review:
#     def __init__(self,reviewer,rating,comment):
#         self.reviewer=reviewer
#         self.rating=rating
#         self.comment=comment
#
#     def __str__(self):
#         return "Reviewer: "+self.reviewer+ " Rating: " +str(self.rating)+ " Comment: "+self.comment
#
# class Movie:
#     def __init__(self,title,year):
#         self.title=title
#         self.year=year
#         self.reviews=[]
#         self.list1=[]
#
#     def add_review(self,review):
#         self.reviews.append(review)
#
#     def average_rating(self):
#         for i in self.reviews:
#             self.list1.append(i.rating)
#         total=sum(self.list1)
#         avg=total/len(self.reviews)
#         return avg
#
#     def show_reviews(self):
#         for i in self.reviews:
#             print(str(i))
#
# review1=Review("tuttu",9.8,"best movie")
# review2=Review("resh",7,"okayish")
# review3=Review("chittu",8,"nice")
# m=Movie("The Matrix",1999)
# m.add_review(review1)
# m.add_review(review2)
# m.add_review(review3)
# m.show_reviews()
# print(m.average_rating())
