# Write a class Employee with private attribute __salary. Provide getter and setter
# methods to access and update the salary. Demonstrate encapsulation by trying to
# access __salary directly and via getter/setter.


class Employee:
    def __init__(self, salary: float):
        # Private attribute (name-mangled by Python)
        self.__salary = salary

    def get_salary(self) -> float:
        """Return the employee's salary."""
        return self.__salary

    def set_salary(self, amount: float) -> None:
        """Update the salary if the amount is positive, else raise ValueError."""
        if amount > 0:
            self.__salary = amount
        else:
            raise ValueError("Invalid salary amount! Salary must be positive.")


if __name__ == "__main__":
    # Create an Employee and demonstrate encapsulation
    emp = Employee(50000)
    print("Accessing salary via getter:", emp.get_salary())

    # Trying to access the private attribute directly will raise AttributeError
    try:
        print("Direct access to __salary:", emp.__salary)
    except AttributeError as e:
        print("Error accessing __salary directly:", e)

    try:
        print("Accessing via name-mangled attribute:", emp._Employee__salary)
    except Exception as e:
        print("Could not access name-mangled attribute:", e)

    # Update salary via setter
    emp.set_salary(60000)
    print("Updated salary via getter:", emp.get_salary())

    # Demonstrate setter rejects invalid values
    try:
        emp.set_salary(-1000)
    except ValueError as e:
        print("Setter rejected invalid value:", e)
