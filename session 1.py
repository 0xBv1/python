# set's write our first Python file, called helloworld.py, which can be done in any text editor.
print("Hello, World!")

# Variables in Python:
x = 5
y = "Hello, World!"
# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.
# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"


# Comments in Python:

#This is a comment.
print("Hello, World!")

print("Hello, World!") #This is a comment

#This is a comment
#written in
#more than just one line
print("Hello, World!")


# Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

# Example
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# Creating Variables
# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
name = "Python"
print("I love", name)

# Taking user input
name = input("What is your name? ")

#  Displaying user input
print("Hello, " + name + "! Nice to meet you.")

# task1:
# Write a code that welcomes the user when the program starts.
# Use input() to collect the user's name and age.
# Print a welcome message that includes the user's name.
# !!optional!! Perform a simple arithmetic operation using numbers entered by the user.
