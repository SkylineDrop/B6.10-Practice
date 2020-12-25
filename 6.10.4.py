class Client:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.cash_operations = []

    def __str__(self):
        return (f"Клиент: {self.name}. Баланс: {self.balance} руб.")

    
    def put(self, money):
        self.balance = self.balance + money

    def take(self, money):
        self.balance = self.balance - money

client_1 = Client("Иван Петров")
client_1.put(100)
client_1.take(50)
#print(client_1)  # "Ivan petrov, balance 50"

client_2 = Client("Равшан Аскеров", 3000)
client_2.take(1000)
client_2.take(2000)
#print(client_2)

class Guest(Client):
    def __init__(self, name, city, rank):
        self.name = name
        self.city = city
        self.rank = rank

    def __str__(self):
        return (f"{self.name}, г.{self.city}, статус '{self.rank}'")

#При выводе в консоль вы должны получить:  «Иван Петров, г. Москва, статус "Наставник"»

guest_1 = Guest(name = "Иван Петров", city = "Москва", rank = "Наставник")
guest_2 = Guest(name = "Максим Патрушев", city = "Смоленск", rank = "Волонтер")
guest_3 = Guest(name = "Сергей Валерьевич", city = "Москва", rank = "Волонтер")

list_ = [guest_1, guest_2, guest_3]
for guest in list_:
    print(guest)
