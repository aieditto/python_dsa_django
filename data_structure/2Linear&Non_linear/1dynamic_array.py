"""
Data Structure
1. Time Complexity:
Big O Notation

2. Linear VS Non-Linear
Linear:
One after one
1. Array,
2. Linked list,
3. Stack
4. Queue
5. Hashing

Non-Linear:
1. Tree
2. Graph
3. Heap
4. Trie
5. Set
"""

                            #Array
"""
Array:
Array is a linear data structure. Its kind like the list but the biggest difference Is an Array can store only same data type and array sizes are fixed. When declares any array the sizes of array need to declare. 

Disadvantage:
1.	Fixed size (memory waste)
2.	Homogenous (lack of flexibility)

For avoiding homogenous array or normal array I can use referential array.
Referential array is kinda different from normal array because it A Referential Array is an array that stores references to objects or other data structures rather than the actual data itself. In programming, particularly in object-oriented languages like Java, Python, or C#, referential arrays are widely used to hold references to instances of classes or other complex data types. 


Disadvantage:
1.	This are slower than normal array because of when a value is search from the array usually in normal array the value is directly search from the array in linear way by using address. But in Referential Array when any value Is search from the array it first search from the address number then the address pointer the value address which are attach with the value. Then the expected value can be find.

The major issue for static array is fixed size array.
So, the solution is dynamic array. Dynamic array its actually depend on the concept there are doesn’t any special keyword 

Dynamic array is not fixed array. The size is increase as the given input. The biggest similarity is in Python Language List are the Dynamic Array. 

For Example:

List is kind of dynamic array

Code: 
import sys  (system specific)
empty_list=[]

for i in range(0,100):
    print(i,sys.getsizeof(empty_list))
    empty_list.append(i)

0 56
    +32 (add on storage)
1 88 
2 88 
3 88 
4 88 
    +32
5 120
6 120
7 120
8 120
    +64
9 184
10 184
11 184

"""

    
import ctypes
# ctypes is a foreign function library for Python. 
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries

class Meralist:
    def __init__(self):
        self.size= 1 #how many storage
        self.n= 0 #how many number are store
        # create a C type array with size = self.size
        self.Array = self.__make_array(self.size)
        #self Array as a array
    
    #__len__ is not a private method its a special method for finding the length
    def __len__(self):
        return self.n
    
               
    def __make_array(self, capacity):
        #creates a C type array(static,referential) with size-->capacity
        return (capacity*ctypes.py_object)()
    
    def append(self, item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)
        
        #append
        # jodi jaiga khali thake shei khetre array er Nth jaigai value boshe
        # jaa ager n e chilo ta toh  item e thake sheta abr notun n rakha hoi erpr 1 kre increment kre dei size
        self.Array [self.n] = item
        self.n=self.n+1
    
    def __resize(self, new_capacity):
        #create a new array with new capacity
        B_NEW_Array = self.__make_array(new_capacity)
        self.size = new_capacity #already double size than Array
        #copy Array element to B_NEW_Array
        for i in range (self.n):
            B_NEW_Array[i]=self.Array[i]
        
        #reasign Array
        self.Array = B_NEW_Array
        
    
    #for printing the whole list
    def __str__(self):
        result = ''
        for i in range (self.n):
            result = result + str(self.Array[i])+','
        return '['+ result[:-1] + ']' # result.strip(',') can use
    
    #for indexing it helps to finds value by index
    def __getitem__(self,index):
        if 0 <= index <self.n:
            return self.Array[index]
        else:
            return 'index not found'
        
    #popping
    def pop(self):
        if self.n==0:
            return 'emptylist'
        else:
            print(self.Array[self.n-1])
            self.n=self.n-1
    
    #clear
    def clear(self):
        self.n=0
        self.size=1
    
    #find use for searching value by their value
    def find(self,value):
        for i in range(self.n):
            if self.Array[i]==value:
                return i  
        return 'value not found'  
    
    
    #insertion
    def insertion(self, pos, value):
        # if check and there is no space then make the array size double other wise next line
        if self.size == self.n:
            self.__resize(self.size*2) 
        """now running a loop and traversing in reverse to find the give position .
           The logic would be running to backward from the last number to the given position.
           So that we can insert the value at the given position. so now swapping number next position for making space.

        """   
        for i in range(self.n,pos,-1):
            self.Array[i] = self.Array[i-1]
            # poisiton:5 <----position: 4
        self.Array[pos]=value
        self.n+=1
    
    #delete uses for deleting element by their index
    def __delete__(self, pos):
        item=self.Array[pos]
        if 0<=pos<self.n:
            for i in range (pos, self.n-1):
                self.Array[i]=self.Array[i+1]
            self.n-=1
            print('Item Deleted:',item)
        else:
            return 'Position not found'
    
    #remove use for removing value by given value
    def remove(self,value):
        pos=self.find(value)
        if type(pos) == int:
            self.__delete__(pos)
        else:
            return pos
            
            
L=Meralist()
L.append('Á')
L.append('B')
L.append(1)
L.append('A')
L.append('B')
L.append(1)

# print(L.find('B'))
# # L.clear()

# print(L.find(1))
# L.insertion(2,7)
# L.insertion(6,'Hello Hanki Panki')
# print(L)
# print(L.__len__())  

L.__delete__(0)
print(L)
# print(L.__len__())  
L.remove('A')
print(L)

'''
Sort/Min/Max/Sum (Find function +)
Extend
Negative Indexing
Slicing
Merge
'''
 

