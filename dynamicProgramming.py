import sys
from random import randint


class DynamicProgramming():
    def tabultaion(self, arr_datas, arr_size):
        #Caso base si el valor encontrado es 0 devolvemos infinito
        if arr_datas[0] == 0:
            return sys.maxsize

        aux=[sys.maxsize]*arr_size
        aux[0] = 0

        for i in range(0,arr_size):
            for j in range(1, arr_size):
                if j <= min(arr_size-1, int(arr_datas[i])) and i+j < arr_size:
                    if aux[i+j] != sys.maxsize:
                        aux[i+j] = min(aux[i+j], aux[i]+1)
                    else:
                        aux[i+j] = aux[i]+1
        return aux[arr_size-1]

    def memoization(self, arr_datas, i, arr_size, aux):
        if i == arr_size-1:
            return 0

        if i >= arr_size or arr_datas[i] == 0:
            return sys.maxsize

        if aux[i] != 0:
            return aux[i]

        min_jumps = sys.maxsize
        for j in range(i+1, arr_size):
            if j <= i+int(arr_datas[i]):
                cost = self.memoization(arr_datas, j, arr_size, aux)
                if cost != sys.maxsize:
                    min_jumps = min(min_jumps, cost+1)

        aux[i] = min_jumps
        return aux[i]
