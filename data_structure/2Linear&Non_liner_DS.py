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
    
    
    def append(self, item):
        if self.n == self.size:
            #resize
            self._resize(self.size*2)
        
        #append
        # jodi jaiga khali thake shei khetre array er Nth jaigai value boshe
        # jaa ager n e chilo ta toh  item e thake sheta abr notun n rakha hoi erpr 1 kre increment kre dei size
        self.Array [self.n] = item
        self.n=self.n+1
    
    def _resize(self, new_capacity):
        #create a new array with new capacity
        B_NEW_Array = self.__make_array(new_capacity)
        self.size = new_capacity #already double size than Array
        #copy Array element to B_NEW_Array
        
        
            
    def __make_array(self, capacity):
        #creates a C type array(static,referential) with size-->capacity
        return (capacity*ctypes.py_object)()