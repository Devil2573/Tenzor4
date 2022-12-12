from random import randint
mas=[]
count=5
for i in range(count):
    mas.append(randint(1,50))
print(mas)
for i in range (count-1):
    for j in range(count-i-1):
        if mas[j]>mas[j+1]:
            mas[j], mas[j+1] = mas[j+1], mas[j]
print(mas)