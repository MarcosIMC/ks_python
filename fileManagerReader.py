import os

from dataHandler import DataHandler
from sortManager import SortManager


class FileManagerReader():

    def load_file(self, ruta):
        print("Cargando el fichero")
        arr_value = []
        arr_weight = []
        first = True
        num_items = 0
        global max_weight
        max_weight = 0
        with open(ruta, "r") as datas:
            for data in datas:
                aux = data.split()
                if first:
                    num_items = aux[0]
                    max_weight = int(aux[1])
                    first = False
                else:
                    arr_value.append(aux[0])
                    arr_weight.append(aux[1])

        datas.close()
        sm = SortManager()

        sm.quicksort(arr_value, arr_weight, 0, len(arr_value) - 1)

        items_bag = sm.greedy_algorithm(arr_value, arr_weight, num_items, max_weight)
        dh = DataHandler()
        dh.handlerDataFile(items_bag)


    def load_directory(self, ruta):
        print("Cargando todos los ficheros de la ruta")
        list = os.listdir(ruta)
        number_file = 1
        arr_value = []
        arr_weight = []
        first = True
        num_items = 0

        for file in list:
            print(str(number_file) + " - " + file)
            with open(os.path.join(ruta, file), "r") as datas:
                for data in datas:
                    aux = data.split()
                    if first:
                        num_items = aux[0]
                        max_weight = int(aux[1])
                        first = False
                    else:
                        arr_value.append(aux[0])
                        arr_weight.append(aux[1])

                datas.close()
                sm = SortManager()
                sm.quicksort(arr_value, arr_weight, 0, len(arr_value) - 1)
                items_bag = sm.greedy_algorithm(arr_value, arr_weight, num_items, max_weight)
                dh = DataHandler()
                dh.handlerDataFile(items_bag)
                first = True
                arr_value = []
                arr_weight = []
                num_items = 0
                max_weight = 0

            number_file = number_file + 1