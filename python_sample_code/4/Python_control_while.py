count = 1
numbers = [1, 3, 5]
position = 0

while count <= 5:
    print(count)
    count += 1

while 1:
    stuff = input("String to capitalize [type q to quit] : ")
    if stuff == 'q' or stuff == 'Q':
        break
    print(stuff.capitalize())

while True:
    value = input("Integer, please [q to quit]")
    if value == 'q' or value == 'Q':
        break
    number = int(value)
    if number %2 == 0:
        continue
    print(number, 'squared is ', number*number)

while position < len(numbers):
    number = numbers[position]
    if number %2 == 0:
        print('Found even number: ', number)
        break
    position += 1
else:
    print('No even number found')