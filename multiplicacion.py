from operacion import Operacion

class Multiplicacion(Operacion):
   @staticmethod
   def op(x, y):
        z = x * y
        return z