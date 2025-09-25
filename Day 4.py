#Hello Everyone
# So today we will learn about conditional statements in python
# Conditional statements are used to perform different actions based on different conditions.
# In Python, we have the following conditional statements:
# 1. if statement
# 2. if...else statement
# 3. if...elif...else statement

# Let's see how each of these work with examples

# Example of if statement
age = 18
if age >= 18:
    print("You are eligible to vote.")

# Example of if...else statement
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Example of if...elif...else statement
age = 20
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# You can also have nested if statements
num = 10
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number")
   
    #short-hand if else
    x = 5
y = 10

# One-line if
print("x is greater") if x > y else print("y is greater")

# That's it for today! Practice these conditional statements to get a better understanding.
# I hope you all will try these examples on your own and do let me know if you have any questions.
# See you all tomorrow with a new topic.
# Keep learning and keep exploring.
# Happy coding!  :)
