# Hello everyone, welcome to Day 13 of the Advent of Code challenge!
#  Lists (Part 1) — Basics, Indexing & Looping
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Hafsa", 22, True, 5.7]

#Accessing List Elements (Indexing)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[2])   # cherry

#Negative Indexing
print(fruits[-1])  # cherry
print(fruits[-2])  # banana

# Slicing a Lists
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]

# Looping Through a List
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

    #Check if an Item Exists
if "banana" in fruits:
    print("Yes, banana is available!")

    #List Length
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5
