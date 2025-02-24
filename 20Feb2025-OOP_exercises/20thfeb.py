"""
Collection of exercises demonstrating Python programming concepts.

Contains implementations of list operations, numpy array manipulations,
and OOP concepts including inheritance, polymorphism, and decorators.
"""

import math
from abc import ABC, abstractmethod


def find_unique_elements():
    """Count number of unique elements in a list."""
    numbers = map(int, input().split())
    unique_numbers = set(numbers)
    print(len(unique_numbers))


def product_excluding_duplicates():
    """Calculate product of elements excluding duplicates."""
    numbers = map(int, input().split())
    unique_numbers = set(numbers)
    result = 1
    for num in unique_numbers:
        result *= num
    print(result)


def find_elements_above_frequency(numbers, k):
    """Extract elements with frequency greater than k."""
    unique = []
    frequency = {}
    result = []

    for num in numbers:
        if num not in unique:
            unique.append(num)
            frequency[num] = 1
        else:
            frequency[num] += 1
        if frequency[num] == k + 1:
            result.append(num)
    return result


def check_range(numbers, lower, upper):
    """Check if all elements are within the given range."""
    return all(lower <= num <= upper for num in numbers)


def find_consecutive_numbers(numbers):
    """Check if list has three consecutive common numbers."""
    numbers = list(numbers)
    for i in range(len(numbers) - 2):
        if numbers[i] == numbers[i + 1] == numbers[i + 2]:
            return "Found"
    return "Not Found"


def find_strongest_neighbors(numbers):
    """Find strongest neighbor for each pair of elements."""
    return [max(numbers[i], numbers[i + 1]) for i in range(len(numbers) - 1)]


def remove_element(numbers, target):
    """Remove all instances of an element from list."""
    return [num for num in numbers if num != target]


def get_last_n_elements(numbers, n):
    """Get the last n elements from a list."""
    return numbers[-n:]


class Student:
    """Class representing a student with name and grade."""

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        """Display student information."""
        print(f"{self.name} {self.grade}")


class Book:
    """Class representing a book in library."""

    def __init__(self, name, author, copies):
        self.name = name
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"{self.name} by {self.author} - {self.copies}"


class Library:
    """Class representing a library and its operations."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def display_books(self):
        """Display all books in the library."""
        for book in self.books:
            print(book)

    def borrow_book(self, name):
        """Process book borrowing request."""
        for book in self.books:
            if book.name == name and book.copies > 0:
                book.copies -= 1
                print(f"You borrowed '{name}'.")
                return
        print(f"'{name}' is not available.")


class BankAccount:
    """Base class for bank accounts."""

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        """Process deposit transaction."""
        if amount <= 2_000_000:
            self._balance += amount
            print(f"Deposited: {amount} rupees")
        else:
            print("Amount exceeds deposit limit of 20,00,000 rupees")

    def withdraw(self, amount):
        """Process withdrawal transaction."""
        if amount > 2_000_000:
            print("Amount exceeds withdrawal limit of 20,00,000 rupees")
        elif self._balance - amount >= 5000:
            self._balance -= amount
            print(f"Withdrawn: {amount} rupees")
        else:
            print("Minimum balance of 5000 rupees must be maintained")

    def get_balance(self):
        """Return current balance."""
        return self._balance


class Employee:
    """Base class for employees."""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        """Display employee details."""
        print(f"Employee: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    """Class representing a manager, derived from Employee."""

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_details(self):
        """Display manager details including department."""
        super().display_details()
        print(f"Department: {self.department}")


class Animal:
    """Base class for animals."""

    def speak(self):
        """Return generic animal sound."""
        return "Sound!"


class Dog(Animal):
    """Class representing a dog."""

    def speak(self):
        """Return dog's sound."""
        return "Bark!"


class Cat(Animal):
    """Class representing a cat."""

    def speak(self):
        """Return cat's sound."""
        return "Meow!"


class Calculator:
    """Class implementing basic calculator operations."""

    def add(self, *args):
        """Add variable number of arguments."""
        return sum(args)

    def multiply(self, *args):
        """Multiply variable number of arguments."""
        return math.prod(args)


class CreditAccount:
    """Class representing a credit account."""

    def __init__(self, credit_limit):
        self._credit_limit = credit_limit
        self._credit_used = 0

    def use_credit(self, amount):
        """Process credit usage."""
        if amount <= self._credit_limit - self._credit_used:
            self._credit_used += amount
            print(f"Credit used: {amount} rupees")
        else:
            print("Credit limit exceeded!")

    def pay_credit(self, amount):
        """Process credit payment."""
        if amount <= self._credit_used:
            self._credit_used -= amount
            print(f"Credit payment of {amount} rupees successful")
        else:
            print("Invalid credit payment amount")

    def get_credit_details(self):
        """Return credit account details."""
        return f"Credit Limit: {self._credit_limit} rupees, Used: {self._credit_used} rupees"


class Order(ABC):
    """Abstract base class for orders."""

    def __init__(self, items):
        self.items = items

    @abstractmethod
    def calculate_total(self):
        """Calculate total order amount."""
        pass


class DineIn(Order):
    """Class representing dine-in orders."""

    def calculate_total(self):
        """Calculate total with dine-in markup."""
        return sum(self.items.values()) * 1.2


class Takeout(Order):
    """Class representing takeout orders."""

    def calculate_total(self):
        """Calculate total for takeout."""
        return sum(self.items.values())


class Online(Order):
    """Class representing online orders."""

    def calculate_total(self):
        """Calculate total with online markup."""
        return sum(self.items.values()) * 1.5


class Product:
    """Class representing a product with price and discount."""

    def __init__(self, name, price):
        self.name = name
        self._price = price
        self._discount = 0

    @property
    def price(self):
        """Calculate final price after discount."""
        return self._price - (self._price * self._discount / 100)

    @price.setter
    def price(self, new_price):
        """Set new base price."""
        if new_price > 0:
            self._price = new_price
        else:
            print("Price must be positive!")

    @property
    def discount(self):
        """Get current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, percentage):
        """Set discount percentage."""
        if 0 <= percentage <= 50:
            self._discount = percentage
        else:
            print("Invalid discount percentage!")


def main():
    """Main function to demonstrate class usage."""
    # Library demonstration
    library = Library()
    library.add_book(Book("1984", "George Orwell", 5))
    library.add_book(Book("Metamorphosis", "Kafka", 1))
    library.display_books()
    library.borrow_book("1984")

    # Bank account demonstration
    account = BankAccount("John", 5000)
    account.deposit(100_000)
    account.withdraw(50_000)
    print(f"Balance: {account.get_balance()} rupees")

    # Order processing demonstration
    orders = [
        DineIn({"Burger": 250, "Fries": 95}),
        Takeout({"Pasta": 490, "Wine": 300}),
        Online({"Salad": 315, "Bread": 60})
    ]
    for order in orders:
        print(f"{order.__class__.__name__}: {order.calculate_total():.2f}")


if __name__ == "__main__":
    main()