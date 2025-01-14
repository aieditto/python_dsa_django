# cont=1
# while cont<=5 :
#     print("Hello")
#     cont +=1

"""Print numbers from 100 to 1""" 
# count=100
# while count>=1:
#     print(count)
#     count-=1

"""Print the multiplication table of a number n"""
# n=int(input("Ënter the number n"))
# val=1
# while val<=10:
#     print(n*val)
#     val+=1
    


""" Print the eleents ofthe following list using a loop
    [1,4,9,16,25,36,49,64,81,100]
"""
# index=0
# numbers=[1,4,9,16,25,36,49,64,81,100]
# while index<=len(numbers)-1:
#     print(numbers[index])
#     index+=1


""" make this a tuple 
    [1,4,9,16,25,36,49,64,81,100]
    find number from the tuple
"""
# number=(1,4,9,16,25,36,49,64,81,100)
# index=0
# print("1,4,9,16,25,36,49,64,81,100")
# search_number=int(input("Enter number for search: "))
# while index < len(number):
#     if (number[index] == search_number):
#         print("Number found", index)
#     index+=1

    
# index=0
# while index<10:
#     print(index)
#     if(index==3):
#         break
#     index+=1

# index=0
# while index<10:
#     if(index==3):
#         index+=1
#         continue
#     print(index)
#     index+=1
    
# index=0
# while index<10:
#     if(index%2 != 0):
#         index+=1
#         continue
#     print(index)
#     index+=1

"""
Print the elements of the  following list using a loop:
[1,4,9,16,25,36,49,81,100]
"""

# numbers=[1,4,9,16,25,36,49,81,100]
# for val in numbers:
#     print(val)

"""
Search for a number x in this tuple using loop:
(1,4,9,16,25,36,49,81,100)
"""

# x=int(input("Enter the number: "))
# index=0
# numbers=(1,4,9,16,25,36,49,81,100)
# for val in numbers:
#     if x==val:
#         print(index)
#     index+=1
    
"""
range() function is used to generate 
a sequence of numbers starting from 0 up to but not including.
The default value will start from 0 and it has step. usually step default value are
1 but it can be change as per needed.

so in range 
there are: start, stop and step
range(start, stop, step)

for example:
"""

"""Print odd/even number or print 1 to 100"""
# for i in range(2,100,2):
#     print(i)

# """Print 100 to 1"""
# for i in range (100,0,-1):
#     print(i)
    
# """"Print the mulptiplication for number"""
# num=int(input("Enter the number: "))
# for i in range(1,10):
#     print(num*i)

""" Wap to find the sum of first n numbers (using while)"""
# num=int(input("Enter the number: "))
# i=1
# sum=0
# while i<=num:
#     sum+=i
#     i+=1
# print(sum)

# sum=0
# num=int(input("Enter the number: "))
# for i in range(1,num+1):
#     sum+=i
#     i+=1
# print(sum)

# """factorial number"""
# factorial=1

# num=int(input("Enter the number: "))
# # while i<=num:
# #     factorial*=i
# #     i+=1
# for i in range(1,num+1):
#     factorial*=i
# print(factorial)

"""Pass keyword use. Usually pass keyword use when 
no need to do anything but you have to run loop.
"""
for i in range(1,6):
    pass