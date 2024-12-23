def describe_person(name, age=30):
    print('Его/её зовут',name,'. Ему/ей',age)
name=input('Введите имя человека: ')
age=input('Введите возраст человека: ')
describe_person(name,age)
describe_person(name)
