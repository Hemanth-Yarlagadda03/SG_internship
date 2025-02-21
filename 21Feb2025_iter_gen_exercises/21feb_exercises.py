# -*- coding: utf-8 -*-
"""21Feb-Exercises.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jf0DDRUdeUZt2DwwaF3f6_71BVyF2BC_

# Class and Static Methods
"""

# class methods- implemented to act as a alternate constructor and a method to change class variable
class Employee:
    roles = {"VP": 500000, "Manager": 150000, "Intern": 30000}

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.salary = self.roles.get(role, 0)

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["role"])

    @classmethod
    def update_salary(cls, role, new_salary):

        if role in cls.roles:
            cls.roles[role] = new_salary
        else:
            print(f"Role '{role}' not found.")

dict1 = {"name": "Hem", "role": "Intern"}
emp1 = Employee.from_dict(dict1)
emp2 = Employee("Lakshman", "Manager")

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)
Employee.update_salary("Intern", 50000)
emp3 = Employee("Yarlagadda", "Intern")

print(emp3.name, emp3.salary)

# static methods
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('Ram', 21)
person2 = Person.fromBirthYear('Raj',2003)

print(person1.age)
print(person2.age)

print(Person.isAdult(14))

#__new__
class PositiveNumber:
    def __new__(cls, value):
        if value <= 0:
            raise ValueError("Value must be positive!")
        return super().__new__(cls)

    def __init__(self, value):
        self.value = value

num1 = PositiveNumber(10)
print(num1.value)

try:
    num2 = PositiveNumber(-5)
except ValueError as e:
    print("Error:", e)

#__new__

class ImmutableConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, setting):
        if not self.__initialized:
            object.__setattr__(self, "setting", setting)
            object.__setattr__(self, "__initialized", True)

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise AttributeError("Cannot modify immutable attributes")
        object.__setattr__(self, key, value)

config1 = ImmutableConfig("Dark Mode")
config2 = ImmutableConfig("Light Mode")

print(config1.setting)
print(config2.setting)
print(config1 is config2)
try:
    config1.setting = "Blue Mode"
except AttributeError as e:
    print("Error:", e)

# __new__
class SingleCharName:
    def __new__(cls, name):
        if len(name) != 1:
            raise ValueError("Only one character allowed")
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name

char1 = SingleCharName("X")
print(char1.name)

try:
    char2 = SingleCharName("Hem")
except ValueError as e:
    print("Error:", e)

"""# ITERATORS"""

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Iterator for default data structures
emp_name = ["A","B","C","D"]
it = iter(emp_name)
try:
  while True:
   print(next(it))
except StopIteration:
  pass

#class based iterator
class SalaryIterator:
    def __init__(self, salaries):
        self.salaries = salaries
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.salaries):
            raise StopIteration
        salary = self.salaries[self.index] * 1.50
        self.index += 1
        return f"Updated Salary: {salary:.2f}"

salaries = [50000, 60000, 55000]
salary_iter = SalaryIterator(salaries)

for salary in salary_iter:
    print(salary)

"""# Generators"""

#employee increment
def emp_incr():
    salary = [100000, 200000, 150000]
    for s in salary:
        yield f"Increment received: {s * 0.20:.2f}"

incr = emp_incr()

for i in incr:
    print(i)

#Role-Based Salary generator

def salary_role(emp_roles):
    base_salaries = {"HR": 50000, "IT": 60000, "Finance": 70000, "Marketing": 55000}

    for role in emp_roles:
        if role in base_salaries:
            yield f"Role: {role}, New Salary: {base_salaries[role] * 1.20:.2f}"
        else:
            yield f"Role: {role}, No data available"

roles = ["IT", "HR", "Finance", "CEO"]
salary_gen = salary_role(roles)

for salary in salary_gen:
    print(salary)

#infinite Iterator and generator:
import random

def rand_empids():
    while True:
        yield random.randint(100, 999)

idgen = iter(rand_empids())

for _ in range(5):
    print(next(idgen))

# combinig all concpets to create a library management system
#book class
class Book:
    lib_name = "SG Library"

    def __init__(self, b_id, title, author, copies):
        self.b_id = b_id
        self.title = title
        self.author = author
        self.copies = copies

    def show(self):
        print(f"ID: {self.b_id}, {self.title} by {self.author}, Copies: {self.copies}")

    @staticmethod
    def fine(days):
        return days * 50

    @classmethod
    def set_lib_name(cls, name):
        cls.lib_name = name

#book iterator
class BookIter:
    def __init__(self, books):
        self.books = books
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.books):
            raise StopIteration
        b = self.books[self.i]
        self.i += 1
        return b

#book generator for availability
def book_avail(books):
    for b in books:
        yield f"{b.title} - Available: {b.copies}" if b.copies > 0 else f"{b.title} - Out of Stock"

#library management system
class Library:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print("\nBooks:")
        for b in BookIter(self.books):
            b.show()

    def check_avail(self):
        print("\nAvailability:")
        for b in book_avail(self.books):
            print(b)

    def show_lib_name(self):
        print(f"\nLibrary: {Book.lib_name}")

books = [
    Book(1, "1984", "George Orwell", 4),
    Book(2, "Metamorphosis", "Kafka", 2),
    Book(3, "Hippie", "Paul Ceolho", 0)
]

lib = Library(books)

lib.list_books()
lib.check_avail()
lib.show_lib_name()
Book.set_lib_name("Seg Library")
lib.show_lib_name()
print(f"{Book.fine(3)} rupees")