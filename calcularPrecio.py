#
#   Laboratorio de Ingenieria de Software - Tarea 2
#
#   Autores:    - Jose Acevedo      13-10006
#               - Augusto Hidalgo   13-10665
#
import sys
import datetime
import decimal


# Objetos del tipo tarifa para dias durante semana y fines de semana.
class Tarifa:
    def __init__(self, semana, finDeSemana):
        self.semana = decimal.Decimal(semana)
        self.finDeSemana = decimal.Decimal(finDeSemana)
    
        
# Objetos para el intervalo de trabajo
class TiempoDeTrabajo:
    def __init__(self, inicioDeServicio, finDeServicio):
        self.inicioDeServicio = inicioDeServicio
        self.finDeServicio = finDeServicio

        
# Determina si el dia es fin de semana
def finDeSemana(dia):
    return  dia.weekday() == 5 or \
            dia.weekday() == 6


# Verificar tiempo de servicio valido
def verificarServicio(servicio):
    
    inicio = servicio.inicioDeServicio
    final  = servicio.finDeServicio
    
    try:
        assert((final-inicio).total_seconds() >= 15*60)
    except:
        print("Duracion de servicio debe ser mayor o igual a 15 minutos")
        sys.exit()

    try:
        assert((final-inicio).total_seconds() <= 7*24*3600)
    except:
        print("Duracion de servicio debe ser menor o igual a 7 dias")
        sys.exit()


# Verifica tarifa valida
def verificarTarifa(tarifa):
    try:
        assert(tarifa.semana >= 0 and tarifa.finDeSemana >= 0)
    except:
        print("Monto de tarifa no puede ser negativo")
        sys.exit()
    

# Calcula precio a pagar
def calcularPrecio(tarifa, tiempoDeServicio):

    verificarServicio(tiempoDeServicio)
    verificarTarifa(tarifa)

    precio = 0
    inicio = tiempoDeServicio.inicioDeServicio
    final  = tiempoDeServicio.finDeServicio

    # Primer dia de trabajo
    if finDeSemana(inicio):
        precio += (24 - inicio.hour) * tarifa.finDeSemana
    else:
        precio += (24 - inicio.hour) * tarifa.semana

    print(precio)

    # Dias intermedios de trabajo
    dia = (inicio.weekday() + 1) % 7
    for i in range((final.date() - inicio.date()).days - 1):
        if dia == 5 or dia == 6:
            precio += 24*tarifa.finDeSemana
        else:
            precio += 24*tarifa.semana

        dia = (dia + 1) % 7

    print(precio)

    # Ultimo dia de trabajo
    if(final > inicio):
        if finDeSemana(final):
            precio += final.hour * tarifa.finDeSemana
            if(final.minute > 0):
                precio += tarifa.finDeSemana
        else:
            precio += final.hour * tarifa.semana
            if(final.minute > 0 or final.second > 0):
                precio += tarifa.semana

        print(precio)

    return precio