with open('user_input.txt', 'a') as file:
    s = input('Введите текст: ')
    file.write(s)
file.close()

