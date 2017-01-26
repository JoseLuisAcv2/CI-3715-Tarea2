#
#   Laboratorio de Ingenieria de Software - Tarea 2
#
#   Autores:    - Jose Acevedo      13-10006
#               - Augusto Hidalgo   13-10665
#

import unittest
from datetime import *
from decimal import Decimal
from calcularPrecio import *
from logging import exception

# Pruebas para la clase de Tarifa
class TestTarifa(unittest.TestCase):
    
    def testTarifaNegativaSemana(self):
        try:
            t = Tarifa("-1","1")
        except:
            pass
            
    def testTarifaNegativaFinDeSemana(self):
        try:
            t = Tarifa("1","-1")
        except:
            pass

    def testTarifaNula(self):
        t = Tarifa("0","0")
        self.assertEqual(t.semana,Decimal("0"))
        self.assertEqual(t.finDeSemana,Decimal("0"))

    def testTarifaValida(self):
        t = Tarifa("10","20")
        self.assertEqual(t.semana,Decimal("10"))
        self.assertEqual(t.finDeSemana,Decimal("20"))


# Pruebas para la clase de Tiempos de Servicio
class TestTiempoDeServicio(unittest.TestCase):
    
    def testTiempoDeServicioCorrecto(self):
        t = TiempoDeTrabajo(datetime.datetime(2017,01,21,2,30),datetime.datetime(2017,01,28,10,15))
        self.assertEqual(t.inicioDeServicio,datetime.datetime(2017,01,21,2,30))
        self.assertEqual(t.finDeServicio,datetime.datetime(2017,01,28,10,15))

    def testTiempoDeServicioNegativo(self):
        # Servicio de 10min
        try:
            t = TiempoDeTrabajo(datetime.datetime(2017,02,30),datetime.datetime(2017,01,30,0,10))
        except:
            pass
        else:
            self.assertIsNotNone(t)
    
    def testTiempoDeServicioCorto(self):
        # Servicio de 10min
        try:
            t = TiempoDeTrabajo(datetime.datetime(2017,01,30),datetime.datetime(2017,01,30,0,10))
        except:
            pass
        else:
            self.assertIsNotNone(t)

    def testTiempoDeServicioMinimo(self):
        # Servicio de 15min
        try:
            t = TiempoDeTrabajo(datetime.datetime(2017,01,30),datetime.datetime(2017,01,30,0,15))
        except:
            assert False
        
    def testTiempoDeServicioMaximo(self):
        # Servicio de 7 dias
        try:
            t = TiempoDeTrabajo(datetime.datetime(2017,01,21),datetime.datetime(2017,01,28))
        except:
            assert False

    def testTiempoDeServicioLargo(self):
        # Servicio de 10 dias
        try:
            t = TiempoDeTrabajo(datetime.datetime(2017,01,20),datetime.datetime(2017,01,30))
        except:
            pass
        else:
            self.assertIsNotNone(t)
            

# Pruebas para la verificar correctitud de precios.
class TestCalcularPrecio(unittest.TestCase):

    def testCosto15minSemana(self):
        tarifa = Tarifa("15","2.8")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,20,0,15),datetime.datetime(2017,01,20,0,30))
        self.assertEqual(calcularPrecio(tarifa,tiempo),15)

    def testCosto30minSemana(self):
        tarifa = Tarifa("30","2")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,20,0),datetime.datetime(2017,01,20,0,30))
        self.assertEqual(calcularPrecio(tarifa,tiempo),30)
    
    def testCosto1horaSemana(self):
        tarifa = Tarifa("1","2")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,20,0),datetime.datetime(2017,01,20,1))
        self.assertEqual(calcularPrecio(tarifa,tiempo),1)

    def testCosto24horaSemana(self):
        tarifa = Tarifa("1","0")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,20),datetime.datetime(2017,01,21))
        self.assertEqual(calcularPrecio(tarifa,tiempo),24)

    def testCosto3diasSemana(self):
        tarifa = Tarifa("3","0")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,17),datetime.datetime(2017,01,20))
        self.assertEqual(calcularPrecio(tarifa,tiempo),216)
        
    def testCosto15minFinDeSemana(self):
        tarifa = Tarifa("1","2")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,28,0,15),datetime.datetime(2017,01,28,0,30))
        self.assertEqual(calcularPrecio(tarifa,tiempo),2)

    def testCosto30minFinDeSemana(self):
        tarifa = Tarifa("30","40")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,28,0),datetime.datetime(2017,01,28,0,30))
        self.assertEqual(calcularPrecio(tarifa,tiempo),40)
    
    def testCosto1horaFinDeSemana(self):
        tarifa = Tarifa("1","2")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,28,14,30),datetime.datetime(2017,01,28,15,30))
        self.assertEqual(calcularPrecio(tarifa,tiempo),2)

    def testCosto24horaFinDeSemana(self):
        tarifa = Tarifa("1","10")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,28,13),datetime.datetime(2017,01,29,13))
        self.assertEqual(calcularPrecio(tarifa,tiempo),240)

    def testCosto2diasFinDeSemana(self):
        tarifa = Tarifa("1000","1")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,28),datetime.datetime(2017,01,30))
        self.assertEqual(calcularPrecio(tarifa,tiempo),48)

    def testCostoCambiodeDia(self):
        tarifa = Tarifa("1","0.5")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,18,23,30),datetime.datetime(2017,01,19,1,30))
        self.assertEqual(calcularPrecio(tarifa,tiempo),2)

    def testCostoSemanayLuegoFin(self):
        tarifa = Tarifa("1","10")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,20,23),datetime.datetime(2017,01,21,1))
        self.assertEqual(calcularPrecio(tarifa,tiempo),11)

    def testCostoFinyLuegoSemana(self):
        tarifa = Tarifa("1","10")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,22,23),datetime.datetime(2017,01,23,1))
        self.assertEqual(calcularPrecio(tarifa,tiempo),11)

    def testCosto7dias(self):
        tarifa = Tarifa("1","10")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,16),datetime.datetime(2017,01,23))
        self.assertEqual(calcularPrecio(tarifa,tiempo),600)

    def testCobrarHoraCompletaPorMinutosSobrantes(self):
        tarifa = Tarifa("1","10")
        tiempo = TiempoDeTrabajo(datetime.datetime(2017,01,20,10),datetime.datetime(2017,01,20,11,1))
        self.assertEqual(calcularPrecio(tarifa,tiempo),2)
        

if __name__ == "__main__":
    unittest.main()