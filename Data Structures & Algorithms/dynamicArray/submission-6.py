class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = capacity
        self.arr = [0] * self.size
        self.end_index = 0


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.end_index == self.size:
            self.resize()
        self.arr[self.end_index] = n
        self.end_index += 1

    def popback(self) -> int:
        self.end_index -= 1
        output = self.arr[self.end_index]
        return output

    def resize(self) -> None:
        self.size = self.size * 2
        new_arr = [0] * self.size
        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.end_index
    
    def getCapacity(self) -> int:
        return self.size
