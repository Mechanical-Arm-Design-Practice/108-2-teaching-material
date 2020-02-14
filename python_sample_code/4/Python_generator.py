# method 1
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print("method 1: ", number_list)

# method 2
number_list = []
for number in range(1, 6):
    number_list.append(number)
print("method 2: ", number_list)

# method 3
number_list = []
number_list = list(range(1, 6))
print("method 3: ", number_list)

# method 4
number_list = []
number_list = [number for number in range(1, 6)]
print("method 4: ", number_list)

# method 4-1
number_list = []
number_list = [number*2 for number in range(1, 6)]
print("method 4-1: ", number_list)

# method 4-2
number_list = []
number_list = [number*2 for number in range(1, 6) if (number*2) %3 == 1]
print("method 4-2: ", number_list)

# method 4-3 list generator
number_list = []
rows = range(1, 4)
cols = range(0, 2)
number_list = [(row, col) for row in rows for col in cols]
print("method 4-2: ", number_list)

# method 4-4 dictionary generator
word = 'letter'
letter_count = {letter:word.count(letter) for letter in set(word)}
print("method 4-4: ", letter_count)

# method 4-5 set generator
a_set = {number for number in range(1, 6) if number%3 == 1}
print("method 4-5: ", a_set)