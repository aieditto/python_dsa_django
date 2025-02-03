"""
Linked list is basically a collection of nodes.

Two variable need 1 is data and other is address of the next node
"""
# #Making Node
# class Node:
#     def __init__(self, value):
#         self.data=value
#         self.next=None

# a = Node(1)
# b= Node(2)
# c= Node(3)
# print(id(a)) #496-a   304-a     208-b   NOne-c
# print(id(b))
# # print(id(c))
# a.next=b
# # b.next=c

# # print(a.next)
# print(int(0x000001A68272BEE0))

"""
The first linked list node will be empty. The node are called head that next address will be none. 
Because no other address are added with that.
"""
class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
#creating a linked list
class LinkedList:
    def __init__(self):
        
        #Empty Linked List
        self.head=None
        #No of nodes in the Linked List
        self.n=0
    
    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        #Creating a new node
        new_node=Node(value)
        
        #creating connection
        new_node.next=self.head
        
        #reassign head
        self.head=new_node
        
        #increment n
        self.n=self.n+1
        
        
first=LinkedList()
print(first.__len__())
