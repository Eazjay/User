
class User:
    def __init__(self, first_name, last_name, age, account_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.balance = account_balance
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdrawal(self, amount):
        self.balance -= amount
    def transfer_money(self, receiver, amount):
        self.balance -= amount
        receiver.balance += amount
        return self
    def display_user_balance(self):
        print(f"\n{self.first_name}'s account balance is: ${self.balance}")
        return self

Joel = User("Joel", "Okoh" ,35 ,500)
Joel.make_deposit(50)
Joel.make_deposit(50)
Joel.make_deposit(100)
Joel.make_withdrawal(20)
Joel.display_user_balance()


Babe = User("Katie", "Rose", 22, 50)
Babe.make_deposit(50)
Babe.make_deposit(100)
Babe.make_withdrawal(10)
Babe.make_withdrawal(20)
Babe.display_user_balance()

Friend = User("Ossai", "J", 38, 450)
Friend.make_deposit(100)
Friend.make_withdrawal(100)
Friend.make_withdrawal(100)
Friend.make_withdrawal(100)
Friend.display_user_balance()

Joel.transfer_money(Friend, 20)

Joel.display_user_balance()
Friend.display_user_balance()

