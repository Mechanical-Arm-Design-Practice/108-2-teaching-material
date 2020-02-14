class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words

class QuestionQuote(Quote):
    def says(self):
        return self.words + " ?"

class ExclamationQuote(Quote):
    def says(self):
        return self.words + " !"

class Another_One():
    def who(self):
        return "Another One"
    def says(self):
        return "What?"

def main():
    A = Quote('Jack', "I'm Jack.")
    B = QuestionQuote("Tom", "I'm Tom.")
    C = ExclamationQuote("Sam", "I'm Sam")
    D = Another_One()

    print(A.who(), 'says: ', A.says())
    print(B.who(), 'says: ', B.says())
    print(C.who(), 'says: ', C.says())

    def who_says(obj):
        print(obj.who(), 'says: ', obj.says())

    print("============Duck Typing below==============")

    who_says(A)
    who_says(B)
    who_says(C)
    who_says(D)

if __name__ == "__main__":
    main()