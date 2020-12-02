import sys

from fileManagerReader import FileManagerReader

free_space = False
benefit = False
time = False
id_objects = False

class Options():

    def __init__(self):
        if 1 < len(sys.argv) <= 7:
            self.check_first_argument(sys.argv[1])
        else:
            self.help_menu()

    def check_first_argument(self, first_argument):

        if first_argument == "-h":
            self.help_menu()
        elif first_argument == "-f":
            self.check_options()
            fmr = FileManagerReader()
            fmr.load_file(sys.argv[2], free_space, benefit, time, id_objects)
        elif first_argument == "-d":
            self.check_options()
            fmr = FileManagerReader()
            fmr.load_directory(sys.argv[2], free_space, benefit, time, id_objects)
        else:
            print("Estructura de la ejecución del método inválida, vea la ayuda a continuación.")
            self.help_menu()

    def help_menu(self):
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

    def check_options(self):
        i = 3
        print(len(sys.argv))
        while i < len(sys.argv):
            if sys.argv[i] == "-r":
                global free_space
                free_space = True

            elif sys.argv[i] == "-b":
                global benefit
                benefit = True

            elif sys.argv[i] == "-t":
                global time
                time = True

            elif sys.argv[i] == "-dt":
                global id_objects
                id_objects = True

            i = i + 1