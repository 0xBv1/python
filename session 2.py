# Integer Example
x = 1  # int

# String Examples
y = "ahmed"  # str
y = 'ahmed'

# Boolean Example
z = True  # bool

# Float Example
s = 1.3  # float

# Convert integer to string
x_str = str(3)  # x_str will be '3'

# Print and check type
print(x)
print(type(x))  # <class 'int'>

# Input and convert to integer
n = int(input("Enter first number: "))
v = int(input("Enter second number: "))
print("Sum:", n + v)
print("Type of sum:", type(n + v))  # <class 'int'>

# Convert integer to string for concatenation
x = 1
print("Converted to string:", str(x))

# Basic input and summation
print("Welcome")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print("Sum of " + num1 + " and " + num2 + " = " + str(int(num1) + int(num2)))

# Combining integer and string with type conversion
x = 1
y = "2"
print(x + int(y))  # 3

# Assigning multiple variables at once
x, z, c = 1, 2, 3
print(x, z, c)

x = z = c = 1
print(x, z, c)

# Assigning the same value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# String indexing
x = "ahmed"
print(x[1])  # h

# String length
x = "ahmgsdfgasdfasdfed"
print(len(x))  # Length of string

# String slicing and searching
txt = "The best things in life are free!"
print(txt[1:])  # Starting from index 1
print("best" in txt)  # True

# More string slicing
x = 'ahmed2'
print(x[0:3])  # ahm

# String case methods
x = "hello world"
print(x.upper())  # HELLO WORLD
print(x.lower())  # hello world

# Removing whitespace
x = "    Hello world            "
print(x.strip())  # Hello world

# Replace substring
x = "Hello world"
print(x.replace("ll", "#"))  # He##o world

# Escape characters
x = "welcome \"bedo\""
print(x)  # welcome "bedo"

# String tasks
txt = " Hello World "
# 1. Remove whitespace
print(txt.strip())
# 2. Convert to uppercase
print(txt.upper())
# 3. Replace H with a
print(txt.replace("H", "a"))

# More string slicing
x = 'Welcome'
print(x[3:5])  # co
print(x[2:5])  # lco
print(x[3:])   # come

# Type conversions
print(int(35.25))  # 35
print(float(23))   # 23.0
print(str(23))     # "23"
print(type(str(23)))  # <class 'str'>
print(int(35.55))  # 35
