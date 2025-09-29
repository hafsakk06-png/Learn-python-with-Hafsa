# Hello students Today is our 7th day
# I hope you are doing great
# so lets start our day with some coding

#   Functions in python

# Simple function
def say_hello():
    print("Hello! Welcome to Python.")

say_hello()   # Function call

#   Functions in parameters
def greet(name):
    print(f"Hello, {name}! How are you?")

greet("Hafsa")
greet("Ali")

#   Functions with return values
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

#    Default parameters
def welcome(name="Student"):
    print(f"Welcome, {name}!")

welcome()
welcome("Hafsa")

#   Multiple return values
def calculate(a, b):
    return a + b, a - b, a * b

s, d, m = calculate(5, 3)
print("Sum:", s)
print("Difference:", d)
print("Multiplication:", m)