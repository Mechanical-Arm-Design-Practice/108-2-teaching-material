class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, another_word):
        return self.text.lower() == another_word.text.lower()

class Word_2():
    def __init__(self, text):
        self.text = text

    def __eq__(self, another_word):
        return self.text.lower() == another_word.text.lower()
class Word_3():
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text
    def __repr__(self):
        return ' Word(" ' + self.text + ' ") '

def main():
    first = Word("ha")
    second = Word("HA")
    third = Word("eh")
    print(first.equals(second))
    print(first.equals(third))

    print("==========Special method below===========")
    first = Word_2("ha")
    second = Word_2("HA")
    third = Word_2("eh")
    print(first == second)
    print(first == third)

    word = Word_3('Hi!')
    print(word)

if __name__ == "__main__":
    main()