#
#   Laboratorio de Ingenieria de Software - Tarea 2
#
#   Autores:    - Jose Acevedo      13-10006
#               - Augusto Hidalgo   13-10665
#
import sys
import datetime
import decimal


# Verificar tiempo de servicio valido
def verificarServicio(inicio, final):
    
    try:
        assert((final-inicio).total_seconds() >= 15*60)
    except:
        return("Duracion de servicio debe ser mayor o igual a 15 minutos")
        sys.exit()

    try:
        assert((final-inicio).total_seconds() <= 7*24*3600)
    except:
        return("Duracion de servicio debe ser menor o igual a 7 dias")
        sys.exit()


# Verifica tarifa valida
def verificarTarifa(semana, finDeSemana):
    try:
        assert(semana >= 0 and finDeSemana >= 0)
    except:
        return("Monto de tarifa no puede ser negativo")
        sys.exit()


# Objetos del tipo tarifa para dias durante semana y fines de semana.
class Tarifa:
    def __init__(self, semana, finDeSemana):
        verificarTarifa(semana, finDeSemana)
        self.semana = decimal.Decimal(semana)
        self.finDeSemana = decimal.Decimal(finDeSemana)
    
        
# Objetos para el intervalo de trabajo
class TiempoDeTrabajo:
    def __init__(self, inicioDeServicio, finDeServicio):
        verificarServicio(inicioDeServicio, finDeServicio)
        self.inicioDeServicio = inicioDeServicio
        self.finDeServicio = finDeServicio

        
# Determina si el dia es fin de semana
def finDeSemana(dia):
    return  dia.weekday() == 5 or \
            dia.weekday() == 6
    

# Calcula precio a pagar
# 
#    - Dominio de Datos:
#    
#        El dominio de la función consta de pares ordenados cuya 1ra coordenada es
#        un objeto del tipo tarifa y la 2da coordenada es un objeto de tipo tiempoDeServicio.
#
#        La tarifa determinar el monto a pagar por hora en dias de semana y fines de semana.
#        Los montos no pueden ser negativos.
#
#        El tiempoDeServicio almacena el tiempo transcurrido del trabajo. Dicho tiempo se encuentra
#        entre 15 minutos y 7 dias.
#
def calcularPrecio(tarifa, tiempoDeServicio):

    precio = 0
    inicio = tiempoDeServicio.inicioDeServicio
    final  = tiempoDeServicio.finDeServicio
    
    dia = inicio
    while dia < final:
        if finDeSemana(dia):
            precio += tarifa.finDeSemana
        else:
            precio += tarifa.semana
        dia += datetime.timedelta(hours=1)

    return precio
