class UserAccount:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self,old_password):
        if self.check_password(old_password):
            self.__password=input('Введите новый пароль: ')
        else:
            print("Неправильный пароль, попробуйте ещё раз")
            self.set_password(input("Для смены пароля введите старый: "))
    def check_password(self,password):
        if self.__password==password:
            return True
        else:
            return False
    def get_info(self):
        return "Логин : {} Адрес почты : {} Пароль : {}".format(self.username,self.email,self.__password)
ua=UserAccount('hedgehog','hedgehog@gmail.com','yezh')
print(ua.get_info())
ua.set_password(input("Для смены пароля введите старый: "))
print(ua.get_info())
