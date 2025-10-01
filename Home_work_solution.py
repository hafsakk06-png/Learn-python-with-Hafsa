# Hello my friends
# This a solution of your homework
# I hope you will like it

# print a table od any number
num = 7
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

    #  Make a pyramid pattern with *
rows = 5
for i in range(1, rows+1):
    print(" " * (rows-i) + "*" * (2*i-1))

    #Print sum of first 10 natural numbers using a loop
sum_num = 0
for i in range(1, 11):
    sum_num += i

print("Sum of first 10 natural numbers:", sum_num)