import Option_H
import sys
import os
import Check_args
from random import randint

def load_file(ruta):
    print("Cargando el fichero")
    file = open(ruta, "r")
    arr = eval(file.read())
    print(arr)
    file.close()
    quicksort(arr, 0, len(arr)-1)

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

def check_argument(*argv):
    txt: str = ""
    for i in argv:
        if i == '-d':
            txt += "opcion -d \n"
        if i == "-s":
           txt += "opcion -s \n"
    return txt

    """if first_argument == "-h":
        help_menu()
    elif first_argument == "-f":
        load_file(sys.argv[2])
    elif first_argument == "-d":
        load_directory(sys.argv[2])
    else:
        print("Estructura de la ejecución del método inválida, vea la ayuda a continuación.")
        help_menu()"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if(len(sys.argv) > 1 and len(sys.argv) < 7):
            Check_args.check__argument(sys.argv)
    else:
        Option_H


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
