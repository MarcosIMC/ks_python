import sys
import os

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
    file = open(ruta, "r")
    print(file.read())
    file.close()

def load_directory(ruta):
    print("Cargando ruta")
    list = os.listdir(ruta)
    number_file = 1

    for file in list:
        print(str(number_file) + " - " + file)
        data =  open(os.path.join(ruta, file), "r")
        print(data.read())
        data.close()
        number_file = number_file+1

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
    if(len(sys.argv) > 1 and len(sys.argv) < 7):
        check_first_argument(sys.argv[1])
    else:
        help_menu()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
