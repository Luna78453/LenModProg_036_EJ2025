from operacion import Operacion

class Raiz_Cuadrada(Operacion):
    def floor(num):
        n = int(num)
        f = float(n)

        if(f == num or num >= 0):
            return f
        else:
            return f - 1
        
    def cieling(num):
        n = int(num) + 1
        f = float(n)

        if(f == num or num >= 0):
            return f
        else:
            return f + 1

    def regresar_resultado(x):
        z = x
        return z