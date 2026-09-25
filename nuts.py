#Задание 1
print('Задание 1')
c = 25
f = (c * 9/5) + 32
k = c + 273.15
print(c , 'C =', f, 'F')
print(c, 'C = ', k, 'K')

#Задание 2
print('Задание 2')
n = int(input())
if n%2==0:
    print('четное')
else:
    print('нечетное')
if n>0:
    print('положительное')
elif n<0:
    print('отрицательное')
else:
    print('ноль')
if n>=10 and n<=50:
    print('принадлежит диапозону')
else:
    print('не принадлежит диапозону')

#Задание 3
print('Задание 3')
import random
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symvols ="!@#$%^&*"
password = ''
for i in range(3):
    password += random.choice(letters)
for i in range(3):
    password += random.choice(numbers)
for i in range(2):
    password += random.choice(symvols)
print(password)

#Задание 4
print('Задание 4')
from collections import Counter

text = input().lower()
k = Counter(text)
print(k.most_common(3))

#Задание 5
print('Задание 5')
N = int(input())
numbers = [True] * (N + 1)
numbers[0] = False
numbers[1] = False
for i in range(2,N+1):
    if numbers[i]:
        for j in range(i*2,N+1,i):
            numbers[j] = False

for i in range(2, N + 1):
    if numbers[i]:
        print(i)
        
