# Type Checking and Type Casting
username = input("Enter your name?")
namelenght = len(username)

print(type("Number of letters in your name: ")) #str
print(type(namelength)) #int

print("Number of letters in your name: " + str(namelength))
# OR
print("Number of letters in your name: " + str(len(input("Enter your name"))))

#Math Operators
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3) # Python's implicit typecasting
print(5 // 3) # Dangerous: Trucates the floating valeu after the comma
print(2 ** 3) # Exponents - 2 to the power of 3

""" When you have multiple math operators in one line of code PEMDASLR is the order of execution:
 1 Parentheses, 2 Exponents, 3 Left to Right Multiplication/Division, 4 Left to Right Addition/Subtraction
"""
print(3 * 3 + 3 / 3 - 3) # Order 1: 3*3, 2: 3/3, then 9 + 1 - 3 = 7

# To get a total of 3 using Parenthese
print(3 * (3 + 3) / 3 - 3) # Order 1: 3 + 3, 2: 3 * 6, 3: 18 / 3 then 6 - 3 = 3

""" Create a calculator to test someone's BMI using mathematical operators in Python. 
The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. 
This is the formula used to calculate it:
bmi is equal to the person's weight divided by the person's height squared. """
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight/height ** 2

print(bmi) # 30.85399449035813
print(int(bmi)) # 30 - Flooring the number
print(round(bmi)) # 31 - Rounding the number



