# Function Return Values
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

#Multiple Return Values
def calculate(a, b):
    sum_ = a + b
    diff = a - b
    return sum_, diff

x, y = calculate(10, 5)
print("Sum:", x)
print("Difference:", y)

#Default Parameters
def greet(name="Guest"):
    print("Hello,", name)

greet("Hafsa")
greet()

#Recursion (Function calling itself)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Keep coding and exploring more about functions!
# Happy coding!