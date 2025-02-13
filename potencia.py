from operacion import Operacion

class Potencia(Operacion):
    @staticmethod
    def op(x, y):
        i = 0
        z = x

        while i < y:
            z *= z

        return z