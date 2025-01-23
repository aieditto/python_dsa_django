import ctypes

class MeraList:
    def __init__(self):
        self.size=1
        self.n=0
        self.Array=self.__make_array(self.size)
        
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self, item):
        if self.n == self.size:
             self.__resize(self.size*2)
        
        self.Array[self.n]=item
        self.n+=1
    
    def __resize(self, new_capacity):
        Barry=self.__make_array(new_capacity)
        self.size=new_capacity
        
        for i in range(self.n):
           Barry[i] = self.Array[i]
        self.Array = Barry
    
    def __str__(self):
        result=''
        for i in range(self.n):
            result+=str(self.Array[i])+','
        return '['+ result[:-1] + ']' 
    
    def pop(self):
        if self.n==0:
            print('Nothing Left')
        else:
            print(self.Array[self.n-1])
            self.n-=1
        
    def indexing(self,index):
        if 0<=index<self.n:
            return self.Array[index]
        else:
            return 'Not found'
    
    def clear(self):
        self.size=1
        self.n=0
     
    def find(self,value):
         for i in range(self.n):
            if value==self.Array[i]:
                return i 
                 
            else:
                return 'value not found'       
    
test=MeraList()
print(test.__len__())
test.append(5)
test.append(3)
test.append(4)
test.append(2)
print(test)
# test.pop()
# print(test.__len__())
# print(test.indexing(2))
# print(test.clear())
print(test.find(2))
        