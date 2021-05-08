import random

def square_range(num):
    for n in range(num):
        yield n**2

def rand_num(low,high,num):
    for n in range(num):
        yield random.randint(low,high)

def convert_string_iterator(word):
    return iter(word)

for i in rand_num(3,234,10):
    print(i)

s = convert_string_iterator('sachin negi')

print(next(s))
print(next(s))
next(s)

