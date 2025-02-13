from operacion import Operacion

class Suma(Operacion):
    @staticmethod
    def op(x, y):
        z = x + y
        return z