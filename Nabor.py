from random import randint
a=set()
b=set()
n=10
for i in range(n):
    a.add(randint(1,10))
    b.add(randint(1,10))
print(a)
print(b)
print(a&b)
print(a-b)
print(b-a)
print(a^b)