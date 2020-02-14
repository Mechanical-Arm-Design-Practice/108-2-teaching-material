class Duck_property_2():
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print("Inside the getter.")
        return self.__name

    @name.setter
    def name(self, input_name):
        print("Inside the setter.")
        self.__name = input_name

    def __pravite_method(self):
        print("I'm a pravite method~")

    def using_pravite_method(self):
        self.__pravite_method()

def main():
    duck = Duck_property_2("Jack")
    print(duck.__name)
    duck.name = 'Tom'
    duck.using_pravite_method()

if __name__ == "__main__":
    main()