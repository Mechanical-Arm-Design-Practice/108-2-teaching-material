class Person():
    def __init__(self, name):
        self.name = name

    def exclame(self):
        print("My name is", self.name)

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def exclame(self):
        print("My name is {}. I'm student. I'm {} years old.".format(self.name, self.age))

def main():
    person_1 = Person("Jack")
    person_2 = Student("Tom", 17)
    person_1.exclame()
    person_2.exclame()

if __name__ == "__main__":
    main()