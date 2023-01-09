# Hello World
print('Remember the Python')
# Integer - Float
print(56 / 7)  # equals 8
print(54.25 / 7.1)  # 7.64
# Variables
a = 10
b = 3
c = a + b
print(c)
a, b = b, a  # relocate
print(a, b)
print(a)
i = 5
i += 1
# Mathematics Operators
print(345 // 7)  # integer division
print(13 % 4)  # remainder
print(4 ** 3)  # exponent
print(4 ** 0.5)  # sqrt
#  Strings
print('Ilyurek Kilic')
x = "Gender"
print(x[3])  # returns d
print(x[-3])  # returns d
print(x[0:3])  # returns Gen
print(x[::-1])  # reverse
# Properties of Strings
print(len(x))  # length
y = "Man"
print(x + y)
# str does not support item assignment

# Type conversion

# integer to float
a = 43
a = float(a)
print(a)

# float to integer
b = 4.7
b = int(b)
print(b)

# integer to string
a = 24
a = str(a)
print(a)

# Print and Format
print("ilyurek")
print("İlyurek","Kılıç",2429157)

# /n and /t
print("İlyurek\nKılıç")
print("İlyurek\tKılıç")

# parameters of print function
print("İlyurek","Kılıç",2429157,sep="\n")
print("06","04","1997",sep="/")
# *
print(*"Python",sep="/")
print(*"TBMM",sep=".")
# format function
a = 3
b = 4
print("{} + {} equals {}".format(a,b,a+b))

# Lists
temp = ["Apple",35,"Hello",3.14]
print(len(temp))

# indexing and slicing
print(temp[2])
print(temp[-1])
print(temp[len(temp)-1]) # last value in list
print(temp[::-1]) # inverse of list

temp[:2] = [10,11] # change first two value
print(temp)

# methods

# append
temp.append("Python") # to add value to end of the list
print(temp)
# pop
temp.pop(0) # to discard item from the list
print(temp)
# sort both numerical and alphabetic
a = [1,4,2,5,9]
a.sort(reverse=True)
print(a)

# list in a list
a=[[2,2],[3,3],[4,4]]
print(a[2][0]) # gives you four

# Tuples
a = (1,2,3,2,4,3,2,3,4,1)
print(a[0])

# methods

# count
print(a.count(2)) # returns count of item in tuple
# index
print(a.index(2)) # returns index of item in tuple

# tuples do not support item assignment

# Dictionaries

d = {"One":1,"Two":2,"Three":3}
print(d)
print(d["One"])
d["Four"] = 4
print(d)
a = {"numbers":{"One":1,"Two":2,"Three":3},"fruits":{"orange":"winter","watermelon":"summer"}}
print(a)

# methods

print(d.keys()) # returns keys
print(d.values()) # returns values
print(d.items()) # returns tuples

# Input from user

a = int(input("Please Enter a Number"))
print("The Value is",a)
print(type(a))

# Boolean

a = True
print(type(a))
print(1 == 0)  # Returns False
print("Car" <= 'Desk')

# Logical Conjunctions

print((1 == 0) and "Car" <= 'Desk')  # False
print((1 == 0) or "Car" <= 'Desk')  # True
print(not 1 == 0)  # True

# Conditional States

a = 2
if a == 2:
    print(a)
    
# if-else

age = int(input("Please Enter Your Age"))

if age < 18:
    print("You shall not pass")
else:
    print("Welcome on Board")
    
# if-elif-else

grade = int(input("Please Enter Your Grade"))

if grade >= 70:
    print("High Honor")
elif grade >= 50:
    print("Honor")
else:
    print("FF")
    
# Loops
# In operator
print(5 in (1, 2, 3, 4))

# For loop-1
a = [1, 2, 3, 4, 5, 6, 7]
for i in a:
    print("Item", i)
b = [1, 2, 3, 4, 34, 63, 79]
for i in b:
    if i % 2 == 0:
        print(i)
# For loop-3
s = "Python"
for i in s:
    print(i)
# For loop-4
k = [(1, 2), (3, 4), (5, 6), (7, 8)]
for i in k:
    print(i)
# For loop-5
for i, j in k:
    print(i, "and", j)
# For loop-6
n = {"One": 1, "Two": 2, "Three": 3}
for i in n:
    print(i)
# For loop-7
for i in n.values():
    print(i)
# For loop-8
for i, j in n.items():
    print(i, j)
# While loop-1
counter = 0
while counter < 10:
    print(counter)
    counter += 1
# While loop-2
index = 0
a = [1, 2, 3, 4, 5]
while index < len(a):
    print('index:', index, "item", a[index])
    index += 1

# range()

print(*range(0, 20))
print(*range(0, 100))
print(*range(1, 20))
print(*range(15))  # Starts from 0
print(*range(1, 100, 2))
print(*range(20, 0, -1))  # descending
for i in range(1, 10):
    print("*" * i)
    
# break&continue

i = 0
while i < 20:
    if i == 5:
        break
    print(i)
    i += 1

while True:
    name = input("Enter your name for exit press 'q' ")
    if name == "q":
        break
    print(name)

a = list(range(11))
for i in a:
    if i == 3 or i == 5:
        continue
    print(i)
    
# list Comprehension

temp = [1,2,3,4,5]
temp1 = [i for i in temp]
print(temp1)
temp2 = [(1,2),(3,4),(5,6)]
temp2 = [i*j for i,j in temp2]
print(temp2)
temp3 = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
temp3 = [x for i in temp3 for x in i]
print(temp3)
# Methods

a = [1, 2, 3, 4, 5]
a.insert(1, "İlyürek")
print(a)
help(a.pop)  # to remember


# Functions
def hi(name):
    print("your name is", name)


print(type(hi))
hi(name="İlyürek")


def summy(a, b, c):
    print(a + b + c)


summy(3, 5, 8)


def fact(number):
    fact = 1
    if (number == 1 or number == 0):
        print(fact)
    else:
        while number >= 1:
            fact *= number
            number -= 1
        print(fact)

fact(4)
