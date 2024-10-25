name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))
print(f"Привіт {name}, тобі {age}!")

age = int(input("Введіть ваш вік: "))
if age >= 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

import random

secret_number = random.randint(1, 10)
guess = None

while guess != secret_number:
    guess = int(input("Вгадай число від 1 до 10: "))
    if guess > secret_number:
        print("Менше")
    elif guess < secret_number:
        print("Більше")
    else:
        print("Ви вгадали")

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

if num1 <= num2:
    for i in range(num1, num2 + 1):
        print(i)
else:
    print("Друге число має бути більше або рівне першому.")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

n = int(input("Введіть число факторіалу: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Факторіал {n} = {factorial}")