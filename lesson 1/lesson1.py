# Задание 1
c = 10
d = "привет"

e = 20
f = e
j = f

a = input("введите число 1: ")
b = input("введите число 2: ")
print(a,b,c,d)

print(id(e))
print(id(f))
print(id(j))

# Задание 2
sec = input('Введите число секунд: ')

if sec.isdigit():
    mins = int(sec)/60
    hours = mins/60
    print('Часы:', hours)
    print('Минуты:', mins)
    print('Секунды:', int(sec))
else:
    print('Надо было вводить число!')
