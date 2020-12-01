from random import randint


class SortManager():
    def quicksort(self, arr_value, arr_weight, start, end):
        if start < end:  # La vamos a ordenar por el valor de los pesos
            index = self.partition(arr_weight, arr_value, start, end)
            # Se llama así misma la función cambiando los valores de start o end por el del indice
            self.quicksort(arr_value, arr_weight, start, index - 1)
            self.quicksort(arr_value, arr_weight, index + 1, end)

    def partition(self, arr_weight, arr_value, start, end):
        pivot = randint(start, end)  # Escogemos un valor aleatorio entre los rangos
        # Intercambiamos los valores de ambas listas para poner el del pivoteo al final y el del final al pivoteo
        last_element = arr_value[end]
        last_element_weight = arr_weight[end]
        arr_value[end] = arr_value[pivot]
        arr_weight[end] = arr_weight[pivot]
        arr_value[pivot] = last_element
        arr_weight[pivot] = last_element_weight

        index = start  # Puntero de la lista (Inicio)
        # print(index)

        for i in range(start, end):
            if arr_weight[i] <= arr_weight[end]:
                # Mientras coincida que es menor, avanzamos el indice de la lista
                index += 1

        # Intercambiamos el final, por el valor del indice, ya que ese valor es mayor al del pivote.
        aux_1 = arr_value[end]
        aux_weight1 = arr_weight[end]
        arr_value[end] = arr_value[index]
        arr_weight[end] = arr_weight[index]
        arr_value[index] = aux_1
        arr_weight[index] = aux_weight1

        # Retorno del indice ya que lo que esta anterior a el esta ordenado
        return index

    def greedy_algorithm(self, arr_value, arr_weight, num_items, max_weight):
        i = 0
        items_bag = []

        while int(num_items) != 0:
            item_select = int(arr_value[i])
            arr_value[i] = 0
            if int(arr_weight[i]) <= int(max_weight):
                max_weight = max_weight - int(arr_weight[i])
                items_bag.append(item_select)
                num_items = int(num_items) - 1
            else:
                num_items = 0

            i = i + 1
        print("El peso libre en la mochila es de: " + str(max_weight))
        max_weight = 0
        return items_bag