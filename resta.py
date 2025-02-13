from operacion import Operacion

class Resta(Operacion):
    @staticmethod
    def op(x, y):
        z = x - y
        return z