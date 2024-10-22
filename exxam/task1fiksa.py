from typing import Any


class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def get_info(self) -> None:
        print("Full Name:", self._first_name, self._last_name)
        print("Age:", self._age)


#Inheritance
class Student(Person):
    def __init__(self, first_name: str, last_name: str, age: int, student_id: str) -> None:
        super().__init__(first_name, last_name, age)
        self._student_id = student_id

    def get_info(self) -> None:
        super().get_info()
        print("Student ID:", self._student_id)


#Inheritance
class Employee(Person):
    def __init__(self, first_name: str, last_name: str, age: int, emp_number: int, salary: float) -> None:
        super().__init__(first_name, last_name, age)
        self._emp_number = emp_number
        self._salary = salary

    def get_info(self) -> None:
        super().get_info()
        print("Employee Number:", self._emp_number)
        print("Salary:", self._salary)


def main() -> None:
    new_student = Student("Anthony", "Smith", 35, "s346571")
    new_student.get_info()
    print("==========================")
    new_employee = Employee("Sarah", "Taylor", 34, 2919736, 5000)
    new_employee.get_info()


if __name__ == "__main__":
    main()
