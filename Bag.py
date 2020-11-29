from io import open
from QuickSort import quicksort
class Bag:
    n_elements = 0
    freeSpace = 0
    elementsValue = 0
    listValue = []
    listWeight =[]


    def __init__(self, route):
        file = open(route, "r")
        arr = file.readlines()
        file.close()
        for i in range (len(arr)):
            if i == 0:
                vec = arr[i].split()
                self.n_elements = int(vec[0])
                self.freeSpace = int(vec[1])
            else:
                vec = arr[i].split()
                self.listValue.append(int(vec[0]))
                self.listWeight.append(int(vec[1]))
        quicksort(self.listValue,0,self.n_elements -1)
        quicksort(self.listWeight, 0, self.n_elements - 1)

    def getValue(self):
        return self.listValue
    def getWeight(self):
        return self.listWeight

