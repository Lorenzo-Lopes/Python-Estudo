class Data:
    def __init__(self):
        self.__dia = 0
        self.__mes = 0
        self.__ano = 0

    def le_data(self):
        self.dia = int(input('Digite o dia: '))
        self.mes = int(input('Digite o mes: '))
        self.ano = int(input('Digite o ano: '))

    def formatada(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')
