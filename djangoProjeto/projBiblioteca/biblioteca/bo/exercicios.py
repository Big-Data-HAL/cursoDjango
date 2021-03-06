

class Calculadora:
    def __init__(self, r): #Construtor da classe.
        self.r = r

    def somar(self, a):
        self.r = self.r + a
        return self.r

    def dividir(self,a):
        self.r = self.r / a
        return self.r
    def oper(self, a, b):
        print("O valor da soma é " + str(self.somar(a, b)))

calc = Calculadora(10)
print("O valor inicial é: ", calc.r)
print("O valor da soma é ", calc.somar(2))
print(calc.dividir(2) + calc.somar(2))
# # print(str(calc.dividir(calc, 2,3)) + " " + str(calc.somar(calc, 2,3)))
# calc.oper(2,6)
num = ""
while num != "0":
    num = input("Digite um número:")
    print(calc.somar(int(num)))


