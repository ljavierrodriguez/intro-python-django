class Calculadora:

    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def squart(num):
        return num * num 




print(Calculadora.suma(10, 10))
print(Calculadora.squart(10))