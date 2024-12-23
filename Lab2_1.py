def greet(name):
    print('Здравствуй,',name)
a=input('Введите своё имя: ')
greet(a)


def square(number):
    print(number**2)
n=int(input('Введите число: '))
square(n)


def max_of_two(x, y):
    print(max(x,y))
a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
max_of_two(a,b)
