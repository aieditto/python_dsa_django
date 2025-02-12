                                    #Lecture-3: List & Tuple in python
                                    
""" list is kind of container of many element of different type. we can store integer, float, string, double type.
    list is almost like array but the difference is array can only store same type element but in list or tuple can store
    different type element.
    
    (tuple), [list], {set:set}
"""

#add fruits name as tuple. tuple is kind of array
# fruit=['Apple','Mango', 'Guava', 'Jack Fruit', 'Pineaplle', 'Strawberry']
# fruit=["Apple","Mango", "Guava", "Jack Fruit", "Pineaplle", "Strawberry"]
# fruits=("Apple","Mango", "Guava", "Jack Fruit", "Pineaplle", "Strawberry")
# print(fruit)
# print(len(fruit))
# print(f'this is list:',type(fruit))
# print(f'this is tuple:',type(fruits))
# print(fruit[1])


"""
List are mutable that means by accessing element throw the index it can be changeable value

"""
# student_information_list=['Anis',63,'CSE','BGC Trust University Bangladesh']
# # print(student_information_list)
# student_information_list[0]='Amzad'
# print(student_information_list)


#                         #List slicing
# student_information_list=['Anis',63,'CSE','BGC Trust University Bangladesh']
# print(student_information_list[0:3])


#List Methods

# list = [2,1,3]
# list.append(4) #add number at thelast
# print(list)

# list.sort() #list sorting
# print("Ascending Sorted", list)

# list.sort(reverse=True) #sorting descending 
# print("Descending SOrted reverse",list)

# list.reverse() #reversing the whole list
# print("Reverse list",list)

# str=['a','e', 'd', 'g', 'q']
# str.reverse() #reversing all sorted can be apply for the string in list
# print(str)

# list.insert(3, 5)  # this is kind of append but it will apply on targeted index like variable.insert(index.value)
# print(list)

# str.pop(3)  # pop use for deleting element by index from the list here str=['a','e', 'd', 'g', 'q']
# print(str)  # but after deleted this are ['q', 'g', 'd', 'a'] because index 3 are 'g'

# var=[1,54,2]
# var.remove(54) # remove use for deleting the targeted value
# print(var)




                                        #Tuple

""" A built in data type that lets us create immutable sequences of values.

The big difference between List and Tuple is:
            1. List is mutable and Tuple is immutable.
            
    that means tuple values cant change.
"""                                     

# tupple=(5,)
# print(type(tupple))

# # empty tupple
# tup=()
# print(tup)


# #tuple slicing
# tupple1=(4,6,7,2,76,3)
# print(tupple1[2:])

# #finding element from tuple
# tupple2=('Anis', 'Sakib', 'Rakib', 'Farjana', 'Takib')
# print(tupple2.index('Rakib'))
# print(tupple2.count('Farjana'))


"""                                     ""Question""                """
"""Question: Take input from the user and make a list of movies name """
# movie=[]
# movie.append(input("Enter the movie name 1: "))
# movie.append(input("Enter the movie name 2: "))
# movie.append(input("Enter the movie name 3: "))
# print(movie)

"""Question 2: Check if the word is palindrome or not"""
# pal=[1,2,3,2,1]
# check_palindrome=pal.copy()
# check_palindrome.reverse()
# if(check_palindrome==pal):
#     print("it is palindrome")
# else:
#     print("it is not palindrome")




