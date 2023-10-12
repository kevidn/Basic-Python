# Error :
# Exceptions :

# SyntaxError
a = 99 print(a)
a = 99 
print(a))

# TypeError
a=5 + '10'

# ModuleNotFoundError
import randommodule

# NameError
a = 5
b = c

# FileNotFoundError
f = open(randomtext.txt)

# ValueError
a = [1,2,3]
a.remove(2)
print(a)

# IndexError
a = [1,2,3]
a[4]
print(a)

# KeyError
my_dict = {'name' : 'Kevin'}
my_dict['age']

# AssertionError
x = -5
insert (x>=), 'x is not postive'

# ZeroDivisionError: Karena pembagian dengan 0 tidak bisa.
a = 2 / 0

# Exception: x seharusnya positif.
x = -5
if x < 0:
    raise Exception('x should be positive')

