import Option_H
import sys
import os
from Bag import Bag
from random import randint

def load_file(ruta):
    print("Cargando el fichero")
    file = open(ruta, "r")
    arr = eval(file.read())
    for i in arr:
        print(i)
    file.close()
    #quicksort(arr, 0, len(arr)-1)

def load_directory(ruta):
    print("Cargando todos los ficheros de la ruta")
    list = os.listdir(ruta)
    number_file = 1

    for file in list:
        print(str(number_file) + " - " + file)
        data =  open(os.path.join(ruta, file), "r")
        #print(data.read())
        arr = eval(data)
        data.close()
        quicksort(arr, 0, len(arr)-1)
        number_file = number_file+1

def quicksort(arr, start, end):
    if start < end:
        index = partition(arr, start, end)
        quicksort(arr, start, index-1)
        quicksort(arr, index+1, end)

def partition(arr, start, end):
    pivot = randint(start, end) #Escogemos un valor aleatorio entre los rangos
    last_element = arr[end]
    arr[end] = arr[pivot]
    arr[pivot] = last_element

    index = start

    for i in range(start, end):
        if arr[i] <= arr[end]:
            aux = arr[i]
            arr[i] = arr[index]
            arr[index] = aux
            index += 1
        aux_1 = arr[end]
        arr[end] = arr[index]
        arr[index] = aux_1

        return index


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if(len(sys.argv) > 1 and len(sys.argv) < 7):
        for i in range(0, len(sys.argv)):
            if sys.argv[1] == "-f" and i == 1:
                print(sys.argv[i])
                mochila = Bag(sys.argv[2])
    else:
        Option_H

    print(mochila.getValue())
    print(mochila.getWeight())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
