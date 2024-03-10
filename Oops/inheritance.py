class Human:
    def __init__(self, name):
        self.name = name


class Student(Human):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def __str__(self):
        return f"{self.name} and {self.roll}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        roll = input("Roll: ")
        return cls(name, roll)
    
class Teacher(Human):
    def __init__(self, name, Id):
        super().__init__(name)
        self.Id = Id
    
    def __str__(self):
        return f"{self.name} and {self.Id}"

    @classmethod
    def get(cls):
        name = input("Enter teacher's name: ")
        Id = input("Enter teacher's ID: ")
        return cls(name, Id)




student = Student.get()
teacher = Teacher.get()
print(student)
print(teacher)
