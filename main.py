import sys
import os

from random import randint


def help_menu():
    print("Ayuda para el comando:")
    print("La estructura del comando es: main.py (opcion -d ó -f) ruta (opción -b, -r, -t, -dt)")
    print()
    print("------------------------------------------------------------------------------------")
    print("Descripción de las opciones:")
    print("-h -> Muestra la ayuda del programa.")
    print("-f -> Especifica el nombre del fichero que vamos a usar como datos de entrada.")
    print("-d -> Especifica el directorio que contiene todos los ficheros a procesar.")
    print("-b Muestra el beneficio de los items obtenidos.")
    print("-r Muestra el peso sobrante en la mochila.")
    print("-t Muestra el tiempo en segundos de la ejecución.")
    print("-dt Muestra el identificador de los objetos elegidos.")
    print("-----------------------------------------------------------------------------------")


def load_file(ruta):
    print("Cargando el fichero")
    arr_value = []
    arr_weight = []
    first = True
    num_items = 0
    max_weight = 0
    with open(ruta, "r") as datas:
        for data in datas:
            aux = data.split()
            if first:
                num_items = aux[0]
                max_weight = aux[1]
                first = False
            else:
                arr_value.append(aux[0])
                arr_weight.append(aux[1])

        datas.close()
        print(arr_value)
        print(arr_weight)
        quicksort(arr_value, arr_weight, 0, len(arr_value)-1)
        print(arr_value)
        print(arr_weight)


def load_directory(ruta):
    print("Cargando todos los ficheros de la ruta")
    list = os.listdir(ruta)
    number_file = 1

    for file in list:
        print(str(number_file) + " - " + file)

        data = open(os.path.join(ruta, file), "r")
        # print(data.read())
        arr = eval(data)
        data.close()
        quicksort(arr, 0, len(arr) - 1)
        number_file = number_file + 1


def quicksort(arr_value, arr_weight, start, end):
    if start < end: #La vamos a ordenar por el valor de los pesos
        index = partition(arr_weight, arr_value, start, end)
        #Se llama así misma la función cambiando los valores de start o end por el del indice
        quicksort(arr_value, arr_weight, start, index - 1)
        quicksort(arr_value, arr_weight, index + 1, end)


def partition(arr_weight, arr_value, start, end):
    pivot = randint(start, end)  # Escogemos un valor aleatorio entre los rangos
    #Intercambiamos los valores de ambas listas para poner el del pivoteo al final y el del final al pivoteo
    last_element = arr_value[end]
    last_element_weight = arr_weight[end]
    arr_value[end] = arr_value[pivot]
    arr_weight[end] = arr_weight[pivot]
    arr_value[pivot] = last_element
    arr_weight[pivot] = last_element_weight

    index = start #Puntero de la lista (Inicio)
    print(index)

    for i in range(start, end):
        print(i)
        if arr_weight[i] <= arr_weight[end]:
            #Mientras coincida que es menor, avanzamos el indice de la lista
            index += 1

    #Intercambiamos el final, por el valor del indice, ya que ese valor es mayor al del pivote.
    aux_1 = arr_value[end]
    aux_weight1 = arr_weight[end]
    arr_value[end] = arr_value[index]
    arr_weight[end] = arr_weight[index]
    arr_value[index] = aux_1
    arr_weight[index] = aux_weight1

    #Retorno del indice ya que lo que esta anterior a el esta ordenado
    return index


def check_first_argument(first_argument):
    if first_argument == "-h":
        help_menu()
    elif first_argument == "-f":
        load_file(sys.argv[2])
    elif first_argument == "-d":
        load_directory(sys.argv[2])
    else:
        print("Estructura de la ejecución del método inválida, vea la ayuda a continuación.")
        help_menu()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if 1 < len(sys.argv) < 7:
        check_first_argument(sys.argv[1])
    else:
        help_menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
