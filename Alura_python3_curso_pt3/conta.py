class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('contruindo objeto ....{}'.format(self))
        self.numero=123
        self.titular = "lolo"
        self.saldo =55
        self.limite = 1000

    def extrato(self):
        print(f'O saldo da conta é {self.saldo}, titular {self.titular}')

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor