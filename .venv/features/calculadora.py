class Calculadora(object):
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.value = 0

    def armazenarNumeros(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def somar(self):
        self.value = self.num1 + self.num2

    def obterValor(self):
        return self.value