class Client:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.cash_operations = []

    def __str__(self):
        print(f"Клиент: {self.name}. Баланс: {self.balance} руб.")        
    
    def put(self, money):
        self.balance = self.balance + money

    def take(self, money):
        self.balance = self.balance - money

client_1 = Client("Иван Петров")
client_1.put(100)
client_1.take(50)
client_1.__str__()  # "Ivan petrov, balance 50"

client_2 = Client("Равшан Аскеров", 3000)
client_2.take(1000)
client_2.take(2000)
client_2.__str__()
