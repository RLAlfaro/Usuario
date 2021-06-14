
display_user_balance (self) : haz que este método imprima el nombre del usuario y el saldo de la c
uenta en el terminalp.ej. "Usuario: Guido van Rossum, Saldo: $ 150
BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario en la cantidad y agrega esa cantidad al saldo de otro other_user

# make_withdrawal (self, amount) : haz que este método disminuya el saldo del usuario en la cantidad especificada

class User():

    def accountbalance(self):

    def make_deposit(self, cash):
        self.accountbalance += cash
        print(f"su deposito por {cash} pesos, ha sido cargado exitosamente. Su nuevo saldo es {self.accountbalance}")

    def make_withdraw(self, cash):
        self.accountbalance -= cash
        if cash > self.accoutbalance:
            print(f"Este giro ha sido cargado a su línea de sobregiro.")
        else:
            print(f"{self.nombre}, su giro por {cash} pesos, ha resultado exitoso. Su nuevo saldo es {self.accountbalance}")

    def display_user_balance(self):
        print(f"{self.nombre} tiene en su cuenta {self.accountbalance} pesos.")

    def transfer_money(self, otheruser, trans):
        self.accountbalance -= trans
        otheruser.accountbalance += trans
        if trans > self.accountbalance:
            print(f"Esta transferencia ha hecho uso de su línea de sobregiro.")
            print(f"Estimado cliente, ha transferido {trans} pesos, a {otheruser}")
        else:
            print(f"Estimado cliente, ha transferido {trans} pesos, a {otheruser}")







