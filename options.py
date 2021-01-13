import sys

from fileManagerReader import FileManagerReader

check = False
time = False

class Options():

    def __init__(self):
        if 1 < len(sys.argv) <= 6:
            self.check_first_argument(sys.argv[1])
        else:
            self.help_menu()

    def help_menu(self):
        print("Ayuda para el comando:")
        print("La estructura del comando es: main.py (opcion -d ó -f) ruta (estilo -sm ó -st) (opción: -t -check)")
        print()
        print("------------------------------------------------------------------------------------")
        print("Descripción de las opciones:")
        print("-h -> Muestra la ayuda del programa.")
        print("-f -> Especifica el nombre del fichero que vamos a usar como datos de entrada.")
        print("-d -> Especifica el directorio que contiene todos los ficheros a procesar.")
        print("-----------------------------------------------------------------------------------")
        print("-sm -> memoization, ejecuta la solución de memoization")
        print("-st -> tabulation, ejecuta la solución de tabulation")
        print("-check -> Comprueba que el resultado calculado mediante Memoization y Tabulation coincide.")
        print("-t -> Muestra el tiempo en segundos de la ejecución.")
        print("Ejemplo de llamada:")
        print("ks.py [-h (ayuda)] [-d ó -f] [-sm ó -st] [-t] [-check]")

    def check_options(self):
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "-t":
                global time
                time = True

            elif sys.argv[i] == "-check":
                global check
                check = True

            i = i + 1

    def check_first_argument(self, first_argument):
        self.check_options()
        if first_argument == "-h":
            self.help_menu()
        elif first_argument == "-f":
            fmr = FileManagerReader()
            fmr.load_file(sys.argv[2], sys.argv[3], time, check)
            print("Programa finalizado correctamente.")
            exit()
        elif first_argument == "-d":
            fmr = FileManagerReader()
            fmr.load_directory(sys.argv[2], sys.argv[3], time, check)
            print("Programa finalizado correctamente.")
            exit()
        else:
            print("Estructura de la ejecución del método inválida, vea la ayuda a continuación.")
            self.help_menu()