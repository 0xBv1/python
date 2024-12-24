# session3

# Boolean examples
x = True
y = False

print(type(x))  # <class 'bool'>
print(10 > 5)  # True
print(10 < 5)  # False
print(10 == 5)  # False

# Operations on boolean values
print(x + y)  # 1 (True is 1, False is 0)
print(x - y)  # 1
print(x * y)  # 0
# print(x / y)  # Division by zero error if uncommented

# Modulus operation
# print(x % y)  # Division by zero error if uncommented

# Exponentiation
print(x ** y)  # 1

# Floor division
# print(x // y)  # Division by zero error if uncommented

# Increment and decrement operations
x = 1
x += 1  # Increment by 1
print(x)
x -= 1  # Decrement by 1
print(x)

# Comparison operators
x = 1
y = 2
print(x < y)  # True
print(x > y)  # False

# List examples
x = [1231, "fasdfsdf", True, 1.5, [123, 123123, "sdfsf"]]
print(x[1])  # "fasdfsdf"
print(x[0])  # 1231
print(x[1][0])  # "f"
print(len(x))  # 5
print(x[-1][-1][-1])  # "f"

# Nested lists
x = [1231, "fasdfsdf"]
x1 = [1.5, [123, 123123, "sdfsf"]]
x2 = [True]
new_list = [x, x1, x2]
print(type(new_list))  # <class 'list'>

# Modifying lists
x = [1231, "fasdfsdf", True, 1.5, [123, 123123, "sdfsf"]]
x[1:3] = ["sdsf"]
print(x)

# Insert, append, and extend methods
x = [1231, "fasdfsdf", True, 1.5]
x.append("test")
x.append("test1")
print(x)

# Extend method
x = [1231, "fasdfsdf"]
x1 = [1.5, [123, 123123, "sdfsf"]]
x2 = [True]
new_list = x + x1 + x2
print(new_list)

# Remove and pop methods
x = [1231, "fasdfsdf", 231, "f", 121, "fasf"]
x.pop(2)  # Removes item at index 2
x.pop()  # Removes the last item
print(x)

# Deleting items
x = [1231, "fasdfsdf", 231, "f", 121, "fasf"]
del x[2]
print(x)

# Clear method
x = [1231, "fasdfsdf", 231, "f", 121, "fasf"]
x.clear()
print(x)

# Looping through a list
x = [1231, "fasdfsdf", 231, "f", 121, "fasf"]
for i in x:
    print(i)

# Sorting a list
x = [5, 8, 1, 3, 5, 7, 4, 8, 2, 5, 0, 1, 4]
x.sort()
print(x)

x.sort(reverse=True)
print(x)

x.reverse()
print(x)

# Copying lists
x = [5, 8, 1, 3, 5, 7, 4, 8, 2, 5, 0, 1, 4]
y = x.copy()
print(y)

# Using slicing to copy
x = [5, 8, 1, 3, 5, 7, 4, 8, 2, 5, 0, 1, 4]
y = x[:]
print(y)

# Joining lists
x = [4, 8, 2, 5, 0, 1, 4]
y = [1]
for i in x:
    y.append(i)
print(y)

# Count method
x = [4, 8, 2, 5, 8, 1, 8]
print(x.count(8))

# Index method
x = [4, 8, 4, 5, 8, 1, 8]
x.sort()
print(x.count(4))
print(x.index(4))

# Sample operations on fruits list
mylist = ['apple', 'banana', 'cherry']
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(mylist[0])  # First item
print(len(mylist))  # Number of items
print(fruits[-1])  # Last item
print(fruits[1:5])  # Items from index 1 to 5

fruits[0] = "grape"  # Change first item
if "apple" in fruits:
    fruits[fruits.index("apple")] = "kiwi"  # Change "apple" to "kiwi"

mylist[1:2] = ["kiwi", "mango"]
print(mylist[2])  # "mango"

fruits.pop()  # Remove last item
fruits.remove("banana")  # Remove "banana"
fruits.clear()  # Remove all items

for fruit in fruits:
    print(fruit)  # Print all items using for loop

i = 0
while i < len(fruits):
    print(fruits[i])  # Print all items using while loop
    i += 1

fruits.sort()  # Sort in ascending order
fruits.sort(reverse=True)  # Sort in descending order
