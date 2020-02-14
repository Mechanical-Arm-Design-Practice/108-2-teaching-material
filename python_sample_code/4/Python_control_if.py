# You can say what you want here~
# Let's try '\'
alphabet = 'abcd' + 'efgh' + 'ijkl' + 'mnop' + 'qrst' + 'uvwx' + 'yz'

alphabet_2 = 'abcd' + 'efgh'\
                + 'ijkl' + 'mnop'\
                + 'qrst' + 'uvwx' + 'yz'

alphabet_3 = ''
alphabet_4 = None
flag_A = True
number = 10
list_a = [1, 2, 4, 8, 10]
'''
print("alphabet: ", alphabet)
print("alphabet_2: ", alphabet_2)
print("alphabet = alphabet_2 ? ", alphabet == alphabet_2)
'''
'''
if flag_A:
    print("In 'if'")
else:
    print("In 'else'")


#Don't do this...!
if flag_A == True:
    print("Yap, it can work...but not good.")
else :
    print("In else, still not good.")

'''
'''
#More about if/elif/else
if number == 1:
    print("number = 1")
elif number == 10:
    print("number = 10")
else:
    print("number = ?")
'''

if 3 < number <12:
    if number != 7:
        if number <= 11:
            if number > 9 and number not in list_a:
                print("Hi there!")
