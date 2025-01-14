"""
Function are started by def and then any type of
variable name with braces. 
for example:
def function_name():

function has parameter and argument

def function_name(a,b)  a and b are parameter and whole thing are called
       some logic.....   function definition

function_name(a,b)      this are called function calling and the passing value are called argument.

"""
# def summition(a,b):
#     sum=a+b
#     print(sum)
#     return sum

# a=6
# b=5
# summition(a,b)
# a=4
# b=3
# summition(a,b)

"""print from large number to small number"""
# def show(n):
#        if(n==0):
#               return
#        print(n)
#        return show(n-1)

# print(show(5))

# """print n factorial number by recursion"""

# def fact(n):
#        if(n==0 or n==1):
#               return 1 
#        return fact((n-1))*n
       

# print(fact(5))


"""Implement a recursive function to find the nth Fibonacci number."""

def num(n):
       def fibonacci(n):
              if (n==0):
                     return 0
              elif (n==1):
                     return 1
              else:
                     return fibonacci(n-1)+fibonacci(n-2)
       
       store=[]
       for i in range(n):
              store.append(fibonacci(i))
       
       return store
       
       # series=[fibonacci(i) for i in range(n)]
       # return series
       


print(num(10))

