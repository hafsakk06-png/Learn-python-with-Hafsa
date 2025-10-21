# Hello my lovely coders I hope you all will fine and doing good
# Now start our 15th Day python code

# Default Parameters

# When a function parameter has a default value, it doesn’t need to be passed every time.

def greet(name="Student"):
    print("Hello,", name)

greet()           # Output: Hello, Student
greet("Hafsa")    # Output: Hello, Hafsa

# Keyword Arguments

# You can specify parameter names while calling a function.

def intro(name, age):
    print(f"My name is {name} and I am {age} years old.")

intro(age=20, name="Hafsa")

#Return Multiple Values

# A function can return multiple results at once using a tuple.

def calculator(a, b):
    return a + b, a -