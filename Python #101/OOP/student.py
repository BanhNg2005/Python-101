class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # def __str__ is a special method that is called when you use print() on an object
    def __str__(self):
        return f"{self.name} of house {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    # Getter
    @property # this is a decorator that makes the method below a getter
    def house(self):
        return self._house
    
    # Setter
    @house.setter # this is a decorator that makes the method below a setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house name")
        self._house = house
    
    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🦒"
    #         case "otter":
    #             return "👞"
    #         case "Jack Russell Terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"
    
def main():
    student = get_student()
    # student.house = "Number 4 Privet Drive" this is just an example of how the setter works 
    # and how it will raise an error if the house is not one of the four houses
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) 
    return student


if __name__ == "__main__":
    main()