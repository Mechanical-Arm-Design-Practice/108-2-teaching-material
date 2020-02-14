class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print("Inside the getter.")
        return self.hidden_name

    def set_name(self, input_name):
        print("Inside the setter.")
        self.hidden_name = input_name

class Duck_property():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print("Inside the getter.")
        return self.hidden_name

    def set_name(self, input_name):
        print("Inside the setter.")
        self.hidden_name = input_name

    name = property(get_name, set_name)

class Duck_property_2():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print("Inside the getter.")
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print("Inside the setter.")
        self.hidden_name = input_name

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

def main():

    #duck_1 = Duck('A')
    #print(duck_1.get_name())

    #duck_2 = Duck_property('B')
    #print(duck_2.name)
    #duck_2.name = "C"
    #print(duck_2.name)


    #duck_3 = Duck_property_2('D')
    #print(duck_3.name)
    #duck_3.name = "E"
    #print(duck_3.name)


    circle = Circle(5)
    print(circle.diameter)
    circle.radius = 1
    print(circle.diameter)


if __name__ == "__main__":
    main()