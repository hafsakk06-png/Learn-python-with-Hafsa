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

    #*args and kwargs

#These allow you to pass a variable number of arguments to a function.

def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  # Output: 10


# *args → collects multiple positional arguments into a tuple.

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Hafsa", age=20, city="Lahore")


# **kwargs → collects multiple keyword arguments into a dictionary.

# Lambda Functions

# Lambda = small, single-line anonymous function.

square = lambda x: x * x
print(square(5))


# Same as:

def square(x):
    return x * x