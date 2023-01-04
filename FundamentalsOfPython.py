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

