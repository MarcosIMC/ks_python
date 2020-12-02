import time

class DataHandler():
    def handlerDataFile(self, list, benefit, start_time, id_items, id_list):
        if benefit:
            print("El valor de los objetos es de: ")
            result = 0
            for item in list:
                result = result + int(item)

            print(result)

            if id_items:
                for i in id_list:
                    print("Los identificadores de objetos son: ")
                    print(id_list[i])

        if start_time != 0:
            print("Se tardó: " + str((time.time() - start_time)))

        print("Programa finalizado correctamente.")