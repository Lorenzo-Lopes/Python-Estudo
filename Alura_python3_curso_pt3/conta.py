class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('contruindo objeto ....{}'.format(self))
        self.__numero=numero
        self.__titular =titular
        self.__saldo =saldo
        self.__limite = limite
    def extrato(self):
        print(f'O saldo da conta é {self.__saldo}, titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

