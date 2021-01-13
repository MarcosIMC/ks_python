import os
import time
import csv

from dataHandler import DataHandler
from dynamicProgramming import DynamicProgramming

id_list = []

class FileManagerReader():

    def load_file(self, ruta, method, clock, check):
        global aux
        print("Cargando el fichero")
        arr_datas = []

        with open(ruta, "r") as datas:
            record = csv.reader(datas, delimiter=',')
            for data in record:
                arr_datas = data

        datas.close()
        dp = DynamicProgramming()
        start_time = 0

        if clock:
            start_time = time.time()

        if method == "-sm":
            aux = [0]*len(arr_datas)
            aux = dp.memoization(arr_datas, 0, len(arr_datas), aux)
        elif method == "-st":
            aux = dp.tabultaion(arr_datas, len(arr_datas))
        dh = DataHandler()
        dh.handlerDataFile(aux, method)

        if check:
            if method == "-sm":
                aux = dp.tabultaion(arr_datas, len(arr_datas))
                dh.handlerDataFile(aux, "-st")
            else:
                aux = [0]*len(arr_datas)
                aux = dp.memoization(arr_datas, 0, len(arr_datas), aux)
                dh.handlerDataFile(aux, "-sm")

        if start_time != 0:
            print("Se tardó: ", time.time() - start_time)

    def load_directory(self, ruta, method, clock, check):
        print("Cargando todos los ficheros de la ruta")
        list = os.listdir(ruta)
        number_file = 1
        arr_datas = []
        start_time = 0
        if clock:
            start_time = time.time()

        for file in list:
            print(str(number_file) + " - " + file)
            with open(os.path.join(ruta, file), "r") as datas:
                record = csv.reader(datas, delimiter=',')

                for data in record:
                    arr_datas = data

                datas.close()
                dp = DynamicProgramming()

                if method == "-st":
                    aux = dp.tabultaion(arr_datas, len(arr_datas))
                else:
                    aux = [0]*len(arr_datas)
                    aux = dp.memoization(arr_datas, 0, len(arr_datas), aux)

                dh = DataHandler()
                dh.handlerDataFile(aux, method)

                if check:
                    if method == "-st":
                        aux = [0]*len(arr_datas)
                        aux = dp.memoization(arr_datas, 0, len(arr_datas), aux)
                        dh.handlerDataFile(aux, "-sm")
                    else:
                        aux = dp.tabultaion(arr_datas, len(arr_datas))
                        dh.handlerDataFile(aux, "-st")

            number_file = number_file + 1
        if start_time != 0:
            print("Se tardó: ",time.time() - start_time)