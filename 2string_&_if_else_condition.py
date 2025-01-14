
               
                            
                                
                                    # Chapter-2 Strings and conditional statements

str1= "This is a string"
str2= 'ApnaCollege'
str3= """This is a string"""

# escape sequence

# \' 	Single Quote 	
# \\ 	Backslash 	
# \n 	New Line 	
# \r 	Carriage Return 	
# \t 	Tab 	
# \b 	Backspace 	
# \f 	Form Feed 	
# \ooo 	Octal value 	
# \xhh 	Hex value

                                                #Strings
"""Concatenation"""
""""concatenation means merging two string together """

# for example:
        
# nam1="Anis"
# nam2="ul Islam"
# print(nam1+nam2)

# result= "Anisul Islam"

                        #Indexing
""""What is indexing?
Indexing is the number of the character which has written.
For Example:
        anis, it has 4 character so the indexing is     a n i s
                                                        1 2 3 4 """

                                                        
# num= "anis"
# print(num[1])   #to access 
# print(num[0:4])
# # result: anis

# print(num[0:]) # to access all character
# print(num[1:2]) # its called slicing
# print(num[:4])
# print(num[-4:-0]) #its called reverse


#String Function

# str = "i am a coder"
# result=str.endswith("er")  #endswith use for finding the substring. if it find then it return TRUE
# print(result) 

# print(str.capitalize()) #capitalize first character
# print(str.replace('coder', 'good one'))
# print(str.find('coder'))

# paragraph = "the symmu dade fdxv sate gsfh gffa gfd"
# print(paragraph.find('gfd')) #find the string as index
# print(paragraph.count("gsfh")) #count the given string


# find=paragraph.find('symmu')
# count=paragraph.count('m')
# print(f"So the number of m in '{find}' word is '{count}")

                                
                                
                                
                                
                                #If-Else Condition

# age = int(input("Enter Your age: "))
# if(age>=18):
#         print("You are eligible for vote")
# else:
#         print(f"You are not eligible for vote bcause your age is {age}")
        
 
# marks= int(input("Enter Your Marks: "))

# if(marks>=90):
#         print("A")
# elif(marks>=80):
#         print("B")       
# elif(marks>=70):
#         print("C")
# elif(marks>=60):
#         print("D")
# elif(marks>=50):
#         print("E")
        
"""Question No:1 
Write a program that asks the user for their age and then prints out the category they belong to:
        Child (0-12 years)
        Teen (13-19 years)
        Adult (20-59 years)
        Senior (60+ years)
"""