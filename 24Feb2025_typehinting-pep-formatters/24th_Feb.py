
from typing import Optional, Union, Tuple, List, Dict, Any, Callable


def add(x: int, y: int) -> int:
    """Adds two integers and returns the result."""
    return x + y


def get_length(s: str) -> int:
    """Returns the length of a string."""
    return len(s)


def find_user(user_id_: int) -> Optional[str]:
    """Returns the user name if found, otherwise None."""""""""
    users = {1: "Hem", 2: "Anth", 3: "Lak"}
    return users.get(user_id_)


def square(n: Union[int, float]) -> float:
    """Returns the square of a number."""
    return n * n


def get_coordinates() -> Tuple[float, float]:
    """Returns latitude and longitude as a tuple."""
    return 17.434284, 78.376361


def get_even_numbers(numbers: List[int]) -> List[int]:
    """Returns a list of even numbers from the input list."""
    return [n for n in numbers if n % 2 == 0]


def user_id() -> Dict[str, float]:
    """Returns a dictionary of user names and their corresponding IDs."""
    return {"Hem": 1, "Anth": 2, "Lak": 3}


def execute_function(func: Callable[[int, int], int], x: int, y: int) -> int:
    """Executes a function that takes two integers as arguments."""
    return func(x, y)


def add_numbers(a: int, b: int) -> int:
    """Adds two integers and returns the result."""
    return a + b


def subtract_numbers(a: int, b: int) -> int:
    """Subtracts two integers and returns the result."""
    return a - b


def get_value(data: Dict[str, Any], key: str) -> Any:
    """Returns the value associated with the given key in a dictionary."""
    return data.get(key)


class Student:
    """Represents a student with a name and a list of grades."""

    def __init__(self, name: str, grades: List[int]) -> None:
        self.name = name
        self.grades = grades

    def get_average(self) -> float:
        """Returns the average of the student's grades."""
        return sum(self.grades) / len(self.grades)


def main() -> None:
    """Main function to demonstrate type hints usage."""

    # Test add function
    print(f"The sum of 10 and 20 is {add(10, 20)}")

    # Test get_length function
    print(f"Length of 'Hemanth Lakshman Yarlagadda': {get_length('Hemanth Lakshman Yarlagadda')}")

    # Test find_user function
    print(f"UserID 1: {find_user(1)}")
    print(f"UserID 3: {find_user(3)}")
    print(f"UserID 5: {find_user(5)}")

    # Test square function
    print(f"Square of 7: {square(7)}")
    print(f"Square of 2.546: {square(2.546)}")

    # Test get_coordinates function
    coordinates = get_coordinates()
    print(f"Coordinates: Latitude={coordinates[0]}, Longitude={coordinates[1]}")

    # Test get_even_numbers function
    print(f"Even numbers: {get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])}")

    # Test user_id function
    print(f"User IDs: {user_id()}")

    # Test execute_function function
    print(f"Executing add_numbers function: {execute_function(add_numbers, 5, 10)}")
    print(f"Executing subtract_numbers function: {execute_function(subtract_numbers, 5, 10)}")

    # Test get_value function
    user_data = {"name": "Hem", "age": 21, "scores": [90, 85, 88]}
    print(f"Name: {get_value(user_data, 'name')}")
    print(f"Age: {get_value(user_data, 'age')}")
    print(f"Scores: {get_value(user_data, 'scores')}")

    # Test Student class
    student = Student("Hem", [90, 86, 90, 95])
    print(f"Student: {student.name}")
    print(f"Average: {student.get_average():.3f}")


if __name__ == "__main__":
    main()
