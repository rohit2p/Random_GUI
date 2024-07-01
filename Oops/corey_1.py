# Define a class called Employee
class Employee:
    def __init__(self, first, second):  # This function is called when creating a new Employee object (like a constructor in other languages)
        self.first = first  # Assign the instance variable
        self.second = second
        self.email = first + second + "@" + "gmail.com"

    def fullname(self):
        return '{} {}' .format(self.first, self.second)

# Create an Employee object named `emp1` with arguments "Rohit" and "Prasad" for first and second name respectively
emp1 = Employee("Rohit", "Prasad")

# Call the `fullname` method of the `emp1` object to get the full name
print(emp1.fullname())