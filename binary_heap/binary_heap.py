class BinaryHeap(object):
    def __init__(self, values=None):
        if values:
            self.values = values
            self._sort()
        else:
            self.values = []
    
    def _switch(self, p_index, c_index):
        self.values[p_index], self.values[c_index] = self.values[c_index], self.values[p_index]
        
    def _sort(self):
        for index, element in enumerate(self.values):
            p_index = (index - 1) // 2
            if p_index < 0:
                p_index = 0
            if element > self.values[p_index]:
                self._switch(p_index, index)
                self._sort()
        return self.values

    def pop(self):
        if self.values:
            value = self.values.pop(0)
            self._sort()
            return value
        else:
            raise IndexError
            
    
    def push(self, value):
        self.values.append(value)
        self._sort()
    
if __name__ == "__main__":
    pass
    
    