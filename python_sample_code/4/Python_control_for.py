rabbits = ['A', 'B', 'C', 'D']
current = 0
'''
#It works, but...
while current < len(rabbits):
    print(rabbits[current])
    current += 1
'''
'''
#This is better
for rabbit in rabbits:
    print(rabbit)

word = 'cat'
for letter in word:
    print(letter)
'''
'''
dict_A = {'John': 17, 'Sam': '20', 'Tom':'30'}
for name in dict_A:
    print(name)
for age in dict_A.values():
    print(age)
for pair in dict_A.items():
    print(pair)
for name, age in dict_A.items():
    print(name, 'is', age, 'years old')
'''
'''
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely,', cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')
'''
'''
cheeses = []
found_one = False
for cheese in cheeses:
    found_one = True
    print('This shop has some lovely,', cheese)
    break
if not found_one:
    print('This is not much of a cheese shop, is it?')
'''
'''
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
deserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

print(type(list(zip(days, fruits, drinks, deserts))))

for day, fruit, drink, desert in zip(days, fruits, drinks, deserts):
    print("{} drink {}, eat {}, enioy {}.".format(day, fruit, drink, desert))
'''

#for i in range(10):
  #  print(i)

#for i in range(1, 5, 2):
    #print(i)

for i in range(2, 0, -1):
    print(i)
