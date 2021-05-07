class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User Name: {self.name}\nAccount Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


jim = User("Jim")
jim.make_deposit(133).make_deposit(133).make_deposit(134).make_withdrawal(13).display_user_balance()

jake = User("Jake")
jake.make_deposit(50).make_deposit(51).make_withdrawal(1).make_withdrawal(1).display_user_balance()

john = User("John")
john.make_deposit(72).make_withdrawal(3).make_withdrawal(6).make_withdrawal(9).display_user_balance()

jim.transfer_money(john, 18)
jim.display_user_balance()
jake.display_user_balance()



# For example if guido.make_deposit(100) returns its own 
# instance (guido), then we can call one of that instance's 
# methods after that call, 
# like guido.make_deposit(100).make_withdrawal(50).