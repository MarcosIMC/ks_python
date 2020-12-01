class DataHandler():
    def handlerDataFile(self, list):
        print("El valor de los objetos es de: ")
        result = 0
        for item in list:
            result = result + int(item)

        print(result)