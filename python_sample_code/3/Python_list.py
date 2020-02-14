#create data
list_a = []
list_b = list()
list_c = [1.0, 2.0, 3.0]

tuple_a = (1, 'a', 3.14)
'''
#string to list
list_a = list('cat')
print("list_a:", list_a)

#tuple to list
list_b = list(tuple_a)
print("list_b:", list_b)
'''
#================================
'''
#assign list_d to list_c
list_d = list_c

print("list_d:", list_d)
list_d[1] = 'b'

print("list_d[1] <-- 'b'")
print("list_d:", list_d)
print("list_c:", list_c)
'''
#================================
'''
#list_c is a copy of list_b
list_d = list_c.copy()

print("list_d:", list_d)
list_d[1] = 'b'
print("list_d[1] <-- 'b'")
print("list_d:", list_d)
print("list_c:", list_c)
'''
#================================

#using slice[start:end:step]
list_e = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list_e[::])
print(list_e[1:])
print(list_e[1:7])
print(list_e[:3])
print(list_e[1:7:1])
print(list_e[0:6:2])
print(list_e[::-1])
print(list_e[-3:2:-1])
print(list_e[-3::-1])
print(list_e[-3::1])
