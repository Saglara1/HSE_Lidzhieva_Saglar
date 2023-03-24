# # #
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

# Задание 2 - вариант 1

sec = input('Введите число секунд: ')

if sec.isdigit():
    mins = int(sec)//60
    hours = mins//60
    print('Часы:', hours)
    print('Минуты:', mins)
    print('Секунды:', int(sec))
else:
    print('Надо было вводить число!')
# # #

# Задание 2 - вариант 2

sec1 = input('Введите число секунд: ')

if sec1.isdigit():
    hours = int(sec1)//3600
    sec2 = int(sec1) - 3600*int(hours)
    mins = int(sec2)//60
    sec3 = int(sec1) - int(hours*3600) - int(mins*60)
    print('Часы:', hours)
    print('Минуты:', mins)
    print('Секунды:', sec3)
else:
    print('Надо было вводить число!')
# # #
# Задание 3
n = int(input("Введите число от 1 до 9: "))
nn = n*10+n
nnn = n*100 + nn
sum = n+nn+nnn
print(sum)