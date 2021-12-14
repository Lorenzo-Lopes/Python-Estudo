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

    def __pode_sacar(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar():
            self.__saldo -= valor
        else:
            print('O seu limite nao permite fazer o saque desse valor')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite