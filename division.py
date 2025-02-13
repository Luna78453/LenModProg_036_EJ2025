from operacion import Operacion

class Division(Operacion):
    @staticmethod
    def op(x, y):
        z = x / y
        return z