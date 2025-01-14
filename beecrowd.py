
# Problem no 2

"""A=int(input())
B=int(input())
result= print("X=",A+B,end="")"""

# problem no 3
'''The formula to calculate the area of a circumference is defined as A = π . R2. Considering to this problem that π = 3.14159:
Calculate the area using the formula given in the problem description.
Input
The input contains a value of floating point (double precision), that is the variable R.
Output
Present the message "A=" followed by the value of the variable, as in the example bellow, with four places after the decimal point. Use all double precision variables. Like all the problems, don't forget to print the end of line after the result, otherwise you will receive "Presentation Error".'''

R = float(input())
result = 3.14159 * R * R
print(f"A={result:.4f}")

