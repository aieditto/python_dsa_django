
# info={
#     "Name":"Anis",
#     "Roll": 63,
#     "Section":"A",
#     "Semester":"6th"
# }
# print(info)
# print(type(info)) # type of dictionary
# print(len(info)) # length of the dictionary
# print(info["Name"]) # calling value by key
# info["Name"] = "Jakir" #changing the value by key and it overwrite the previous key
# info["Mobile"]= "01898234324" # add new key and value to dictionary
# print(info)




# #                           """ Nested Dictionary """

# Student_info = {
#     "name": "Md Anisul Islam",
#     "subjects" : {                  #nesting
#         "Java" : 75,
#         "Data_structure": 66,
#         "Algorithm": 44,
#         "python":67
#     }
# }
# print(Student_info)
# print(f"The Number of Java is {Student_info['subjects']['Java']}") #printing the targeted subject number by their key which are nested under subject key

# #print key

# print(type(Student_info))

# print(type(list(Student_info.keys()))) #typecasting to list then show the type

# print(Student_info.values()) #print all the values

# print(Student_info.items()) #print all the keys and values as a tuple

# print_key_value_as_tuple=list(Student_info.items()) #typecasting to list
# print(print_key_value_as_tuple[1]) # print exact key and value by index but it won't access the nested key and value

# #find  the key by value
# print(Student_info.get("name")) 
# """
# It also like finding the value by key but there was a difference when
# we write direct process 
# print(Student_info["name2"] if there was no any name2 keys then it will show error
# but get() function will return None if there was no any key.
# So, when we write a big code then it will toughest task where was the exactly problem?
# thats why 
# Student_info.get() must be use
# """


                        
                        
                        
                        # Set in python
                        
collection={1,2,3,4}
print(collection)
print(type(collection))

data={'Anis', 3,4,5.5}
print(data)
print(type(data))
""" Set are unorder that means it can not follow indexing.
Also set are mutable and set are accept different types value"""
print(len(data))

#for making empty set write:
emptyset=set()
print(type(emptyset))

#set.add(el) add an element
#set.remove(el) remove an element
#set.clear() #empties the set
#set.pop() removes a random value
#set.discard(el) removes an element if it exists

emptyset.add(1)
emptyset.add(2)
emptyset.add(3)
print(emptyset)

emptyset.remove(2)
print(emptyset)

emptyset.pop()
print(emptyset)

emptyset.clear()
print(emptyset)

"""you can add multiple type value and add also like tuple. But cant
add list. Because list are mutable. But set element are not mutable. set are actually mutable thats why 
the value cant be change"""
emptyset.add((3,5,6,'anis'))
print(emptyset)



set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
"""
set.union() combined between two variables value.

set.intersection() intersect between two variable. that means
it will take common value from both of the set.
"""