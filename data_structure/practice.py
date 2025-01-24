import ctypes

class Dynamic_Array:
    
    def __init__(self):
        self.size=1
        self.num=0
        self.Array=self.__make_array(self.size)
    
    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.num

val=Dynamic_Array()
print(val.__len__())