# Hello everyone, welcome to Day 14 of the coding challenge!
# Let's dive into today's task.
# Functions (Advanced Concepts)
#By now, you already know what functions are — blocks of code that run when called.
#Today, we’ll go a bit deeper — covering arguments, return values, and lambda functions.

# Function Recap

def greet():
    print("Hello, Python Learner!")

greet()

#Parameters and Arguments

#Parameters are variables in the function definition.
#Arguments are the actual values you pass when calling the function.

def greet(name):
    print("Hello", name)

greet("Hafsa")

# Return Statement

#Functions can return data back to where they were called.

def add(a, b):
    return a + b

result = add(5, 10)
print(result)

# Default Arguments

# If no value is passed, Python uses the default one.

def greet(name="Learner"):
    print("Hello", name)

greet()
greet("Hafsa")

#Keyword Arguments

# You can specify arguments by name (not just order).

def intro(name, age):
    print(f"My name is {name} and I am {age} years old.")

intro(age=20, name="Hafsa")

# Variable-Length Arguments

# When you don’t know how many arguments you’ll get:

def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4, 5))

# Lambda (Anonymous) Functions

# Used for short, one-line operations.

square = lambda x: x * x
print(square(5))
