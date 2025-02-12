# class Student:
#     name="Anis"

# student1= Student()
# print(student1.name) 

""""
To start a class I have to declare class name 1st. the class name 
1st alphabet will be Capital letter.
after that I have to declare an object then call the class function. that are init function
then I can print or other use of class object name by add (.) and call the attribute
"""



# class Car:
    
#     #this is call default constructor
#     def __init__(self):
#         pass
    
#     #parameterized constructor
#     """ parameterized means not only self but also other attribute can be access """
#     def __init__(self, brand_name, model, price, owner_name):
#         self.brand_name=brand_name
#         self.model=model
#         self.price=price 
#         self.owner_name=owner_name
#         print(self.brand_name, self.model, self.price, self.owner_name)
    
#     def car_details(self):
#         pass 
# car1=Car("Audi","A8","1M$","Anis")
# print(car1.brand_name, car1.model, car1.price, car1.owner_name)


"""                         Attributes                   """
# to types of attribute are stay
# 1. Class.attribute
# 2. obj.attribute


"""
object attribute are  self.name, self.roll etc
thats mean object attribute will different for different value

class attribute are same for all object.
"""
# class Student:
#     # class attribute
#     school_name="BGC Trust University Bangladesh"
#     serial_number=0
#     @classmethod
#     # object attribute
#     def __init__(self, name, roll):
#         self.name=name
#         self.roll=roll
#         # class method
#         Student.serial_number+=1
#         self.serial=self.serial_number
#         print(f"Printing Student information........ {self.serial}")
#         print(f'Student Name\t\t:\t{self.name}\nStudent ROll\t\t:\t{self.roll}\nStudent College Name\t:\t{self.school_name}\n')
  
  
# """I can do this:by using list and call the function"""  
# print("This are use by list \n")
# student=[
#            Student ("Anis", "220238063"),
#            Student ("Takib", "220238046"),
#            Student ("Rakib", "220238023"),
#            Student ("Sakib", "220238065")
#         ]

# """ Or just sending one after"""

# print("This another half it only done by single single \n")
# student1=Student("Anis", "220238063")
# student1=Student("Takib","220238046")
# student1=Student("Rakib", "220238023")
# student1=Student("Sakib", "220238065")
# student1=Student("Takib","220238046")

# class Student:
#     school_name = "Chittagong Port Authority High School"
#     serial_number = 0
    
#     def __init__(self,name,roll,admitted_class,section, subject1, subject2, subject3):
#         self.name=name 
#         self.roll=roll
#         self.admitted_class=admitted_class
#         self.section=section
        
#         Student.serial_number+=1
#         self.serial=self.serial_number
        
#         #subject number adding
#         self.subject1=subject1
#         self.subject2=subject2
#         self.subject3=subject3
        
#         print(f'SI NO: {self.serial} Showing the details of student {self.name}')
#         print(f'School Name:{self.school_name}\nName\t:{self.name}\nRoll\t:{self.roll}\nClass\t:{self.admitted_class}\nSection\t:{self.section}\n')
#         self.marks() #calling marks function to display
        
#     def marks(self):
#         print(f'Marks of {self.name}')
#         print(f'{self.roll}')
#         print(f'Physics: {self.subject1}\nChemistry: {self.subject2}\nHigher Math: {self.subject3}')
#         print(f'Total Marks: {self.marks_sum()}')
#         print(f'Average: {self.marks_avg()}.2f')
    
#     def marks_sum(self):
#         return self.subject1+self.subject2+self.subject3
    
#     def marks_avg(self):
#         return (self.subject1+self.subject2+self.subject3) / 3
    

# student=[
#     Student("Anis", "220238063", "Sixth", "A",76,44,33),
#     Student("Takib", "220238046", "Sixth", "B",23,56,73),
#     Student("Rakib", "220238023", "Sixth", "A",65,12,65),
# ]

# # subject=[
# #     marks()
# # ]

# class Student:
#     school_name="Chattogram Bandar College"
#     serial_number=0
    
#     #init method write
#     def __init__(self,name,roll,section, marks_dict):
#         self.name=name
#         self.roll=roll
#         self.section=section 
#         self.physics=marks_dict["Physics"] 
#         self.chemistry=marks_dict["Chemistry"]
#         self.biology=marks_dict["Biology"]
        
#         #incrementing the seiral number
#         Student.serial_number+=1
#         self.serial=self.serial_number
#         self.show_student_details()
#         self.show_marks()
    
    
#     def show_student_details(self):
#         print(f"\nSI NO{self.serial} The result are showing of {self.name}\n")
#         print(f'School Name: {self.school_name}\nStudent Name: {self.name}\nRoll: {self.roll}\nSection: {self.section}')
    
#     def show_marks(self):
#         print(f'Student: {self.name} Roll: {self.roll}')
#         print(f'Physics:{self.physics}\nBiology: {self.biology}\nChemistry: {self.chemistry}\n')
#         print(f'Total  Marks: {self.calculate_marks()}')
#         print(f'Average: {self.avg():.2f}')
    
#     def calculate_marks(self):
#         return self.physics+self.biology+self.chemistry
    
#     def avg(self):
#         return (self.calculate_marks())/3


# marks_dict={
#     "Anis"  : {"Physics":76, "Chemistry":78, "Biology":55},
#     "Takib" : {"Physics":67, "Chemistry":55, "Biology":72}
# }
    

      
# student=[
#     Student("Anis", "220238063", "Sixth", marks_dict["Anis"]),
#     Student("Takib", "220238033", "Sixth", marks_dict["Takib"] )
# ]

# class Data:
#     def __init__(self,name):
#         self.name=name
         
#     @staticmethod # this are call decorator. Decorator usually changing the 
                    #behaviour of 
#     def hello():
#         print("Hello, World!")

# student=Data('anis')
# student.hello()
        
"""
 Static method usually use for making the method
 which is not depend on the object. so it no need to any
 self keyword also it was class level method
"""       

"""                       In OOP there are 4 types of pillar
                                        |
            ---------------------------------------------------- 
             |              |               |                  |
           Abstraction    Encaptulation   Inheritance     Polymorphism

Abstraction: Hiding the implementation details of a class and only showing the essential
features of the user.
Unnecesary thing are hidden not to shown the user. Like a user using
in pc what is happening inner body that are user dont know they just use the
product.

Encapsulation: Wrapping data and function in to a single unit (obejct).
"""

#Abstraction example:

# class database:
#     def __init__(self, name, roll):
#         self.name=name 
#         self.roll=roll
    
#     def prin(self):
#         print(f'hello world')
        
# sub=database('anis', 33)
# sub.print()

#Encapsulation    
"""
Encapsulation means the data and function wrapup together. 
Like a capsule the madicine that are covered with a shell
""" 



"""""                        Lectore 9: OOPS Part 2 """

#deleting object in class
# class Student:
#     def __init__(self, name, roll):
#         self.name=name
#         self.roll=roll

# s1=Student("Anis", 123)
# print(s1.name)
# del s1
# print(s1.name)
            

"""
In OOP(Object Oriented Programming) there are two
type of attribute declaration one is 

1. Public attribute/method
2. Private attribute/method
"""
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass      #private attribute
#     def __reset(self):          # private method
#         print(self.__acc_pass)
#     def show(self):
#         self.__reset()

# acc1=Account("12345","abcdef")
# print(acc1.acc_no)
# # print(acc1.__acc_pass)
# print(acc1.show())

"""
Private(like) attributes & methods
Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.
"""

"""
                                Inheritance
"""
