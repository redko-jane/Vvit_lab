class book:
    def __init__(self,title,author,date):
        self.title = title
        self.author = author
        self.date = date
    def get_info(self):
        return "Название книги : {} Автор книги : {} Дата выпуска книги : {}".format(self.title,self.author,self.date)
b=book("Сто лет тому вперёд","Кир Булычёв",1978)
print(b.get_info())
