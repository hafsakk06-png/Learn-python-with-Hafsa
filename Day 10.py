# Hello everyone today is our 10th day
# I hope you are doing best

#     Functions (Part 2)

# Default Arguments

def greet(name="Guest"):
    print("Hello,", name)

greet("Hafsa")   # Output: Hello, Hafsa
greet()          # Output: Hello, Guest

#  Return Multiple Values

def calculate(a, b):
    return a+b, a-b, a*b

x, y, z = calculate(5, 3)
print("Sum:", x)
print("Difference:", y)
print("Product:", z)

#  Keyword Arguments

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Hafsa")

#Variable-Length Arguments

Example – *args (multiple values as tuple)
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(2, 3))          # Output: 5
print(add_numbers(1, 2, 3, 4, 5)) # Output: 15

Example – **kwargs (multiple values as dictionary)
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_info(name="Hafsa", age=20, course="Python")






#   Happy coding my python coders
#   keep smiling and always be happy
#   keep learning and keep exploring
#   May Allah bless you
#   Byeeee