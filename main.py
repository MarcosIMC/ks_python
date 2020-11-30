
import sys
from Bag import Bag


"""def load_directory(ruta):
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
        number_file = number_file+1"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """if(len(sys.argv) > 1 and len(sys.argv) < 7):
        for i in range(0, len(sys.argv)):
            if sys.argv[1] == "-f" and i == 1:
                print(sys.argv[i])
                mochas = Bag(sys.argv[2])
    else:
        Option_H

    print(mochila.getValue())
    print(mochila.getWeight())"""

    for i in range(0, len(sys.argv)):
        if sys.argv[1] == "-f" and i == 1:
            print(sys.argv[i])
            mochila = Bag(sys.argv[2])
print("lista ordenada valores", mochila.get_value())
print("lista ordenada pesos", mochila.get_weight())
print("valor obtenido", mochila.value_bag())
print("espacio final", mochila.get_space())
print("indices", mochila.get_dt())
print("lista original valores", mochila.origin_list)
print("tiempo en segundos ", mochila.get_time())
