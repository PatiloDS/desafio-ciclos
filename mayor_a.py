#Patricio Carrasco
import sys

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

monto = int(sys.argv[1])
for meses, ventasM in ventas.items():
    meses is str and ventasM is int
    if ventasM > monto:
        print(meses, ":", ventasM)
