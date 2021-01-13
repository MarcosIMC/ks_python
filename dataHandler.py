import time
import sys

class DataHandler():
    def handlerDataFile(self, list, method):
        print("El número de saltos mínimo requerido en " + method)
        if list != 0 and list != sys.maxsize:
            print("Saltos requeridos: " + str(list))
        elif list == sys.maxsize:
            print("Saltos requeridos: Infinito")
        else:
            print("Error en la matriz de entrada")