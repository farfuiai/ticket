class Ticket:
    def __init__(self, title, price, quantity, language="Geo"):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.language = language

    def __str__(self):
            return f"movie: {self.title}, price: {self.price}, quantity: {self.quantity}, language: {self.language}"


    def __gt__(self, other):
        if isinstance(other, Ticket):
            return self.quantity > other.quantity
        elif isinstance(other, int):
            return self.quantity > other
        return False


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
            return f"user: {self.name}, balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print(f"added on balance: {amount}")

    def buy_ticket(self, ticket, amount):
        total_price = (ticket.price * amount)

        if total_price <= self.balance and ticket.quantity >= amount:
            self.balance -= total_price
            ticket.quantity -= amount
            print(f"you bought {amount} ticket")
        else:
            print(f"you can't buy {amount} ticket (not enough money)")

titanic = Ticket("titanic", 15, 20)
avengers = Ticket("avengers", 15, 30)

me = User("giorgi", 250 - avengers.quantity - titanic.quantity)

me.buy_ticket(titanic, 2)
me.buy_ticket(avengers, 5)

print(titanic)
print(avengers)
print(me)

print(titanic > avengers)
print(titanic > 10)