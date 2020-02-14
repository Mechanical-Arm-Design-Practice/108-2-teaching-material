class A():
    count = 0
    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", A.count, "little objects.")
        print("A has", cls.count, "little objects.")

    @staticmethod
    def Tell_Me_Something():
        print("Hey! What happened?")

def main():
    A.Tell_Me_Something()

    easy_A = A()
    brezzy_A  = A()
    wheezy_A = A()

    A.kids()
if __name__ == "__main__":
    main()