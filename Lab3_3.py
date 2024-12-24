try:
    def read(f,a):
        if a=='0':
            with open(f, 'r') as file:
                content = file.read()
            print(content)
        elif a=='1':
            with open(f, 'r') as file:
                for line in file:
                    print(line)
        else:
            a=input('Ошибка. Выберите 0 или 1: ')
            read(f,a)
    a=input('Для чтения всего файла введите 0, для построчного чтения - 1: ')
    read('example.txt',a)

except FileNotFoundError:
    print('Ваш файл не существует!')
except Exception: 
    print('возникли неизвестные проблемы')
else: 
    print('Операция выполнена успешно')
