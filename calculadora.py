from division import Division
from multiplicacion import Multiplicacion
from suma import Suma
from resta import Resta
from potencia import Potencia

sumador = Suma()
restador = Resta()
multiplicador = Multiplicacion()
divididor = Division()
exponenciador = Potencia()

print (divididor.op(sumador.op(restador.op(58, 56), 100), multiplicador.op(2, exponenciador.op(2,4))))