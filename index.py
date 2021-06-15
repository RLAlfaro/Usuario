
# display_user_balance (self) : haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminalp.ej. 
# "Usuario: Guido van Rossum, Saldo: $ 150

# BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario
# en la cantidad y agrega esa cantidad al saldo de otro other_user

# make_withdrawal (self, amount) : haz que este método disminuya el saldo del usuario en la cantidad 
# especificada

class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.accountbalance = 0


class BankAccount:
    def __init__(self, int_rate, money):
        self.int_rate = int_rate
        self.account_balance = money
# Metodos
    def deposit(self, money):
        self.account_balance += money
        print(f"Se han cargado {money} pesos a su cuenta bancaria. Su saldo es {self.account_balance}")
        return self

    def withdraw(self, money):
        self.account_balance -= money
        if self.account_balance < 0:
            print(f"Este giro ha sido cargado a su línea de credito.")
        else:
            print(f"Su giro por {money} pesos ha resultado exitoso. Su nuevo saldo es {self.account_balance}")
        return self


    def display_account_info(self):
        print(f"Su saldo corresponde a {self.account_balance}")
        return self

    def yield_interest(self):
        self.account_balance += self.account_balance * self.int_rate
        return self


red = User("Red", "red@python.com")
blue = User("Blue", "blue@python.com")

red_account = BankAccount(0.05, 0)
blue_account = BankAccount(0.05, 0)

red_account.deposit(100).deposit(50).deposit(150).withdraw(200).yield_interest().display_account_info()
blue_account.deposit(500).deposit(1000).deposit(100).withdraw(500).yield_interest().display_account_info()



