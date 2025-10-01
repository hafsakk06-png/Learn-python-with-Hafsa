# Hello my cute coders
# i hope you all are doing great

# Today we learn Practice Problems
# Find the Factorial of a Number
num = 5
fact = 1

for i in range(1, num+1):
    fact *= i

print("Factorial of", num, "is:", fact)

#Check if a Number is Prime
num = 29
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is Prime")
else:
    print(num, "is Not Prime")

#Reverse a String
text = "Python"
reversed_text = text[::-1]
print("Original:", text)
print("Reversed:", reversed_text)

#Fibonacci Series (first 10 terms)
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a+b

    # so this is all for today
    # I hope you like it
    # see you tomorrow
    # keep learning and keep exploring 
    # Happy coding 
    # byeeeeeee