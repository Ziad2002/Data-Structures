class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None for i in range(0, self.capacity)]
        self.length = -1    

    def get(self, i: int) -> int:
        if i <= self.length and i >= 0:
            return self.array[i]
        else:
            print("value not set yet")

    def set(self, i: int, n: int) -> None:
        if i <= self.capacity:
            self.array[i] = n
            
        else:
            print("index out of range")

    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            self.resize()
            self.length += 1
            self.array[self.length] = n
        else:
            self.length += 1
            self.array[self.length] = n

    def popback(self) -> int:
        val = self.array[self.length]
        self.array[self.length] = None
        self.length -= 1

        return val

    def resize(self) -> None:
        new_array = [None for i in range(0, 2*self.capacity)]
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        
        self.capacity = self.capacity * 2
        self.array = new_array

    def getSize(self) -> int:
        return self.length+1
    
    def getCapacity(self) -> int:
        return self.capacity