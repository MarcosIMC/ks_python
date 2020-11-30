from io import open
from typing import List, Any
from time import time
from QuickSort import quicksort


class Bag:

    n_elements: int = 0
    freeSpace: int = 0
    elementsValue: int = 0
    listValue: list = []
    listWeight: list = []
    origin_list: list = []
    dt: list = []
    ttime = 0

    def __init__(self, route):
        start_time = time()
        file = open(route, "r")
        arr = file.readlines()
        file.close()
        for i in range(len(arr)):
            if i == 0:
                vec = arr[i].split()
                self.n_elements = int(vec[0])
                self.freeSpace = int(vec[1])
            else:
                vec = arr[i].split()
                self.listValue.append(int(vec[0]))
                self.listWeight.append(int(vec[1]))
                self.origin_list.append(int(vec[0]))
        quicksort(self.listValue, 0, self.n_elements - 1)
        quicksort(self.listWeight, 0, self.n_elements - 1)
        self.get_by_max_value()
        self.ttime = time() - start_time

    def get_value(self):
        return self.listValue

    def get_weight(self):
        return self.listWeight

    def value_bag(self):
        return self.elementsValue

    def get_space(self):
        return self.freeSpace

    def get_dt(self):
        return self.dt

    def get_time(self):
        return self.ttime

    def get_by_max_value(self):
        for i in range(self.n_elements):
            if self.freeSpace >= self.listWeight[i]:
                self.freeSpace -= self.listWeight[i]
                self.elementsValue += self.listValue[i]
                for j in range(self.n_elements):
                    if self.listValue[i] == self.origin_list[j]:
                        self.dt.append(j)
                        break
            if self.freeSpace == 0:
                break
