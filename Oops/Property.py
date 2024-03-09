class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"I am {self.name} from {self.house}"
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["kolkata", "Bihar", "JJ"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()
